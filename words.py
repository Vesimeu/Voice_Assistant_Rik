# words.py
import random

activation_words = ["Рик", "Привет Рик", "привет", "здарова заебал", "здорово заебал"]

activation_responses = [
    "Да-да, чё хотел?",
    "Слушаю тебя, рассказывай.",
    "Я тут, что тебе нужно?"
]

# Команды и их ответы
command_phrases = {
    "открой браузер": ["открой браузер", "запусти браузер", "открыть интернет"],
    "как дела": ["как дела", "как твои дела", "как настроение"]
    # Добавьте другие команды и их фразы здесь
}

commands = {
    "открой браузер": ["Открываю браузер..."],
    "как дела": ["Всё в норме, спасибо!", "Ахуенчик!", "Тебя это не должно волновать!"]
    # Добавьте ответы на команды здесь
}

execution_responses = [
    "Окей",
    "Хорошо",
    "Сделано",
    "Так уж и быть",
]

# Пути к приветственным аудиофайлам
rick_greetings = [
    "value/greeting1.mp3",
    "value/greeting2.mp3",
    "value/greeting3.mp3"
    # Добавьте пути к другим аудиофайлам здесь
]


# Фразы для завершения работы
termination_commands = ["на этом всё", "больше ничего", "нет, это всё"]

# Фразы для запроса о дополнительных командах
additional_command_request = ["Будут ли ещё какие-то команды?", "Что-то ещё?", "Есть ещё команды?"]


def get_random_execution_response():
    return random.choice(execution_responses)

def get_random_response(command):
    return random.choice(commands.get(command, ["Не знаю, что и сказать..."]))

def get_random_activation_response():
    return random.choice(activation_responses)
