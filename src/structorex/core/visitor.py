import logging
import os
import concurrent.futures

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

try:
    from charset_normalizer import from_path
    HAS_CHARSET_NORMALIZER = True
except ImportError:
    HAS_CHARSET_NORMALIZER = False

logger = logging.getLogger(__name__)

def read_single_file(file_path):
    try:
        if HAS_CHARSET_NORMALIZER:
            results = from_path(file_path)
            best_match = results.best()
            if best_match:
                content = str(best_match)
                return file_path, content, content.count("\n") + 1, None
        
        # Fallback if charset_normalizer is not installed or returns no match
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            return file_path, content, content.count("\n") + 1, None
    except Exception as e:
        return file_path, None, 0, str(e)


class FileSystemVisitor:
    def visit_file(self, file, prefix, is_last):
        raise NotImplementedError

    def visit_directory(self, directory, prefix, is_last):
        raise NotImplementedError

class ProjectStructureVisitor(FileSystemVisitor):
    def __init__(self, filter_obj):
        self.structure = []
        self.content_dict = {}
        self.filter = filter_obj
        self.total_lines = 0
        self.total_files = 0
        self._files_to_read = []
        self.structure_data = []

    def visit_file(self, file, prefix, is_last):
        connector = "└── " if is_last else "├── "
        
        if getattr(file, "skipped", False):
            self.structure.append(f"{prefix}{connector}{file.name} [skipped]")
            self.structure_data.append({"type": "skipped", "name": file.name, "path": file.path, "prefix": prefix, "connector": connector})
            return

        self.structure.append(f"{prefix}{connector}{file.name}")
        self.structure_data.append({"type": "file", "name": file.name, "path": file.path, "prefix": prefix, "connector": connector})
        self.total_files += 1

        if not self.filter.is_within_size_limit(file.path):
            self.content_dict[file.path] = f"[SKIPPED: File too large]"
            return
            
        if not self.filter.is_text_file(file.path):
            self.content_dict[file.path] = f"[SKIPPED: Binary file]"
            return

        self._files_to_read.append(file.path)

    def visit_directory(self, directory, prefix, is_last):
        connector = "└── " if is_last else "├── "
        self.structure.append(f"{prefix}{connector}{directory.name}/")
        self.structure_data.append({"type": "dir", "name": directory.name, "path": directory.path, "prefix": prefix, "connector": connector})

    def process_queued_files(self, verbose=False):
        if not self._files_to_read:
            return

        disable_tqdm = not HAS_TQDM or verbose
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_path = {executor.submit(read_single_file, path): path for path in self._files_to_read}
            
            iterator = concurrent.futures.as_completed(future_to_path)
            if HAS_TQDM and not disable_tqdm:
                iterator = tqdm(iterator, total=len(self._files_to_read), desc="Reading files", unit="file")
                
            for future in iterator:
                path, content, lines, error = future.result()
                if error:
                    self.content_dict[path] = f"[ERROR: {error}]"
                else:
                    self.content_dict[path] = content
                    self.total_lines += lines
