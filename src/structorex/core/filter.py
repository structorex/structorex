import mimetypes
import os

class FileFilter:
    def __init__(self, allowed_extensions, max_file_size):
        self.allowed_extensions = allowed_extensions
        self.max_file_size = max_file_size
        self.sensitive_files = {".env", "id_rsa", "id_ed25519", "secrets.yml", "secrets.json"}
        self.sensitive_extensions = {".pem", ".key", ".p12", ".keystore", ".jks", ".pkcs12", ".pfx"}

    def is_allowed_extension(self, filename: str) -> bool:
        ext = os.path.splitext(filename)[1].lower()
        if ext in self.allowed_extensions:
            return True
        # Check if the whole filename is allowed (e.g., Dockerfile)
        if filename.lower() in self.allowed_extensions:
            return True
        return False

    def is_text_file(self, filepath: str) -> bool:
        mime, _ = mimetypes.guess_type(filepath)
        return mime is None or mime.startswith("text/") or mime in ("application/json", "application/xml")

    def is_within_size_limit(self, filepath: str) -> bool:
        try:
            return os.path.getsize(filepath) <= self.max_file_size
        except OSError:
            return True

    def is_sensitive_file(self, filename: str) -> bool:
        if filename.lower() in self.sensitive_files:
            return True
        ext = os.path.splitext(filename)[1].lower()
        if ext in self.sensitive_extensions:
            return True
        if filename.startswith("secret") or filename.endswith("secret"):
            return True
        return False

    def should_process_file(self, filepath: str) -> bool:
        filename = os.path.basename(filepath)
        if self.is_sensitive_file(filename):
            return False
        if not self.is_allowed_extension(filename):
            return False
        return True
