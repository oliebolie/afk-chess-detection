from pygame import mixer
import time
import pyautogui
import keyboard

mixer.init()
plays = mixer.Sound("beep.wav")

def repeat_until_stop():
    while True:
        notmyturn = pyautogui.pixelMatchesColor(112, 494, (43, 41, 38))
        if notmyturn:
            print("It's not your turn yet.")
            while notmyturn:
                notmyturn = pyautogui.pixelMatchesColor(112, 494, (43, 41, 38))
                time.sleep(1)
            alarm()
            print("It's your turn! Do you want to run again? (y/n)")
            choice = input().lower()
            if choice != 'y':
                break
        else:
            print("It's your turn!")
            alarm()

def alarm():
    plays.play()
    time.sleep(3)
    plays.play()

repeat_until_stop()
