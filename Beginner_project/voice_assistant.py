import pyttsx3
import datetime
import speech_recognition as sr 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voices",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am lim sir . please tell me how may i help you")

def takeCommand():
    """its takes microphone input from the user and returns string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = "en-in")
        print(f"user said : {query} \n ")
    
    except Exception as e:
         #print(e)
         print("say that again please ...")
         return "None"
    return query



if __name__ == "__main__":
    wishMe()
    takeCommand()
