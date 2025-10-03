import logging
import time
import os

def write_logs_every_3_seconds():
    log_dir = '/app/logs'
    os.makedirs(log_dir, exist_ok=True)  # Create directory if it doesn't exist
    log_file = os.path.join(log_dir, 'file_name.log')

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create file handler using 'with' for opening the file safely during setup
    with open(log_file, 'a'):
        pass  # Just to ensure file is created

    # Create a file handler for the logger
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        while True:
            logger.info("This is a log message written every 3 seconds.")
            time.sleep(3)
    except KeyboardInterrupt:
        print("Logging stopped by user.")

if __name__ == "__main__":
    write_logs_every_3_seconds()

