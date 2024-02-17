import keyboard
import os
import subprocess
import time
def track():
	result = subprocess.run(['/bin/bash', 'dumpsys.sh'], stdout=subprocess.PIPE)
	print(result.stdout.decode('utf-8')) # print trackname output
def nextmedia():
    os.system("adb shell input keyevent 87")
    track()
def prevmedia():
	os.system("adb shell input keyevent 88")
	track()
def playpause():
	os.system("adb shell input keyevent 85")
	track()
keyboard.add_hotkey('ctrl+shift+g', nextmedia)
keyboard.add_hotkey('ctrl+shift+f', prevmedia)
keyboard.add_hotkey('ctrl+shift+d', playpause)
keyboard.wait('Ctrl + Q')

