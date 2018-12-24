#!/usr/bin/python3
#
# pip3 install schedule
#
# https://github.com/dbader/schedule
#

import schedule
import datetime
import time

def job():
    print("I'm working...")
    print(datetime.datetime.now())

schedule.every(5).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
