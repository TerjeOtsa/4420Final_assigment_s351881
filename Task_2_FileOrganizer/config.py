FILE_TYPES = {
    "txt": "Text Files",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "docx": "Documents",
    "mp3": "Music",
    "mp4": "Videos",
    "csv": "Data Files",
    "xlsx": "Spreadsheets",
}

def add_file_type(extension, folder):
    FILE_TYPES[extension.lower()] = folder
