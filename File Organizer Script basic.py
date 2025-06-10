# Python File Organizer Script - Organize files by extension


import os
import shutil

# Function to organize files based on their extensions
def select_files(folder_path):
    # Get all file/folder names in the given directory
    file_names = os.listdir(folder_path)

    print(f"\n Scanning folder: {folder_path}")
    organized = 0

    for files in file_names:
        full_file_path = os.path.join(folder_path, files)

        # Check if it's a file or folder
        if os.path.isfile(full_file_path):
            # Get file extension
            extension = files.split('.')[-1]

            # New folder name and path
            folder_for_extension = os.path.join(folder_path,extension.upper()+ " Files")

            #  Create the folder if it does not exist
            if not os.path.exists(folder_for_extension):
                os.makedirs(folder_for_extension)
                print(f" Create folder: {folder_for_extension}")

            # Move the file 
            shutil.move(full_file_path, os.path.join(folder_for_extension,files))
            print(f" File Moved from {files} --> {folder_for_extension}")
            organized +=1

    if organized == 0:
        print("No files found to organize.")
    else:
        print(f"{organized} file(s) organized.")

# Take folder path input from the user
folder = input("Enter a folder path you want to organize: ").strip()
folder = folder.replace("\\","/")

# Validate path before running
if os.path.exists(folder):
    select_files(folder)
else:
    print("Error: The folder path you entered does not exist. Please enter a valid path.")