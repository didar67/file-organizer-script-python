import os
import shutil

#  Function: Organize files based on their extensions
def select_files(folder_path):
    #  Get all file/folder names in the given path
    file_names = os.listdir(folder_path)

    for f_loop in file_names:
        full_file_path = os.path.join(folder_path, f_loop)

        #  Check if it's a file (not a folder)
        if os.path.isfile(full_file_path):
            #  Get file extension (e.g., 'txt', 'pdf')
            extension = f_loop.split('.')[-1]

            #  Target folder based on extension
            folder_for_extension = os.path.join(folder_path, extension.upper() + " Files")

            #  Create folder if not exists
            if not os.path.exists(folder_for_extension):
                os.makedirs(folder_for_extension)

            #  Move file to appropriate folder
            shutil.move(full_file_path, folder_for_extension)

#  Input from user
folder = input("Enter a path: ").strip()
folder = folder.replace("\\", "/")

#  Call the function
select_files(folder)
