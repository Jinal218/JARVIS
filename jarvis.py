import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pyaudio
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit #pip install pywhatkit
import pyautogui
import keyboard
import pyjokes
import pydictionary as pd
from playsound import playsound
from googletrans import Translator
import psutil


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
            speak(f"What should I message ?")
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

    def Screenshot():
        kk = pyautogui.screenshot()
        speak("Ok mam, what should I name the file?")
        path = takeCommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\LENOVO\\Pictures\\Screenshots\\"+ path1name
        kk.save(path1)
        os.startfile("C:\\Users\\LENOVO\\Pictures\\Screenshots")
        speak("Here is your screenschot!")

    def YoutubeAuto():
        print("Whats your command?")
        speak("Whats your command?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')
        
        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')
        
        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')
        
        elif 'fullscreen' in comm:
            keyboard.press('f')

        elif 'filmmode' in comm:
            keyboard.press('t')

        elif 'next video' in comm:
            keyboard.press_and_release('shift + n')

        elif 'previous video' in comm:
            keyboard.press_and_release('shift + p')

        elif 'decrease volume' in comm:
            keyboard.press('F2')

        elif 'increase volume' in comm:
            keyboard.press('F3')

        elif 'exit full screen' in comm:
            keyboard.press('Escape')

        speak('Done Mam');

    def ChromeAuto():
        print('Chrome automation startedd!')
        speak('Chrome automation startedd!')

        comd = takeCommand()

        if 'close this tab' in comd:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in comd:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in comd:
            keyboard.press_and_release('ctrl + n')

        elif 'open history' in comd:
            keyboard.press_and_release('ctrl + h')

        elif 'previous page' in comd:
            keyboard.press_and_release('alt + left arrow')

        elif 'next page' in comd:
            keyboard.press_and_release('alt + right arrow')

        elif 'open download page' in comd:
            keyboard.press_and_release('ctrl + j')

        speak('Done mam!')

    def Dict():
        print('Ok  mam, tell me the problem')
        speak('Ok  mam, tell me the problem')

        probl = takeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = pd.meaning(probl)
            print(f'The meaning of {probl} is {result}')
            speak(f'The meaning of {probl} is {result}')

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("synonym of","")
            result = pd.synonym(probl)
            print(f'The synonym of {probl} is {result}')
            speak(f'The synonym of {probl} is {result}')

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("antonym of","")
            result = pd.antonym(probl)
            print(f'The antonym of {probl} is {result}')
            speak(f'The antonym of {probl} is {result}')

        print('Exited dictionary!')
        speak('Exited dictionary!') 

    def TakeHindi():
    #It takes microphone input from the user and returns string output

        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='hi')
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)
            #speak("Say that again please...")
            print('Say that again please...')
            return "None"
        return query.lower()

    def Tran():
        print("Tell me the line!")
        speak("Tell me the line!")
        line = TakeHindi()
        result = Translator.tranlate(line)
        Text = result.text
        speak(f"The translation for thids line is :"+Text) 

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
            query = query.replcae(" ","")
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


        elif 'screenshot' in query:
            Screenshot()

        elif 'pause' in query:
            keyboard.press('space bar')
        
        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')
        
        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')
        
        elif 'fullscreen' in query:
            keyboard.press('f')

        elif 'filmmode' in query:
            keyboard.press('t')

        elif 'next video' in query:
            keyboard.press_and_release('shift + n')

        elif 'previous video' in query:
            keyboard.press_and_release('shift + p')

        elif 'decrease volume' in query:
            keyboard.press('F2')

        elif 'increase volume' in query:
            keyboard.press('F3')

        elif 'exit full screen' in query:
            keyboard.press('Escape')
        
        elif 'youtube auto' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'open history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'previous page' in query:
            keyboard.press_and_release('alt + left arrow')

        elif 'next page' in query:
            keyboard.press_and_release('alt + right arrow')

        elif 'open download page' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat me' in query:
            print('Okay mam!')
            speak('Okay mam!')
            rm = takeCommand()
            print('You said : {rm}')
            speak('You said : {rm}')

        elif 'open dictinary' in query:
            Dict()

        elif 'alarm' in query:
            speak('Enter the time!')
            time = input(": Enter the time")

            while True:
                Time_at = datetime.datetime.now()
                now = Time_at.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up mam!")
                    playsound('Soy-bgm.mp3')
                    speak("Alarm stoped!")
                
                elif now > time:
                    break

        elif 'translate' in query:
            Tran()

        elif 'battery' in query:
            bb = psutil.sensors_battery()
            Text = bb.text
            print("The battery stats are: "+Text)
            speak(f"The battery stats are: {Text}")


        elif 'quit' in query:
            print("Quitting mam. Thank you for your time.")
            speak("Quitting mam. Thank you for your time.")
            exit()

TaskExe()
