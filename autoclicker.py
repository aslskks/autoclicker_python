import pyautogui as py
import keyboard

while True:
    if keyboard.read_key() == "shift":
        for i in range(10):
            posicion = (py.position())
            py.click(posicion)
