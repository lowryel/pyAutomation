import pyttsx3, speech_recognition as sr
def getSpeech():
    recogniser = sr.Recognizer()

    with sr.Microphone() as source:
        print("Welcome Sir, please say something")
        audio = recogniser.listen(source)
        print("done")

        try:
            text = recogniser.recognize_google(audio)
            print("you said:", text)
        except Exception as e:
            print(e)
getSpeech()

