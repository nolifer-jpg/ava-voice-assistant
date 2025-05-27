import speech_recognition as sr

r=sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        print("Say something!")
        audio = r.listen(source) 
    try:
        text = r.recognize_google(audio)
        return text.lower()   
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech recognition service unavailable."

