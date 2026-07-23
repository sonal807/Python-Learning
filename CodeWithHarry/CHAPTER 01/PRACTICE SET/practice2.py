# pyttsx3 is an offline text-to-speech (TTS) conversion library for Python.
# Unlike cloud-based alternatives, it functions entirely without an internet connection.
# . Unlike cloud-based alternatives, it functions entirely without an internet connection. It achieves this by hooking directly into your operating system's native speech synthesis engine. 

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello My name is Sonal Rai")
engine.runAndWait()