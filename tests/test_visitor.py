from structorex.core.visitor import ProjectStructureVisitor
from structorex.core.filter import FileFilter
from structorex.core.components import FileComponent, DirectoryComponent


def test_visitor_visit_file(tmp_path):
    filter_obj = FileFilter(allowed_extensions={".py"}, max_file_size=1024)
    visitor = ProjectStructureVisitor(filter_obj)

    test_file = tmp_path / "test.py"
    test_file.write_text("print('hello')")

    file_node = FileComponent(str(test_file))

    visitor.visit_file(file_node, prefix="├── ", is_last=False)

    # Needs processing for queued files
    visitor.process_queued_files()

    assert len(visitor.structure) == 1
    assert "test.py" in visitor.structure[0]
    assert visitor.total_files == 1
    assert visitor.total_lines == 1
    assert str(test_file) in visitor.content_dict
    assert visitor.content_dict[str(test_file)] == "print('hello')"


def test_visitor_visit_directory(tmp_path):
    filter_obj = FileFilter(allowed_extensions={".py"}, max_file_size=1024)
    visitor = ProjectStructureVisitor(filter_obj)

    test_dir = tmp_path / "src"
    test_dir.mkdir()

    dir_node = DirectoryComponent(str(test_dir))

    visitor.visit_directory(dir_node, prefix="└── ", is_last=True)

    assert len(visitor.structure) == 1
    assert "src/" in visitor.structure[0]
    assert visitor.total_files == 0
