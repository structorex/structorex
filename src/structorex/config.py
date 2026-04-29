import argparse
import json
import os
import sys
from pathlib import Path
import logging

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

try:
    if sys.version_info >= (3, 11):
        import tomllib as toml
    else:
        import tomli as toml
    HAS_TOML = True
except ImportError:
    HAS_TOML = False

logger = logging.getLogger(__name__)


DEFAULT_ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".kt", ".scala", ".go", ".rs", ".c", ".cpp", ".h", ".cs", ".rb", ".php", ".swift", ".dart", ".lua", ".sh", ".bash", ".ps1", ".sql",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env", ".xml", ".html", ".htm", ".css", ".scss", ".less", ".md", ".rst", ".txt", ".log", ".gitignore", ".dockerignore",
    "makefile", "dockerfile", "vagrantfile", "jenkinsfile", "cmakelists.txt"
}

DEFAULT_EXCLUDED_DIRS = {
    ".git", "__pycache__", ".idea", "venv", ".venv", "node_modules", ".vscode", "dist", "build", ".tox", ".pytest_cache"
}

class Config:
    def __init__(self):
        self.root_path = "."
        self.output_file = "project_report.txt"
        self.output_format = "text"
        self.allowed_extensions = set(DEFAULT_ALLOWED_EXTENSIONS)
        self.excluded_dirs = set(DEFAULT_EXCLUDED_DIRS)
        self.max_file_size = 10 * 1024 * 1024  # 10 MB
        self.verbose = False
        self.show_skipped = False
        self.export_zip = None

    def load_from_file(self, root_path: str):
        """Loads configuration from project files if they exist."""
        # Check pyproject.toml
        toml_path = os.path.join(root_path, "pyproject.toml")
        if HAS_TOML and os.path.exists(toml_path):
            try:
                with open(toml_path, "rb") as f:
                    data = toml.load(f)
                    if "tool" in data and "structorex" in data["tool"]:
                        self._apply_dict(data["tool"]["structorex"])
                        logger.debug("Loaded config from pyproject.toml")
            except Exception as e:
                logger.warning(f"Error reading pyproject.toml: {e}")

        # Check .structorex.yaml
        yaml_path = os.path.join(root_path, ".structorex.yaml")
        if HAS_YAML and os.path.exists(yaml_path):
            try:
                with open(yaml_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if data:
                        self._apply_dict(data)
                        logger.debug("Loaded config from .structorex.yaml")
            except Exception as e:
                logger.warning(f"Error reading .structorex.yaml: {e}")

        # Check .structorex.json
        json_path = os.path.join(root_path, ".structorex.json")
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if data:
                        self._apply_dict(data)
                        logger.debug("Loaded config from .structorex.json")
            except Exception as e:
                logger.warning(f"Error reading .structorex.json: {e}")

    def _apply_dict(self, data: dict):
        if "output" in data:
            self.output_file = data["output"]
        if "format" in data:
            self.output_format = data["format"]
        if "exclude" in data:
            self.excluded_dirs.update(data["exclude"])
        if "allowed" in data:
            self.allowed_extensions = set(data["allowed"])
        if "max_size" in data:
            self.max_file_size = data["max_size"] * 1024 * 1024
        if "show_skipped" in data:
            self.show_skipped = bool(data["show_skipped"])

    @classmethod
    def from_args(cls, args):
        config = cls()
        config.root_path = args.path
        
        # Load from file first, then override with args
        config.load_from_file(config.root_path)

        if args.output != "project_report.txt" or not hasattr(config, "output_file"):
            config.output_file = args.output
        if args.format != "text" or not hasattr(config, "output_format"):
            config.output_format = args.format
        if args.exclude:
            config.excluded_dirs.update(args.exclude)
        if args.allowed:
            config.allowed_extensions = set(args.allowed)
        if args.max_size != 10:
            config.max_file_size = args.max_size * 1024 * 1024
        config.verbose = args.verbose
        if args.show_skipped:
            config.show_skipped = args.show_skipped
        if args.export_zip:
            config.export_zip = args.export_zip
        return config

    @classmethod
    def parse_cli(cls):
        parser = argparse.ArgumentParser(description="Structorex: Project structure and content generator.")
        parser.add_argument("path", nargs="?", default=".", help="Path to the root directory (default: current directory)")
        parser.add_argument("-o", "--output", default="project_report.txt", help="Output file name")
        parser.add_argument("-f", "--format", choices=["text", "json", "markdown", "html"], default="text", help="Output format")
        parser.add_argument("-e", "--exclude", nargs="*", help="Additional directories to exclude")
        parser.add_argument("-a", "--allowed", nargs="*", help="Override allowed file extensions (e.g. .py .txt)")
        parser.add_argument("-m", "--max-size", type=int, default=10, help="Maximum file size in MB to read content")
        parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
        parser.add_argument("-s", "--show-skipped", action="store_true", help="Show skipped files in the report")
        parser.add_argument("-z", "--export-zip", help="Create a ZIP archive of the filtered project files")
        
        args = parser.parse_args()
        return cls.from_args(args)
