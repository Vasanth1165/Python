import pyttsx3
import wikipedia
def speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    voice=engine.getProperty("voices")
    engine.setProperty("voice",voice[0].id)
    engine.setProperty("rate",140)
    engine.runAndWait()
speak(wikipedia.summary(input()))

