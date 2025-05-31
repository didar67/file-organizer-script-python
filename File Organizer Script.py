import os
import shutil

# Function: Organize files based on their extensions
def select_files(folder_path):
    # Get all file/folder names in the given path
    file_names = os.listdir(folder_path)

    print(f"\n Scanning folder: {folder_path}")
    organized = 0

    for f_loop in file_names:
        full_file_path = os.path.join(folder_path, f_loop)

        # Check if it's a file (not a folder)
        if os.path.isfile(full_file_path):
            # Get file extension
            extension = f_loop.split('.')[-1]

            # Target folder based on extension
            folder_for_extension = os.path.join(folder_path, extension.upper() + " Files")

            # Create folder if not exists
            if not os.path.exists(folder_for_extension):
                os.makedirs(folder_for_extension)
                print(f" Created folder: {folder_for_extension}")

            # Move file to appropriate folder
            shutil.move(full_file_path, os.path.join(folder_for_extension, f_loop))
            print(f" Moved: {f_loop} → {folder_for_extension}")
            organized += 1

    if organized == 0:
        print(" No files found to organize.")
    else:
        print(f"\n Done! {organized} file(s) organized successfully.")

# Input from user
folder = input(" Enter the folder path you want to organize : ").strip()
folder = folder.replace("\\", "/")

# Validate path before running
if os.path.exists(folder):
    select_files(folder)
else:
    print(" Error: The folder path you entered does not exist.")
