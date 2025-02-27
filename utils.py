import pyautogui
import time


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
