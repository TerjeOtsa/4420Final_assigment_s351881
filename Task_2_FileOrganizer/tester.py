import os
import shutil
from file_sorter import organize_files
from test_generator import create_test_folder
from config import FILE_TYPES

def setup_test_environment(base_directory, folder_name="test_x", file_count=10):
    """
    Create a clean test environment by generating a test folder with random files.
    """
    # Clean up if the folder already exists
    test_folder_path = os.path.join(base_directory, folder_name)
    if os.path.exists(test_folder_path):
        shutil.rmtree(test_folder_path)
    
    # Create a fresh test folder
    create_test_folder(base_directory, folder_name, file_count)
    return test_folder_path

def test_create_test_folder():
    """
    Test if the test folder and files are created correctly.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    folder_name = "test_create_folder"
    file_count = 5

    # Create test folder
    test_folder_path = setup_test_environment(base_dir, folder_name, file_count)

    # Check if folder exists
    assert os.path.exists(test_folder_path), "Test folder was not created."

    # Check if the correct number of files were created
    files = os.listdir(test_folder_path)
    assert len(files) == file_count, f"Expected {file_count} files, found {len(files)}."

def test_organize_files():
    """
    Test if files are organized into the correct subfolders based on their extensions.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    folder_name = "test_organizer"
    file_count = 10

    # Create test folder
    test_folder_path = setup_test_environment(base_dir, folder_name, file_count)

    # Run the file organizer
    organize_files(test_folder_path)

    # Reverse map FILE_TYPES to allow multiple extensions in the same folder
    folder_to_extensions = {}
    for ext, folder in FILE_TYPES.items():
        folder_to_extensions.setdefault(folder, []).append(ext)

    # Check if files are moved to the correct subfolders
    for folder, extensions in folder_to_extensions.items():
        subfolder_path = os.path.join(test_folder_path, folder)
        if os.path.exists(subfolder_path):
            for file_name in os.listdir(subfolder_path):
                assert any(file_name.endswith(f".{ext}") for ext in extensions), (
                    f"File {file_name} in {subfolder_path} does not match extensions {extensions}."
                )


def test_missing_directory():
    """
    Test if the organizer handles missing directories gracefully.
    """
    missing_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "missing_folder")
    try:
        organize_files(missing_dir)
        assert False, "Expected an exception for missing directory."
    except Exception as e:
        assert isinstance(e, FileNotFoundError), f"Unexpected exception type: {type(e)}"

def teardown_test_environment(base_directory, folder_name="test_x"):
    """
    Clean up test folders after testing.
    """
    test_folder_path = os.path.join(base_directory, folder_name)
    if os.path.exists(test_folder_path):
        shutil.rmtree(test_folder_path)

def test_cleanup():
    """
    Test cleanup of the test folder after testing.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    folder_name = "test_cleanup"

    # Create test folder
    test_folder_path = setup_test_environment(base_dir, folder_name, 5)

    # Remove the test folder
    teardown_test_environment(base_dir, folder_name)

    # Check if the folder was deleted
    assert not os.path.exists(test_folder_path), "Test folder was not deleted."
