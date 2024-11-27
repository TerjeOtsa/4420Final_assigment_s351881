import os
import logging
from file_sorter import organize_files
from logger import setup_logging

def main():
    setup_logging()
    logging.info("Starting file organization.")
    
    directory = input("Enter the directory to organize: ").strip()
    if not os.path.exists(directory):
        logging.error(f"Directory does not exist: {directory}")
        print("Error: The specified directory does not exist.")
        return

    try:
        organize_files(directory)
        logging.info("File organization completed successfully.")
        print("File organization completed.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
