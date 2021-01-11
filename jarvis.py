import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
engine=pyttsx3.init()
engine.setProperty('rate',125)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
  listener=sr.Recognizer()
  with sr.Microphone() as source:
       listener.adjust_for_ambient_noise(source,duration=10)
       print("Listening....")
       voice=listener.listen(source)
  try:
    command=listener.recognize_google(voice)
    command.lower()
    print(command)
  except:
    print("Sorry")
  return command
def run_jarvis_initial():
    time=datetime.datetime.now().strftime("%I:%M %p")
    text="Sir how can I help you"
    if 'AM'in time:
        talk("Good morning"+text)
    else:
        talk("Good evening"+text)
def run_jarvis_operations():
    command=take_command()
    if 'play' in command:
        vedio=command.replace('play','')
        talk("Enjoy the vedio"+vedio)
        pywhatkit.playonyt(vedio)
    elif 'tell'  in command:
        if 'tell' in command:
           thing=command.replace('tell me about','')
        else:
           thing=command.replace('search for','')
        info=wikipedia.summary(thing,5)
        talk(info)
    elif 'how are you' in command:
        talk("I am absolutely fine Sir,thanks for asking")
    elif 'bye' in command:
        talk("It always being a pleasure working with you Sir")
        exit(0)
    elif 'thank you' in command:
        talk("Anything else Sir")
    else:
        talk("Sorry Sir didn't understand it")
run_jarvis_initial()
while True:
   run_jarvis_operations()
