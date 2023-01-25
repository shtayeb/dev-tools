import os
import shutil
from datetime import datetime, timedelta
import schedule
import time


def clean_up_folder():
    threshold_days = 2 # files older than 7 days will be deleted
    threshold_date = datetime.now() - timedelta(days=threshold_days)
    folder_path = 'generated'
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if last_modified_time < threshold_date:
                os.remove(file_path)

# schedule the clean_up_folder function to run daily at midnight
schedule.every().day.at("00:00").do(clean_up_folder)

while True:
    clean_up_folder()
    time.sleep(24 * 60 * 60) # sleep for 24 hours

