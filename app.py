import base64
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    #while True:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 1500
        audio = r.listen(source)
        b64 = base64.b64encode(audio.get_wav_data())

        file = open("testfile.txt","wb")
 
        file.write(b64) 
        file.close()