import sys
from structorex.config import Config
from structorex.core.filter import FileFilter
from structorex.core.builder import ProjectBuilder
from structorex.core.visitor import ProjectStructureVisitor
from structorex.writers import get_writer
from structorex.utils import setup_logging, create_zip_snapshot

def main():
    config = Config.parse_cli()
    setup_logging(config.verbose)
    
    file_filter = FileFilter(config.allowed_extensions, config.max_file_size)
    builder = ProjectBuilder(config, file_filter)
    
    root = builder.build_tree()
    if root is None:
        print("Error: Could not build tree. Invalid path or all contents excluded.")
        sys.exit(1)
        
    visitor = ProjectStructureVisitor(file_filter)
    root.accept(visitor)
    
    visitor.process_queued_files(config.verbose)
    
    writer = get_writer(config)
    writer.write(visitor)
    
    if config.export_zip:
        create_zip_snapshot(config, visitor)

if __name__ == "__main__":
    main()
