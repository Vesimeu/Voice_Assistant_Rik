# commands_rik.py
import time
import random
from playsound import playsound
import pyttsx3
from words import get_random_response, get_random_execution_response , how_are_you_responses , music_rik
import webbrowser
import threading
import queue
import pygame



def open_browser():
    webbrowser.open("http://www.google.com")
    return get_random_execution_response()

# Инициализация очереди
speech_queue = queue.Queue()

pygame.mixer.init()

def play_sound(file_path):
    """Функция для воспроизведения звука."""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def speak():
    engine = pyttsx3.init()
    while True:
        text = speech_queue.get()  # Берем фразу из очереди
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

def handle_command(command):
    engine = pyttsx3.init()
    global main
    if command == "стоп команда":
        print("Завершение работы.")
        main()  # Завершение программы
    elif command.lower() == "открой браузер":
        response = open_browser()
    elif command.lower() == "как дела":
        response = random.choice(how_are_you_responses)  # Выбор случайного ответа
        play_sound(response)
    elif command.lower() == "включи музыку":
        print("Зашёл сюда")
        play_sound(music_rik)
    elif command.lower() == "неизвестная команда":
        response = "Извини, я не понял команду."

    # engine.say(response)
    # engine.runAndWait()
    # speech_queue.put(response)

def main():
    # Запуск потока для произнесения фраз
    threading.Thread(target=speak, daemon=True).start()
if __name__ == "__main__":
    main()