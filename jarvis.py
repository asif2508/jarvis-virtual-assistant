import pyttsx3 #python text to speech library
import datetime
import speech_recognition as sr
import wikipedia
name = "JARVIS"
engine = pyttsx3.init()
#text to speech main function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#time function
def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")#for 24 hours format and strftime("%I:%M:%S") for 12 hours format
    speak("The current time is ")
    speak(Time)
#date function
def date_():
    Day = datetime.datetime.now().day
    mon = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("Today's date is ")
    speak(Day)
    speak(mon)
    speak(year)
#wish me function
def wish_me():
    speak("Welcome back Rokeya")
    time_()
    date_()
    hour = datetime.datetime.now().hour
    if hour>6 and hour < 12:
        speak("Good morning !")
        speak("Have a good day")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon boss!")
    elif hour > 18  and hour < 20:
        speak("Good evening boss!")
    elif hour < 6 and hour >= 0:
        speak("Why didn't you sleep boss!")
        speak("It's fucking too late!")
    else:
        speak("Have a night with sweet dreams boss!")
    speak(name)
    speak("is at your service. Please tell me how can I help you")
    
def Take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = Take_command().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'who is' in query:
            speak("searching...")
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(result)
        elif 'shanu' in query:
            speak("Shanu is Asif's sister and she is also known as boots.")
        elif 'creator' in query:
            speak("Asif is my great boss! Creator of jarvis. He is smart, intelligent and kind person.")