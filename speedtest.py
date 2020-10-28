import speedtest
import datetime
import time

s = speedtest.Speedtest()

while True:
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048676), 2)
    print('time :', time_now, 'downspeed :', downspeed, 'up speed :', upspeed)

    time.sleep(60)
