
import pyttsx3
user_say = input("Please enter what to say: ")
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.say(user_say)
engine.runAndWait() 




