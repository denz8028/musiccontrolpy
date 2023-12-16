import keyboard
import os
def nextmedia():
    os.system("adb shell input keyevent 87")
def prevmedia():
	os.system("adb shell input keyevent 88")
def playpause():
	os.system("adb shell input keyevent 85")

keyboard.add_hotkey('ctrl+shift+g', nextmedia)
keyboard.add_hotkey('ctrl+shift+f', prevmedia)
keyboard.add_hotkey('ctrl+shift+d', playpause)
keyboard.wait('Ctrl + Q')


