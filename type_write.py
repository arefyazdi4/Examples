import pyautogui
from time import sleep

if __name__ == '__main__':
    print("shit")
    sleep(2)
    # spamFile = open("text.txt", 'r')
    spamFile = """i love morty
                and i hope morty love me
                i want to rap may arm around him
                and fill him inside me"""

    for word in spamFile:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


