from os import startfile
import webbrowser
from pyautogui import click
from keyboard import press
from keyboard import write
import keyboard
from time import sleep

def WhatsappMsg(name, msg):
    webbrowser.open("https://web.whatsapp.com/") #wp - properties
    sleep(10)
    click(x=111, y=243)
    sleep(1)
    write(name)
    sleep(1)
    click(x=179, y=433) #click on first name
    sleep(1)
    click(x=751,y=978) #msg for typing
    sleep(1)
    write(msg)
    press('enter')

# def WhatsappCall(name):
#     webbrowser.open("https://web.whatsapp.com/")
#     sleep(10)
#     click(x=105, y=247)
#     sleep(1)
#     write(name)
#     sleep(2)
#     click(x=179,y=433) #click on first name
#     sleep(1)
#     click(x=751,y=978) #msg for typing
#     sleep(1)
#     click(x=,y=) #click on call button


# def WhatsappChat(name):
#     webbrowser.open("whatsapp.com")
#     sleep(10)
#     click(x=111, y=243)
#     sleep(1)
#     write(name)
#     sleep(1)
#     click(x=179,y=433) #click on first name
#     sleep(1)
#     click(x=751,y=978) #msg for typing
#     sleep(1)
   
# def WhatsappVC(name):
#     webbrowser.open("whatsapp.com")
#     sleep(10)
#     click(x=105, y=247)
#     sleep(1)
#     write(name)
#     sleep(2)
#     click(x=,y=) #click on first name
#     sleep(1)
#     click(x=,y=) #msg for typing
#     sleep(1)
#     click(x=,y=) #click on vc button


def ChromeAuto(comd):
    while True:
        query = str(comd)

        if 'close this tab' in query:
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

        elif 'open bookmark' in query:
            keyboard.press_and_release('ctrl + d')
            press('enter')

        elif 'open incognito' in query:
            keyboard.press_and_release('Ctrl + Shift + n')
        
def YoutubeAuto(comm):
    while True:
        query = str(comm)
        
        if 'pause' in query:
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