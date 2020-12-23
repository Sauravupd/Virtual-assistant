import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes

engine = pyttsx3.init()
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(text):
    engine.say(text)
    engine.runAndWait()

def command_centre():  

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'saurabh' in command:
                command.replace('saurabh',"")
                print(command)
            return command
            
            
        

    except:
        pass

def assistant():
    command = command_centre()
    if 'play' in command:
        song = command.replace('play',"")
        say("playing"+song)
        print('playing',song)
        pywhatkit.playonyt(song)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        say(pyjokes.get_joke())
    
    else:
        say("i didn't get that")



while True:
    assistant()




