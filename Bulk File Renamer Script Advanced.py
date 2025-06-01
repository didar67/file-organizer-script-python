import os
import shutil
import logging
import argparse
from datetime import datetime

# Logging Setup
log_filename = f"organizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Main Function
def organize_files_by_extension(folder_path):
    try:
        if not os.path.isdir(folder_path):
            logging.error(f"Provided path is not a directory: {folder_path}")
            print(" The path you provided is not a valid directory.")
            return

        files = os.listdir(folder_path)
        if not files:
            print(" The folder is empty.")
            return

        for file_name in files:
            full_file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(full_file_path):
                extension = file_name.split('.')[-1].lower()
                if extension == file_name:  # No extension
                    extension = "no_extension"

                target_folder = os.path.join(folder_path, f"{extension.upper()}_Files")

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                    logging.info(f"Created folder: {target_folder}")

                shutil.move(full_file_path, target_folder)
                logging.info(f"Moved: {file_name} → {target_folder}")
        
        print(" Files have been organized by extension.")
    except Exception as e:
        logging.exception("An error occurred while organizing files.")
        print(f" Error: {e}")

# CLI Setup
def main():
    parser = argparse.ArgumentParser(description="Bulk File Organizer Script")
    parser.add_argument("path", help="Path to the folder you want to organize")
    args = parser.parse_args()

    organize_files_by_extension(args.path)

# Run the Script
if __name__ == "__main__":
    main()
