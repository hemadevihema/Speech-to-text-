import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"you said:{text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio")


