"""
Site blocker for Linux
You will be needed to use Cron Job Scheduler:
    sudo crontab -e 
    add:
        <@reboot python3> <the path to the main file>
"""


import time
import os
from datetime import datetime as dt


host_path = "/etc/hosts"

redirect = '127.0.0.1'
website_list = ['www.chartable.com', 'www.steamcommunity.com/market/']


while True:
    # if these are the working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('What are you doing here, huh???')
        file = open(host_path, 'r+')
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + ' ' + website + '\n')

    else:
        print('Ok, here.')
        file = open(host_path, 'r+')
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
    time.sleep(5)
