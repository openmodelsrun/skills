#!/usr/bin/env python3
"""
Skills Registry Validation Script

Validates all skill YAML files against the JSON Schema,
checks for duplicate IDs, and verifies category references.

Usage:
    python validate.py
"""

import sys
import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from jsonschema import Draft7Validator


@dataclass
class ValidationError:
    """Represents a validation error for a specific field"""
    field: str
    message: str
    expected: str
    actual: str


@dataclass
class ValidationResult:
    """Result of validating a single file"""
    valid: bool
    errors: List[ValidationError] = field(default_factory=list)


@dataclass
class ValidationReport:
    """Complete validation report for the skills registry"""
    success: bool
    total_files: int = 0
    valid_files: int = 0
    invalid_files: int = 0
    errors: Dict[str, List[ValidationError]] = field(default_factory=dict)
    duplicate_ids: List[str] = field(default_factory=list)
    category_errors: List[str] = field(default_factory=list)


class SkillsValidator:
    """Validates YAML files in the OpenModels Skills registry"""

    def __init__(self, registry_path: Optional[Path] = None):
        self.registry_path = registry_path or Path(__file__).parent
        self.schemas_path = self.registry_path / 'schemas'

        # Load JSON schemas
        self.skill_schema = self._load_schema('skill.schema.json')
        self.category_schema = self._load_schema('category.schema.json')

        # Create validators
        self.skill_validator = Draft7Validator(self.skill_schema)
        self.category_validator = Draft7Validator(self.category_schema)

        # Load valid categories
        self.valid_categories = self._load_valid_categories()

    def _load_schema(self, schema_filename: str) -> Dict[str, Any]:
        """Load a JSON schema from file"""
        schema_path = self.schemas_path / schema_filename
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema not found: {schema_path}")

        with open(schema_path, 'r') as f:
            return json.load(f)

    def _load_valid_categories(self) -> set:
        """Load valid category IDs from categories.yaml"""
        categories_file = self.registry_path / 'categories' / 'categories.yaml'
        if not categories_file.exists():
            return set()

        with open(categories_file, 'r') as f:
            data = yaml.safe_load(f)

        if data and 'categories' in data:
            return {cat['id'] for cat in data['categories']}
        return set()

    def check_yaml_syntax(self, file_path: Path) -> bool:
        """Check if a YAML file has valid syntax"""
        try:
            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            return True
        except yaml.YAMLError as e:
            print(f"  YAML syntax error in {file_path}: {e}")
            return False
        except Exception as e:
            print(f"  Error reading {file_path}: {e}")
            return False

    def check_schema(self, file_path: Path, schema_type: str) -> ValidationResult:
        """Validate a YAML file against its JSON schema"""
        if not self.check_yaml_syntax(file_path):
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='root',
                    message='Invalid YAML syntax',
                    expected='valid YAML',
                    actual='parse error'
                )]
            )

        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='root',
                    message=str(e),
                    expected='valid YAML',
                    actual='parse error'
                )]
            )

        if schema_type == 'skill':
            validator = self.skill_validator
        elif schema_type == 'category':
            validator = self.category_validator
        else:
            raise ValueError(f"Unknown schema type: {schema_type}")

        errors = []
        for error in validator.iter_errors(data):
            field_path = '.'.join(str(p) for p in error.path) if error.path else 'root'

            expected = 'valid value'
            if error.validator == 'type':
                expected = f"type: {error.validator_value}"
            elif error.validator == 'enum':
                expected = f"one of: {', '.join(str(v) for v in error.validator_value)}"
            elif error.validator == 'required':
                missing_prop = error.message.split("'")[1] if "'" in error.message else 'unknown'
                expected = f"required field: {missing_prop}"
                field_path = missing_prop
            elif error.validator == 'pattern':
                expected = f"pattern: {error.validator_value}"
            elif error.validator in ('minimum', 'maximum', 'minLength', 'maxLength', 'minItems', 'maxItems'):
                expected = f"{error.validator}: {error.validator_value}"

            actual = 'invalid value'
            if error.instance is not None:
                if isinstance(error.instance, (dict, list)):
                    actual = f"type: {'array' if isinstance(error.instance, list) else 'object'}"
                else:
                    actual = str(error.instance)[:100]

            errors.append(ValidationError(
                field=field_path,
                message=error.message,
                expected=expected,
                actual=actual
            ))

        return ValidationResult(valid=len(errors) == 0, errors=errors)

    def check_duplicate_ids(self) -> List[str]:
        """Find duplicate skill IDs across all files"""
        duplicates = []
        skill_ids = {}

        skills_dir = self.registry_path / 'skills'
        if skills_dir.exists():
            for yaml_file in skills_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            skill_id = data['id']
                            if skill_id in skill_ids:
                                duplicates.append(
                                    f"Duplicate skill ID: {skill_id} "
                                    f"(found in {skill_ids[skill_id]} and {yaml_file})"
                                )
                            else:
                                skill_ids[skill_id] = yaml_file
                except Exception as e:
                    print(f"  Error reading {yaml_file}: {e}")

        return duplicates

    def check_filename_id_match(self) -> List[str]:
        """Verify that filename matches the id field inside"""
        errors = []
        skills_dir = self.registry_path / 'skills'
        if skills_dir.exists():
            for yaml_file in skills_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            expected_filename = f"{data['id']}.yaml"
                            if yaml_file.name != expected_filename:
                                errors.append(
                                    f"Filename mismatch: {yaml_file.name} contains id '{data['id']}' "
                                    f"(expected filename: {expected_filename})"
                                )
                except Exception:
                    pass

        return errors

    def check_related_skills_exist(self) -> List[str]:
        """Verify that related_skills reference existing skill IDs"""
        errors = []

        # Collect all skill IDs
        skill_ids = set()
        skills_dir = self.registry_path / 'skills'
        if skills_dir.exists():
            for yaml_file in skills_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            skill_ids.add(data['id'])
                except Exception:
                    pass

        # Check related_skills references
        if skills_dir.exists():
            for yaml_file in skills_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'related_skills' in data:
                            for related_id in data['related_skills']:
                                if related_id not in skill_ids:
                                    errors.append(
                                        f"Skill {yaml_file.name}: related_skills references "
                                        f"non-existent skill '{related_id}'"
                                    )
                except Exception:
                    pass

        return errors

    def validate_all(self) -> ValidationReport:
        """Validate all YAML files in the skills registry"""
        report = ValidationReport(success=True)

        # Validate categories
        categories_file = self.registry_path / 'categories' / 'categories.yaml'
        if categories_file.exists():
            report.total_files += 1
            result = self.check_schema(categories_file, 'category')
            if result.valid:
                report.valid_files += 1
            else:
                report.invalid_files += 1
                report.success = False
                report.errors[str(categories_file)] = result.errors

        # Validate skills
        skills_dir = self.registry_path / 'skills'
        if skills_dir.exists():
            for yaml_file in sorted(skills_dir.glob('*.yaml')):
                report.total_files += 1
                result = self.check_schema(yaml_file, 'skill')
                if result.valid:
                    report.valid_files += 1
                else:
                    report.invalid_files += 1
                    report.success = False
                    report.errors[str(yaml_file)] = result.errors

        # Check for duplicate IDs
        report.duplicate_ids = self.check_duplicate_ids()
        if report.duplicate_ids:
            report.success = False

        # Check filename-ID consistency
        filename_errors = self.check_filename_id_match()
        if filename_errors:
            report.category_errors.extend(filename_errors)
            report.success = False

        # Check related_skills references (warning only, not blocking)
        related_errors = self.check_related_skills_exist()
        if related_errors:
            report.category_errors.extend(related_errors)

        return report


