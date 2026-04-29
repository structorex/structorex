import os
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    @abstractmethod
    def accept(self, visitor, prefix="", is_last=True):
        pass

class FileComponent(FileSystemComponent):
    def __init__(self, path):
        super().__init__(path)
        self.skipped = False

    def accept(self, visitor, prefix="", is_last=True):
        visitor.visit_file(self, prefix, is_last)

class DirectoryComponent(FileSystemComponent):
    def __init__(self, path):
        super().__init__(path)
        self.children = []

    def add_child(self, component):
        self.children.append(component)

    def accept(self, visitor, prefix="", is_last=True):
        visitor.visit_directory(self, prefix, is_last)
        for i, child in enumerate(self.children):
            child.accept(
                visitor,
                prefix + ("    " if is_last else "│   "),
                i == len(self.children) - 1,
            )
