import os
import pytest
from structorex.config import Config

def test_config_defaults():
    config = Config()
    assert config.output_file == "project_report.txt"
    assert config.output_format == "text"
    assert config.excluded_dirs == {"node_modules", ".git", ".venv", "venv", "__pycache__", ".idea", ".vscode", "dist", "build", ".pytest_cache", ".tox"}
    assert ".py" in config.allowed_extensions
    assert config.max_file_size == 10 * 1024 * 1024

def test_config_load_from_yaml(tmp_path):
    yaml_file = tmp_path / ".structorex.yaml"
    yaml_file.write_text("""
format: markdown
output: custom.md
exclude:
  - tests
max_size: 5
""")
    
    config = Config()
    config.load_from_file(str(tmp_path))
    
    assert config.output_format == "markdown"
    assert config.output_file == "custom.md"
    assert "tests" in config.excluded_dirs
    assert config.max_file_size == 5 * 1024 * 1024

def test_config_load_from_toml(tmp_path):
    toml_file = tmp_path / "pyproject.toml"
    toml_file.write_text("""
[tool.structorex]
format = "json"
output = "analysis.json"
""")
    
    config = Config()
    config.load_from_file(str(tmp_path))
    
    assert config.output_format == "json"
    assert config.output_file == "analysis.json"