def format_report(report: ValidationReport) -> str:
    """Format validation report for terminal and CI output"""
    lines = []

    if report.success:
        lines.append("✅ Validation Passed")
        lines.append(f"\n  Validated {report.total_files} files successfully.")
    else:
        lines.append("❌ Validation Failed")
        lines.append(f"\n  Summary: {report.invalid_files} of {report.total_files} files failed validation.")

        if report.errors:
            lines.append("\n  Schema Validation Errors:")
            lines.append("  " + "-" * 40)
            for file_path, errors in report.errors.items():
                lines.append(f"\n  📄 {file_path}")
                for error in errors:
                    lines.append(f"    • {error.field}: {error.message}")
                    lines.append(f"      Expected: {error.expected}")
                    lines.append(f"      Actual:   {error.actual}")

        if report.duplicate_ids:
            lines.append("\n  Duplicate ID Errors:")
            lines.append("  " + "-" * 40)
            for duplicate in report.duplicate_ids:
                lines.append(f"    • {duplicate}")

        if report.category_errors:
            lines.append("\n  Reference Errors:")
            lines.append("  " + "-" * 40)
            for error in report.category_errors:
                lines.append(f"    • {error}")

    return "\n".join(lines)


def main():
    """Main entry point"""
    print("OpenModels Skills Registry Validator")
    print("=" * 50)

    validator = SkillsValidator()

    print("Validating skills registry...")
    report = validator.validate_all()

    print("\n" + format_report(report))

    sys.exit(0 if report.success else 1)


if __name__ == '__main__':
    main()
