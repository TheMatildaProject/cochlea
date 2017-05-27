import speech_recognition as sr

print('ready');

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        print ('Hey I heard something')