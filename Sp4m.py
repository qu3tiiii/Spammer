import pyautogui as spam
import time

palabras = open("Palabras.txt", 'r')
time.sleep(5)

for Palabras in palabras:
    spam.typewrite(Palabras)
    spam.press('enter')
