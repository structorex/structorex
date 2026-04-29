import os
import pytest
from structorex.config import Config
from structorex.core.filter import FileFilter
from structorex.core.builder import ProjectBuilder

def test_builder_initialization():
    config = Config()
    file_filter = FileFilter(config.allowed_extensions, config.max_file_size)
    builder = ProjectBuilder(config, file_filter)
    
    assert builder.config == config
    assert builder.file_filter == file_filter
