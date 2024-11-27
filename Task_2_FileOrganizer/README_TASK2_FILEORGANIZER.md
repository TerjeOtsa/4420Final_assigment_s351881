# Task 2: File Organizer

## Project Overview

The **File Organizer** is a Python-based tool designed to automate the organization of files in a directory. It dynamically categorizes files by their extensions, placing them into appropriate subfolders based on predefined rules. This project demonstrates modular programming, metaprogramming, file handling, error handling, and testing with `pytest`.

---

## Features

1. **File Handling**:
   - Automatically traverses a directory and moves files into categorized subfolders.
   - Creates new subfolders dynamically when necessary.

2. **Dynamic Configuration**:
   - Supports adding new file types and categories without modifying the core logic.

3. **Error Handling**:
   - Handles missing directories, permission errors, and other runtime exceptions gracefully.

4. **Regular Expressions**:
   - Uses regex to identify file extensions for robust categorization.

5. **Logging**:
   - Maintains a log file to track operations and errors.

6. **Testing**:
   - Fully tested using `pytest`, covering edge cases and verifying functionality.

7. **Test File Generator**:
   - Includes a script to generate a test environment with random files for easy testing.

---

## Requirements

### System Requirements
- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux

### Python Libraries
Install the required libraries with:
```bash
pip install -r requirements.txt


Task_2_FileOrganizer/
│
├── config.py               # Configuration for file type mappings
├── file_sorter.py          # Core logic for organizing files
├── logger.py               # Logging configuration
├── main.py                 # Entry point to run the file organizer
├── test_generator.py       # Script to generate test environments
├── tester.py               # Unit tests for the project
├── file_organizer.log      # Log file (auto-created during execution)
└── __pycache__/            # Compiled Python files (auto-generated)


config.py

FILE_TYPES = {
    "txt": "Text Files",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "docx": "Documents",
    "xlsx": "Spreadsheets",
    "csv": "Data Files",
}

FILE_TYPES["extension"] = "Category Name"

To organize files use python main.py 
You will then be prompted to write which directory to organize
The script will then create sub folders fitting of the different file types


GENERATING TEST FILES 
Python test_generator.py 

enter name of new folder for testing and how many random files to fill it with

RUNNING TESTS 

python -m pytest tester.py

will check through a set of tests made for this Task

alll files organized will be logged to the file_organizer.log