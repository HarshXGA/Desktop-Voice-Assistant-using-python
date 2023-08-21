import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd(want_to_stop):
    text=""
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything ... ')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message :',format(text))

    except Exception as ex:
        print(ex)

    if 'chrome' in text:
        a='Opening chrome...'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    elif 'play' in text:
        a='Opening youtube...'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        b='Opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    elif 'exit' or 'quit' or 'end' in text:
        return True
    
    return False
        
while True:
    if cmd(): 
        print("Need to exit")
        break


