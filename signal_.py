import sys

import pyautogui, pyperclip, keyboard
from datetime import time
import time
from check_files import logic_check, get_files_edit
from utils import correct_name_file_csv, wait_loading
from config import SAVE_DIR, path_btn_signal, EDIT_ECO


def first_point(list_screens):
    """
    Получает список координат всех инпутов и возвращает 

    Аргументы:
    - list_screens - список скриншотов инпутов в формате PNG
    """
    list_points = []
    for screen in list_screens:  # Проходимся по списку циклом
        if screen[1:] in ['.png', '.PNG']:
            print(screen)
            # Добавляем к названию файла папку, аргумент
            # confidence показывает с какой точностью искать
            location = pyautogui.locateOnScreen('Signal/' + screen, confidence=0.78)
            list_points.append({screen[:-4]: location})
            pyautogui.click(location)
        else:
            pass
    return list_points


def paste(text: str):
    """
    Функция имитации нажатия ctrl + v
    и вставки текста

    Аргументы:
    - text - текст который нужно вставить
    """
    buffer = pyperclip.paste()  # Сохраняем текущий буфер обмен
    pyperclip.copy(text)  # Копируем новый текст в буфер обмена
    keyboard.press_and_release('ctrl + v')  # Эмулируем нажатие Ctrl + V (вставку)
    pyperclip.copy(buffer)  # Восстанавливаем оригинальное содержимое буфера:


def search_eco(time_file: str):
    """
    Функция для поиска файлов
    """
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(2)
    keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))
    time.sleep(0.3)
    time.sleep(0.3)
    pyautogui.write('E:/EDIT')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.3)
    pyautogui.write(time_file.replace('-', '_'))
    time.sleep(0.3)
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(0.3)
    time.sleep(0.3)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    location_open_bnt = pyautogui.locateOnScreen('Signal/save/open.png', confidence=0.82)
    pyautogui.click(location_open_bnt)


def save_file_csv(name, press):
    time.sleep(3)
    pyautogui.press('delete')
    name_file_csv = str(correct_name_file_csv(name, press))
    paste(name_file_csv)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    text_search = str(SAVE_DIR) + '/' + str(name)
    print(text_search)
    paste(text_search)
    pyautogui.press('enter')
    location_save_bnt = pyautogui.locateOnScreen('Signal/save/save.png', confidence=0.80)
    pyautogui.click(location_save_bnt)


def main():
    list_samples = logic_check()
    for i in list_samples:
        screens = get_files_edit(path_btn_signal)
        list_point = first_point(screens)
        search_eco(i['Time'])
        save_file_csv(i['Name'], i['Press'])
        wait_loading('Signal/save/2.png')
        print(i['Name'], 'Готово')



main()
