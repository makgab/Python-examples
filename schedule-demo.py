import schedule
import time


def job():
    print( time.strftime("%Y-%m-%d %H:%M:%S") + ": Working..." )

def job2():
    print( time.strftime("%Y-%m-%d %H:%M:%S") + ": Working2..." )



# jobs
schedule.every(1).seconds.do( job )
#schedule.every().hour.at(':00').do( job2 )
schedule.every().minutes.do( job2 )


# schedule
while 1:
    schedule.run_pending()


