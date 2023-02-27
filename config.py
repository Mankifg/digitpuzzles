from pyautogui import *
import pyautogui as pag
import time
import keyboard
import win32api, win32con

inp = []

nums = [
    "Top Left",
    "Bottom right"
]

for i in range(len(nums)):
    print(f"Go to {nums[i]} and press 1")
    keyboard.wait("1")
    pos = str(pag.position()[0]) + "," + str(pag.position()[1])
    inp.append(pos)

with open("config.txt", "w") as f:
    for i, v in enumerate(inp):
        f.write(v)
        f.write("\n")
