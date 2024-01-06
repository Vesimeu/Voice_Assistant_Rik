# commands_rik.py
from words import get_random_response
import pyttsx3
from words import get_random_response, get_random_execution_response
import webbrowser
import threading
import queue
import time



def open_browser():
    webbrowser.open("http://www.google.com")
    return get_random_execution_response()

# Инициализация очереди
speech_queue = queue.Queue()

def speak():
    engine = pyttsx3.init()
    while True:
        text = speech_queue.get()  # Берем фразу из очереди
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

def handle_command(command):
    engine = pyttsx3.init()
    if command.lower() == "открой браузер":
        response = open_browser()
    elif command.lower() == "неизвестная команда":
        response = "Извини, я не понял команду."
    else:
        response = get_random_response(command)

    engine.say(response)
    engine.runAndWait()
    speech_queue.put(response)

def main():
    # Запуск потока для произнесения фраз
    threading.Thread(target=speak, daemon=True).start()
if __name__ == "__main__":
    main()