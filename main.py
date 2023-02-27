from pyautogui import *
import pyautogui as pag
import time
import keyboard
import win32api, win32con
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
)

with open("config.txt", "r") as f:
    inp1 = f.read().splitlines()

with open("words.txt", "r") as f:
    words = f.read().splitlines()

tl, br = [], []

tl = inp1[0].split(",")
br = inp1[1].split(",")

for i in range(len(tl)):
    tl[i] = int(tl[i])
    br[i] = int(br[i])

def grayscale(filename):
    img_rgb = Image.open(filename)
    img_gray = img_rgb.convert('L')
    img_gray.save(filename)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



def readimage(x, y, w, h):
    im1 = pag.screenshot(region=(x, y, w, h))
    im1.save(r"./image.png")
    grayscale(r"./image.png")

    image = "./image.png"
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    if len(text) > 0:
        text = text[0:-2]
        text = text.replace("x", "*")

    return text

def mf(l):
    counter = 0
    num = l[0]
     
    for i in l:
        curr_frequency = l.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def remv(l):
    nw = []

    for i in range(len(l)):
        if not (l[i] == "" and " " in l[i]):
            nw.append(l[i])  
       
    return nw

def good(word):
    return word in words


outputs = []

print("Configured\nPress space!")
keyboard.wait("space")
print("START")

mismach = 0

while True:
    

    inp = readimage(tl[0], tl[1], br[0] - tl[1], br[1] - tl[1])
    print(f"MM: {mismach} | {inp}")
    
    if good(inp):
        pag.typewrite(inp, interval=0.01)
        mismach = 0
    else:
        mismach = mismach + 1
    
    if mismach > 10:
        mismach = 0
        pag.typewrite("xx", interval=0.01)


