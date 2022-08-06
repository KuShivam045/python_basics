import time
import os
import playsound

alarm_time = '14:36'
if time.asctime()[11:-8] == alarm_time :
    absolute_path = os.startfile("C:\\Users\\Shivaay\\Desktop\\Python Basics\\O Jaanwaale.mp3")
    print(absolute_path)
    playsound.playsound(absolute_path)