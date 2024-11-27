import os
import shutil
import re
from config import FILE_TYPES, add_file_type
import logging

def organize_files(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            file_extension = re.search(r'\.([a-zA-Z0-9]+)$', file_name)
            if not file_extension:
                logging.warning(f"Skipping unknown file type: {file_name}")
                continue

            file_extension = file_extension.group(1).lower()
            destination_folder = FILE_TYPES.get(file_extension, "Others")

            destination_path = os.path.join(directory, destination_folder)
            os.makedirs(destination_path, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(destination_path, file_name))
                logging.info(f"Moved {file_name} to {destination_folder}/")
            except Exception as e:
                logging.error(f"Failed to move {file_name}: {str(e)}")

def add_new_file_type(extension, folder):
    add_file_type(extension, folder)
