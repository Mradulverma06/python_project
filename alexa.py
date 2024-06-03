import speech_recognition as sr
'''understand spoken words'''
import pyttsx3
'''a text-to-speech conversion library in Python'''
import pywhatkit
import pyaudio 
import webbrowser
'''a Python library for audio input/output (I/O) operations.'''
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return ""

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        else:
            talk('Please say the command again.')

       

run_alexa() 




