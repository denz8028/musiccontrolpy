adb shell 'dumpsys media_session | grep metadata' | grep -v 'size=0'
