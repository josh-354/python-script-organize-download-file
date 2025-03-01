import os
from pathlib import Path

file_types = {
    'IMAGES': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.svg', '.heif', '.psd'],
    'AUDIO': ['.aac', '.aa', '.dvf', '.m4a', '.m4b', '.m4p', '.mp3', '.msv', '.raw', '.wav', '.wma'],
    'VIDEOS': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
    'DOCUMENTS': ['.doc', '.docx', '.ppt', '.pdf', '.csv','.xlsx'],
    'EXE':['.exe']
}

# Map file extensions to their respective folders
dct = {ext: category for category, extensions in file_types.items() for ext in extensions}

def get_unique_filename(directory, filename):
    """Generates a unique filename if the file already exists in the directory."""
    file_path = directory / filename
    if not file_path.exists():
        return file_path  # Return original filename if it doesn't exist

    stem, suffix = file_path.stem, file_path.suffix
    counter = 1
    while file_path.exists():
        file_path = directory / f"{stem}_{counter}{suffix}"
        counter += 1

    return file_path

def file_organizer(target_folder):
    """Organizes files inside the specified folder."""
    
    target_path = Path(target_folder)
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"❌ Error: '{target_folder}' is not a valid folder.")
        return

    for entry in target_path.iterdir():
        if entry.is_dir():
            continue  # Skip directories

        file_path = Path(entry)
        file_format = file_path.suffix.lower()

        # Skip system files
        if file_path.name in ['NTUSER.DAT', 'Thumbs.db', 'desktop.ini']:
            continue

        # Determine the target directory
        directory_name = dct.get(file_format, 'OTHERS')
        directory_path = target_path / directory_name

        # Create the directory only if it doesn't already exist
        directory_path.mkdir(exist_ok=True)

        # Get a unique filename if it already exists in the target directory
        new_file_path = get_unique_filename(directory_path, file_path.name)

        try:
            file_path.rename(new_file_path)
            print(f"✅ Moved: {file_path.name} → {new_file_path}")
        except PermissionError:
            print(f"🚫 Skipping {file_path} (File in use)")

if __name__ == '__main__':
    folder_to_organize = "D:\DOWNLOADS"  # Change this to the folder you want to organize
    file_organizer(folder_to_organize)
