import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


# listen microphone and return text
def audio2text():
    # store recognizer in a variable
    r = sr.Recognizer()

    # config microphone
    with sr.Microphone() as origin:
        r.pause_threshold = 0.8

        # recording started
        print('You can talk now....')

        # save in a variable
        recorded_audio = r.listen(origin)

        try:
            # Use Google Web Speech API
            request = r.recognize_google(recorded_audio, language='es-ar')

            # test that it could do it
            print("You said: " + request)

            return request

        except sr.UnknownValueError:
            print("Couldn't understand....")
            return 'keep waiting...'

        except sr.RequestError as e:
            print(f"Something went wrong: {e}")
            return 'keep waiting...'

# Function to speak a message
def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def ask_day_of_week():
    request = audio2text()
    active = 1
    response = ''
    if 'día es hoy' in request.lower() or 'día de la semana es' in request.lower():
        today = datetime.datetime.today()
        response = f'Hoy es {today.day} de {today.month} de {today.year}. Hay algo más que quisieras saber?'
        active = 1
    elif 'no gracias' in request.lower() or 'terminar' in request.lower():
        response = 'muy bien. Adiós'
        active = 0
    else:
        response = 'no entendí, repita por favor'
        active = 1

    try:
        speak(response)
        print("resp: " + response)
        return active
    except:
        speak('No entendí')
        return active


active = 1
while active == 1:
    active = ask_day_of_week()

