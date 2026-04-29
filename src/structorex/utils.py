import logging
import os
import zipfile

def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(format="%(levelname)s: %(message)s", level=level)

def create_zip_snapshot(config, visitor):
    zip_path = config.export_zip
    logger = logging.getLogger(__name__)
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for node in visitor.structure_data:
                if node["type"] in ("file", "skipped"):
                    file_path = node["path"]
                    if os.path.exists(file_path):
                        # Add to zip with relative path to root_path
                        arcname = os.path.relpath(file_path, config.root_path)
                        zipf.write(file_path, arcname)
        logger.info(f"ZIP snapshot successfully saved to: {zip_path}")
    except Exception as e:
        logger.error(f"Failed to create ZIP snapshot: {e}")
