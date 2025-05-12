import pyttsx3 as tts
import time
import ctypes
import win32gui
import win32con
import socket
import requests

engine =  tts.init()
engine.say("Hello, your computer has been infected with a virus that will make your computer a living night mare, have fun with this") # living heel as in not blue screen but just as annoything as possible
engine.runAndWait()
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
pcname = socket.gethostname()
ip = socket.gethostbyname(pcname)

def get_location():
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    country = data['country']
    city = data['city']
    region = data['region']
    return country, city, region

country, city, region = get_location()
print(f"Country: {country}")
print(f"City: {city}")
print(f"State: {region}")
