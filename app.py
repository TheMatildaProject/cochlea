import base64
import json
import requests
import speech_recognition as sr
import sys

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 1500
        audio = r.listen(source)
        b64 = base64.b64encode(audio.get_wav_data())
        
        payload = {
            "action": "command",
            "parameters": {
                "audio": "{0}".format(b64.decode())
            }
        } # byte to string as json is prep

        rq = requests.post(sys.argv[1], json=payload);
        
        print('I heard something!')