#!/usr/bin/python3
#
#

import time
import datetime

starttime=time.time()
print(starttime)
while True:
  print ("tick")
  print(datetime.datetime.now())
  # wait 60s
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
