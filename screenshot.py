#Automate Screen Shot Clean-Up

import os
import datetime as dt
import shutil
# Define constant path
DESKTOP = '/~/Desktop/'
TRASH = '/~/.Trash'
# Expiration time in seconds (How long to wait from file creation to move to trash)
EXP_TIME_SEC = 86400.00 

now = dt.datetime.now()
now_utc = now.timestamp() # Current timestamp in UTC format (seconds)
desktopFiles = os.listdir(path=DESKTOP)

for file in desktopFiles:
    file_os_stat = os.stat(DESKTOP + file)
    file_ctime = file_os_stat.st_ctime
    elapse = now_utc - file_ctime  # Time elapsed since file was created in UTC format (seconds)

    # Check if file name starts with 'Screen' and ends with 'png'
    if file[0:6] == 'Screen' and file[-3:] == 'png':
        if elapse >= EXP_TIME_SEC:
            shutil.move(DESKTOP + file, TRASH)

