"""
Core module for File Organizer Script.

Handles:
- Scanning folders
- Categorizing files by extension
- Creating folders if missing
- Moving files
- Logging via core/logger.py
- Reading defaults from config.yaml

"""

import os
import shutil
from core.logger import get_logger
from utils.helper import load_config

logger = get_logger()

class Organizer:
    """
    Organizer class handles file organization based on extensions.
    """

    def __init__(self, folder_path: str | None = None):
        """
        Initialize the Organizer with folder path.

        Args:
            folder_path (str | None): Path to scan and organize files. If None, use default from config.
        """
        config = load_config()
        self.folder_path = folder_path or config["paths"]["default_folder"]

    def organize_files(self) -> int:
        """
        Organize files in the specified folder by their extensions.

        Returns:
            int: Number of files organized.
        """
        try:
            file_names = os.listdir(self.folder_path)
            organized_count = 0
            logger.info(f"Scanning folder: {self.folder_path}")

            for file in file_names:
                full_path = os.path.join(self.folder_path, file)

                if os.path.isfile(full_path):
                    ext = file.split('.')[-1].upper()
                    target_folder = os.path.join(self.folder_path, f"{ext} Files")

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                        logger.info(f"Created folder: {target_folder}")

                    shutil.move(full_path, os.path.join(target_folder, file))
                    logger.info(f"Moved {file} → {target_folder}")
                    organized_count += 1

            if organized_count == 0:
                logger.warning("No files found to organize.")
            else:
                logger.info(f"{organized_count} file(s) organized successfully.")

            return organized_count

        except PermissionError as pe:
            logger.error(f"Permission denied: {pe}")
            return 0
        except FileNotFoundError as fe:
            logger.error(f"Folder not found: {fe}")
            return 0
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return 0
