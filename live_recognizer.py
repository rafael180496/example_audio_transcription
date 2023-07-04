import speech_recognition as sr
import sys

duration = int(sys.argv[1])

r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)