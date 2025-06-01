import os

def rename_files(folder_path, prefix):
    # Get all file names from the folder
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        print(" Folder path not found!")
        return

    # Rename each file with the new prefix and numbering
    for index, old_name in enumerate(files):
        file_extension = os.path.splitext(old_name)[1]  # Extract file extension (e.g., .txt, .jpg)
        new_name = f"{prefix}_{index + 1}{file_extension}"

        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f" Renamed: {old_name} → {new_name}")

# User Input
folder = input("Enter an folder path: ").strip().replace("\\", "/")
prefix = input("Enter the prefix for new filenames: ").strip()

# Call the function
rename_files(folder, prefix)

