import shutil
from pathlib import Path

FOLDERS = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"},
    "Videos": {".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"},
    "Music": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
    "Documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"},
    "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
    "Executables": {".exe"},
}

EXT_TO_FOLDER = {ext: folder for folder, exts in FOLDERS.items() for ext in exts}

def organize_folder(folder_path):
    # Create folders if they don't exist
    for folder in FOLDERS:
        (folder_path / folder).mkdir(exist_ok=True)
    # Organize files
    for item in folder_path.iterdir():
        if item.is_file():
            target_folder = EXT_TO_FOLDER.get(item.suffix.lower())
            if target_folder:
                dest = folder_path / target_folder / item.name
                shutil.move(str(item), str(dest))
            else:
                print(f"Skipped: {item.name}")

def organize_downloads_and_desktop():
    desktop = Path.home() / "Desktop"
    downloads = Path.home() / "Downloads"
    print("Organizing Downloads...")
    organize_folder(downloads)
    print("Organizing Desktop...")
    organize_folder(desktop)
    print("✅ Downloads and Desktop organized successfully!")

if __name__ == "__main__":
    organize_downloads_and_desktop()
