import keyboard
import pyautogui
import time
import platform
import os
import pyperclip

from config import path_btn_pputest, path_btn_signal


def correct_name_file_csv(name: str, press: str) -> str:
    """
    Функция для создания имени файла в который
    входит названия образца и пригруз 

    Аргументы:

    - name - названия образца
    - press - масса пригруза
    """
    new_name = str(name) + f'({str(press)})'
    return str(new_name)


def wait_loading(screen_path: str) -> None:
    """
    Функция для ожидания загрузки программы signal

    Принцип работы:
    Работает по принципу когда будет соответствие с этим скриншотом
    программа продолжит свою работу когда найдет это изображение

    Аргументы:
    - screen_path - скриншот
    """
    time.sleep(1)
    i = 0
    while i < 1:
        time.sleep(0.5)
        print('Waiting')
        try:
            location = pyautogui.locateOnScreen(screen_path, confidence=0.80)
            print(location)
            i += 1
        except:
            i = 0


def check_platform() -> tuple:
    """
    Функция для отслеживания версии windows

    Возвращает:
    - version_platform - список с данными о платформе
    """
    version_platform = platform.win32_ver()
    return version_platform


def paste(text: str):
    """
    Функция имитации нажатия ctrl + v
    и вставки текста

    Аргументы:
    - text - текст который нужно вставить
    """
    # buffer = pyperclip.paste()  # Сохраняем текущий буфер обмен
    pyperclip.copy(text)  # Копируем новый текст в буфер обмена
    keyboard.press_and_release('ctrl + v')  # Эмулируем нажатие Ctrl + V (вставку)
    # pyperclip.copy(buffer)  # Восстанавливаем оригинальное содержимое буфера:


def timeout_step() -> None:
    """
    Функция паузы
    """
    time.sleep(1.3)


def create_dir() -> None:
    """
    Функция для создания корневых паок в которых будут храниться скриншоты кнопок
    """
    for i in path_btn_pputest, path_btn_signal:
        os.makedirs(i, exist_ok=True)
