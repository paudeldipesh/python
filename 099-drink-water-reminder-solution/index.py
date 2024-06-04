import os
import time

from winotify import Notification

toast = Notification(
    app_id="Dell",
    title="Drink Water Reminder",
    msg="Dipesh Sir Drink Water",
)


repeat_interval = 360

while True:
    os.system(
        "powershell -command \"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('Dipesh Sir Drink Water')\""
    )

    toast.show()

    time.sleep(repeat_interval)
