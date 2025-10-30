# Python File Organizer Script - Advanced Version
# Features: CLI Support, Logging, Error Handling, File Categorization by Extension


import os
import shutil
import argparse
import logging

# Logging configuration
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to organize files based on their extensions
def select_files(folder_path):
    # Error handling
    try:
        # Get all file/folder names in the given directory
        file_names = os.listdir(folder_path)

        print(f"\n Scanning folder: {folder_path}")
        organized = 0

        for files in file_names:
            full_file_path = os.path.join(folder_path, files)

            # Check if it's a file (skip folders)
            if os.path.isfile(full_file_path):
              # Get file extension
              extension = files.split('.')[-1]

              # New folder name and path
              folder_for_extension = os.path.join(folder_path,extension.upper()+ " Files")

              #  Create the folder if it does not exist
              if not os.path.exists(folder_for_extension):
                 os.makedirs(folder_for_extension)
                 print(f" Create folder: {folder_for_extension}")
                 logging.info(f"Created folder: {folder_for_extension}")

              # Move the file to the respective folder based on its extension 
              shutil.move(full_file_path, os.path.join(folder_for_extension,files))
              print(f"Moved {files} --> {folder_for_extension}")
              logging.info(f"Moved {files} --> {folder_for_extension}")
              organized +=1

        if organized == 0:
            print("No files found to organize.")
            logging.warning(f"No files found to organize.")

        else:
            print(f"{organized} file(s) organized.")
            logging.info(f"{organized} file(s) organized.")

    except Exception as e:
       print(f" Error: {str(e)}")
       logging.error(str(e))

# CLI argument parse
parser= argparse.ArgumentParser(description='Organize files in a folder by file extension.')
parser.add_argument('path' , help='Path to the folder you want to organize.')
args= parser.parse_args()

# Validate path before running
if os.path.exists(args.path):
    select_files(args.path)
else:
    print("Error: The folder path you entered does not exist.")
    logging.error(f"Invalid folder path entered by user.")