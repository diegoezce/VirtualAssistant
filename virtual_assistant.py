import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


#listen microphone and return text
def audio2text():
    # store recognizer in a variable
    r = sr.Recognizer()

    #config microphone
    with sr.Microphone() as origin:

        r.pause_threshold = 0.8

        #recording started
        print('You can talk now....')

        # save in a varialbe
        audio = r.listen(origin)

        try:
            #google search
            request = r.recognize_google(audio, language='es-ar')

            #test that it could do it
            print("You said: " + request)

            return request
        
        except sr.UnknownValueError:
            print("couldn't understand....")

            return 'keep waiting...'

        except sr.RequestError:

            print("something went wrong....")

            return 'keep waiting...'


audio2text()
