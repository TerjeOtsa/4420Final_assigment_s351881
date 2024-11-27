import logging

def setup_logging():
    logging.basicConfig(
        filename='file_organizer.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
