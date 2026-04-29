from structorex.core.filter import FileFilter


def test_file_filter_allowed_extensions():
    filter_obj = FileFilter(
        allowed_extensions={
            ".py",
            ".txt"},
        max_file_size=1024)
    assert filter_obj.is_text_file("test.py") is True
    assert filter_obj.is_text_file("test.txt") is True
    assert filter_obj.is_text_file("test.exe") is False
    assert filter_obj.is_text_file("no_extension") is True


def test_file_filter_size_limit(tmp_path):
    filter_obj = FileFilter(
        allowed_extensions={".py"},
        max_file_size=10)  # 10 bytes max

    small_file = tmp_path / "small.py"
    small_file.write_text("hello")
    assert filter_obj.is_within_size_limit(str(small_file)) is True

    large_file = tmp_path / "large.py"
    large_file.write_text("hello world, this is a bit too large")
    assert filter_obj.is_within_size_limit(str(large_file)) is False


def test_sensitive_file_detection():
    filter_obj = FileFilter(allowed_extensions={".env"}, max_file_size=1024)
    assert filter_obj.is_sensitive_file(".env") is True
    assert filter_obj.is_sensitive_file("id_rsa") is True
    assert filter_obj.is_sensitive_file("secrets.json") is True
    assert filter_obj.is_sensitive_file("config.py") is False
