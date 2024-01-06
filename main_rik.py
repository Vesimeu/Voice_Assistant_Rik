import speech_recognition as sr
import pyttsx3
import random
import tkinter as tk
from commands_rik import handle_command
from words import get_random_activation_response
import threading
from PIL import Image, ImageTk
from words import activation_words
from words import additional_command_request, termination_commands
from words import command_phrases
from playsound import playsound
import random
from words import rick_greetings  # Импортируем список приветствий


def show_image():
    """ Отображает окно с изображением Рика поверх всех окон в правом нижнем углу """
    window = tk.Tk()
    window.title("Рик")

    # Загрузка и отображение изображения
    image = Image.open("rick_image.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(window, image=photo)
    label.image = photo  # Сохраняем ссылку на изображение
    label.pack()

    # Установка размера и позиции окна
    window_width, window_height = 300, 200  # Размеры окна можно настроить
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_right = int(screen_width - window_width - 10)  # Отступ справа
    position_down = int(screen_height - window_height - 10)  # Отступ снизу
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    # Установка окна поверх других окон
    window.attributes('-topmost', True)

    # Запуск окна
    window.mainloop()

def listen_for_activation():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.5
    recognizer.non_speaking_duration = 0.1
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print("Слушаю...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU").lower()
            print(f"Распознано: {text}")
            if any(word.lower() in text for word in activation_words):
                greeting = random.choice(rick_greetings)  # Выбор случайного приветствия
                playsound(greeting, block=False)  # Неблокирующее воспроизведение приветствия
                return True
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError:
            print("Не удалось подключиться к сервису Google Speech Recognition")

def main():
    engine = pyttsx3.init()
    if listen_for_activation():
        image_thread = threading.Thread(target=show_image, daemon=True)
        image_thread.start()

        while True:
            command = get_command()
            if command:
                if command in activation_words:  # Проверка на активационные слова
                    greeting = random.choice(rick_greetings)  # Выбор случайного приветствия
                    playsound(greeting, block=False)  # Неблокирующее воспроизведение приветствия
                    continue
                if command == "стоп команда":  # Проверка на стоп-команду
                    print("Завершение работы.")
                    break
                handle_command(command)  # Обработка команды
            else:
                print("Команда не распознана или отсутствует")
                continue  # Переход к следующему циклу прослушивания
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Жду команду...")
        audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            command_text = recognizer.recognize_google(audio, language="ru-RU").lower()
            print(f"Распознанная команда: {command_text}")
            if any(cmd in command_text for cmd in termination_commands):  # Проверка стоп-команд
                return "стоп команда"
            for command, phrases in command_phrases.items():
                if any(phrase in command_text for phrase in phrases):
                    return command
            return "неизвестная команда"
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
        except sr.RequestError:
            print("Не удалось подключиться к сервису Google Speech Recognition")
            return None


if __name__ == "__main__":
    main()