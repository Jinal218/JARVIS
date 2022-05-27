import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit #pip install pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("   ")
    engine.say(audio)
    print("   ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    print("I am Jarvis Mam. Please tell me how may I help you!")
    speak("I am Jarvis Mam. Please tell me how may I help you!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        #speak("Say that again please...")
        print('Say that again please...')
        return "None"
    return query.lower()

def TaskExe():

    def Music():
        print("Tell me the name of the song!")
        speak("Tell me the name of the song!")
        musicName = takeCommand()

        if 'hold on' in musicName:
            os.startfile()
        elif 'vaste' in musicName:
            os.startfile()
        else:
            pywhatkit.playonyt(musicName)

        print("Enjoy your song Mam!")
        speak("Enjoy your song Mam!")

    def Whatsapp():
        speak("Whom do you want me to send message?")
        name = takeCommand()

        if 'Shruti' in name:
            speak("What should I message ?")
            msg = takeCommand()
            speak("Tell me the time Mam !")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+919898025928",msg,hour,min,10)
            speak("Ok Mam, sending Whatsapp message !")
        
        elif 'riya' in name:
            speak("What should I message ?")
            msg = takeCommand()
            speak("Tell me the time Mam !")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+919979786796",msg,hour,min,10)
            speak("Ok Mam, sending Whatsapp message !")

        elif 'frenny' in name:
            speak("What should I message ?")
            msg = takeCommand()
            speak("Tell me the time Mam !")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+918200016284",msg,hour,min,10)
            speak("Ok Mam, sending Whatsapp message !")

        else:
            speak("Tell me the phone number please!")
            phone = int(takeCommand())
            #ph = '+91' = phone
            speak("What should I message ?")
            msg = takeCommand()
            speak("Tell me the time Mam !")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg(phone,msg,hour,min,10)
            speak("Ok Mam, sending Whatsapp message !")

    def OpenApps():
        print("Ok Mam, wait a second!")
        speak("Ok Mam, wait a second!")

        if 'code' in query:
             codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
        
        elif 'telegram' in query:
            os.startfile("C:\\Users\\LENOVO\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/')

        print("Your command has been completed Mam!")
        speak("Your command has been completed Mam!")

    def CloseApps():
        print("Ok Mam, wait a second!")
        speak("Ok MAm, wait a second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        print("App has been closed Mam!")
        speak("App has been closed Mam!")

    while True:
        #if __name__ == "__main__":
         #wishMe()
        query = takeCommand().lower()

        if 'hello' in query:
            wishMe()

        elif 'how are you' in query:
            speak("I am fine Mam!")
            speak("What about you Mam?")

        elif 'you need a break' in query:
            print("Ok Mam, You can call me anytime !")
            speak("Ok Mam, You can call me anytime !")
            break

        elif 'bye' in query:
            speak("Ok Mam, Good Bye !")
            break

        # Logic for executing tasks based on query
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("jarvis","")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'youtube search' in query:
            speak("Ok Mam, This is what I found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.yotube.com/resulys?search_query=' + query
            webbrowser.open(web)
            speak("Done Mam!")

        elif 'google search' in query:
             query = query.replace('jarvis', '')
             search = query.replace('google search', '')
             print("Searching results on Google...")
             speak('Searching results on Google')
             pywhatkit.search(search)
             speak("Done Mam!")

        elif 'website' in query:
            speak("Ok Mam, Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched")

        elif 'launch' in query:
            speak("Tell me the name of the website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Mam!")

        elif 'facebook' in query:
            speak("Ok Mam!")
            webbrowser.open("https://www.facebook.com")
            speak("Done Mam!")

        elif 'play' in query:
            Music()

        elif 'send whatsapp message to' in query:
            query = query.replace("jarvis","")
            query = query.replace("send whatsapp message to","")
            Whatsapp()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            print(f"Mam, the time is {strTime}")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            OpenApps()

        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'close code' in query:
            CloseApps()

        elif 'close telegram' in query:
            CloseApps()

        elif 'close chrome' in query:
            CloseApps()

        elif 'close maps' in query:
            CloseApps()

        elif 'close fasebook' in query:
            CloseApps()

        elif 'close instagram' in query:
            CloseApps()

        elif 'close youtube' in query:
            CloseApps()

        elif 'my location' in query:
            webbrowser.open('https://www.google.com/maps/@23.0719488,72.5581824,12z')

        elif 'quit' in query:
            print("Quitting mam. Thank you for your time.")
            speak("Quitting mam. Thank you for your time.")
            exit()

TaskExe()
