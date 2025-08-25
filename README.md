# 🗂️ File Organizer

A simple Python script that organizes files in a given folder by their type (images, videos, documents, etc.).  
Files are automatically moved into categorized folders. If a file with the same name already exists, a unique name will be generated to avoid overwriting.

---

## 📌 Features
- Categorizes files into predefined folders:
  - **IMAGES**, **AUDIO**, **VIDEOS**, **DOCUMENTS**, **EXE**, **ZIP**, **CODE**, **OTHERS**
- Automatically handles duplicate filenames (`file.txt`, `file_1.txt`, `file_2.txt`, etc.)
- Skips system files like `NTUSER.DAT`, `Thumbs.db`, and `desktop.ini`
- Handles file permission issues gracefully

---

## 🚀 How to Use

### 1. Clone or Download the Script
Save the script as `file_organizer.py`.

### 2. Edit the Target Folder
At the bottom of the script, change the path in:
```python
if __name__ == '__main__':
    folder_to_organize = "D:\\DOWNLOADS"  # Change this path
    file_organizer(folder_to_organize)
