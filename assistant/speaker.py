import pyttsx3

def speak(text):
    newVoiceRate = 145
    engine = pyttsx3.init()
    engine.setProperty('rate',newVoiceRate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


speak("Ava is online.")    
