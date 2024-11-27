import os
import random
import string
from config import FILE_TYPES

def create_test_folder(base_directory, folder_name="test_x", file_count=10):
    """
    Create a folder in the specified base directory and populate it with files
    for testing the file organizer script.

    Parameters:
        base_directory (str): The directory where the test folder will be created.
        folder_name (str): Name of the test folder to create.
        file_count (int): Number of test files to generate.
    """
    # Ensure the base directory exists
    if not os.path.exists(base_directory):
        print(f"Base directory '{base_directory}' does not exist.")
        return

    # Create the test folder
    test_folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(test_folder_path, exist_ok=True)
    print(f"Created test folder: {test_folder_path}")

    # Generate random files
    extensions = list(FILE_TYPES.keys())
    for _ in range(file_count):
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        file_extension = random.choice(extensions)
        file_path = os.path.join(test_folder_path, f"{file_name}.{file_extension}")

        # Create an empty file with the chosen name and extension
        with open(file_path, "w") as file:
            file.write("")  # Empty content
        print(f"Created file: {file_path}")

    print(f"Test files created in {test_folder_path}")

if __name__ == "__main__":
    # Define the absolute path to Task_2_FileOrganizer directory
    base_dir = os.path.abspath(os.path.dirname(__file__))
    folder_name = input("Enter the name of the test folder (default 'test_x'): ").strip() or "test_x"
    file_count = int(input("Enter the number of test files to create: ").strip() or 10)

    # Run the test folder creation
    create_test_folder(base_dir, folder_name, file_count)
