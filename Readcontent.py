import pyttsx3
import threading

def _tts_thread(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def read(text):
    t = threading.Thread(target=_tts_thread, args=(text,))
    t.start()
