from pathlib import Path
import shutil
from datetime import datetime
import logging
import time

logging.basicConfig(
    filename='backup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def make_backup(input_source):

    source = Path(input_source)

    if not source.exists():
        error_msg = "The Directory does not exist!"
        print(error_msg)
        logging.error(error_msg)
        return
    
    if not source.is_dir():
        error_msg = "The source is not a directory!"
        print(error_msg)
        logging.error(error_msg)
        return
    
    backup_root = Path.cwd() / "Backup"
    backup_root.mkdir(exist_ok=True)

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d_%H-%M-%S")

    dest = backup_root / f"{source.name}_{formatted_date}"

    try:
        logging.info(f"Starting backup of: {source}")
        shutil.copytree(source, dest)

        success_msg = f"Backup completed successfully: {dest.name}"
        print(success_msg)
        logging.info(success_msg)

    except Exception as e:
        error_msg = f"Backup failed for {source.name}. Error: {str(e)}"
        logging.error(error_msg)
        print(error_msg)

def automated_backup():
    source_folder = "C:\Users\zenab\OneDrive\Random"
    while True:
        print("Checking for backup time...")
        make_backup(source_folder)
        
        print("Backup done. Sleeping for 24 hours.")
        time.sleep(86400)

if __name__ == "__main__":
    automated_backup()
