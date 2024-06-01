import win32com.client as wincom

names = ["Dipesh", "Dinesh", "Rajesh", "Ram"]
speak = wincom.Dispatch("SAPI.SpVoice")
for name in names:
    speak.Speak(f"Shoutout to {name}")
