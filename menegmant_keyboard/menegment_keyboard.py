import keyboard
import pyautogui

from config import SAVE_DIR
from utils import timeout_step, correct_name_file_csv, paste


def search_eco(time_file: str) -> None:
    """
    Функция для поиска файлов
    """
    timeout_step()
    pyautogui.hotkey('ctrl', 'l')
    timeout_step()
    keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))
    timeout_step()
    pyautogui.write('E:/EDIT')
    timeout_step()
    pyautogui.press('enter')
    timeout_step()
    pyautogui.hotkey('ctrl', 'f')
    timeout_step()
    pyautogui.write(time_file.replace('-', '_'))
    timeout_step()

    for _ in range(2): pyautogui.press('down')
    timeout_step()
    for _ in range(4): pyautogui.press('up')
    btn_open = pyautogui.locateOnScreen('Signal/save/open.png', confidence=0.82)
    if btn_open:
        pyautogui.click(btn_open)
    else:
        print("Кнопка 'Открыть' не найдена.")


def save_file_csv(name, press):
    timeout_step()
    pyautogui.press('delete')
    paste(str(correct_name_file_csv(name, press)))
    timeout_step()
    pyautogui.hotkey('ctrl', 'l')
    paste(f"{SAVE_DIR}/{name}")
    pyautogui.press('enter')
    if btn := pyautogui.locateOnScreen('Signal/save/save.png', confidence=0.80): pyautogui.click(btn)
