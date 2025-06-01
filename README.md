# File Organizer Script

This is a Python script to **organize files in a folder based on their extensions**. It helps keep your folders clean by automatically moving files into subfolders like `PDF Files`, `JPG Files`, `TXT Files`, etc.

---

## Features

- Automatically detects file extensions and creates folders for each.
- Moves files into categorized folders (e.g., `.jpg` files go to `JPG Files`).
- Supports all file types — dynamic and flexible.
- Easy to use — just run and input the folder path.

---

## Requirements

- Python 3.x
- No external libraries needed (only `os` and `shutil` from Python standard library)

---

## How to Use

### 1. Clone this Repository:
```bash
git clone https://github.com/your-username/file-organizer-script.git
cd file-organizer-script
```

### 2. Run the Script:
```bash
python3 file_organizer.py
```

### 3. Input Prompt:
You will be asked to enter the folder path where files are to be organized.

Example:
```
Enter a path: /home/user/Downloads
```

After running, files will be moved like:

```
Downloads/
├── JPG Files/
│   ├── image1.jpg
│   └── photo2.jpg
├── PDF Files/
│   └── report.pdf
├── TXT Files/
│   └── notes.txt
```

---

## Example

### Before:
```
Downloads/
├── image1.jpg
├── report.pdf
├── notes.txt
```

### After:
```
Downloads/
├── JPG Files/
│   └── image1.jpg
├── PDF Files/
│   └── report.pdf
├── TXT Files/
│   └── notes.txt
```

---

##  Notes

- This script **only organizes files**, not folders.
- It does not modify the contents of any file.
- It renames/moves files permanently. Make a backup if needed.

---

## Use Cases

- Clean up your messy Downloads folder.
- Sort project files or attachments.
- Prepare data for upload or sharing.

---

## Author

**Didarul Islam**  
Python Automation & DevOps Learner  
GitHub: [your-github-link]

