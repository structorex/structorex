import os
import logging
from .components import DirectoryComponent, FileComponent

try:
    import pathspec
    HAS_PATHSPEC = True
except ImportError:
    HAS_PATHSPEC = False

logger = logging.getLogger(__name__)

class ProjectBuilder:
    def __init__(self, config, file_filter):
        self.config = config
        self.file_filter = file_filter
        self.gitignore_spec = self._load_gitignore(config.root_path)

    def _load_gitignore(self, root_path):
        if not HAS_PATHSPEC:
            return None
        gitignore_path = os.path.join(root_path, ".gitignore")
        if os.path.exists(gitignore_path):
            try:
                with open(gitignore_path, "r", encoding="utf-8") as f:
                    return pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, f)
            except Exception as e:
                logger.warning(f"Failed to read .gitignore: {e}")
        return None

    def _is_ignored_by_gitignore(self, path):
        if not self.gitignore_spec:
            return False
        try:
            rel_path = os.path.relpath(path, self.config.root_path)
            if rel_path == ".":
                return False
            # PathSpec requires posix paths
            posix_path = rel_path.replace(os.sep, '/')
            return self.gitignore_spec.match_file(posix_path)
        except ValueError:
            return False

    def build_tree(self):
        return self._build_component(self.config.root_path)

    def _build_component(self, path):
        if not os.path.exists(path):
            return None

        if self._is_ignored_by_gitignore(path):
            return None

        if os.path.isfile(path):
            if not self.file_filter.should_process_file(path):
                return None
            return FileComponent(path)

        directory = DirectoryComponent(path)
        if directory.name in self.config.excluded_dirs:
            return None

        try:
            dirs = []
            files = []
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_dir() and entry.name not in self.config.excluded_dirs:
                        dirs.append(entry.name)
                    elif entry.is_file():
                        files.append(entry.name)

            for d in sorted(dirs):
                comp_path = os.path.join(path, d)
                child = self._build_component(comp_path)
                if child:
                    directory.add_child(child)
                    
            for f in sorted(files):
                comp_path = os.path.join(path, f)
                child = self._build_component(comp_path)
                if child or self.config.show_skipped:
                    if child is None:
                        skipped_comp = FileComponent(comp_path)
                        skipped_comp.skipped = True
                        directory.add_child(skipped_comp)
                    else:
                        directory.add_child(child)
        except PermissionError:
            logger.warning(f"Permission denied for {path}. Skipping.")
        except FileNotFoundError:
            logger.warning(f"Directory {path} no longer exists. Skipping.")
        except Exception as e:
            logger.error(f"Error processing {path}: {str(e)}")

        return directory
