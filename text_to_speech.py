import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", engine.getProperty("rate") - 70)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

lock = threading.Lock()  # Add a lock to avoid multiple threads running `runAndWait()`

def text_to_speech(text):
    """Speaks the given text using pyttsx3 with thread safety."""
    def run():
        with lock:  # Ensure only one thread runs at a time
            engine.say(text)
            engine.runAndWait()

    threading.Thread(target=run, daemon=True).start()
