import pyautogui

from managmant_files_dirs.Create_dir import get_all_files_if_exist
from managmant_files_dirs.check_files import logic_check, get_files_edit
from menegmant_keyboard.menegment_keyboard import search_eco, save_file_csv
from utils import wait_loading, correct_name_file_csv
from config import path_btn_signal


def first_point(list_screens):
    """
    Получает список координат всех инпутов и возвращает 

    Аргументы:
    - list_screens - список скриншотов инпутов в формате PNG
    """
    list_points = []
    for screen in list_screens:  # Проходимся по списку циклом
        if screen[1:] in ['.png', '.PNG']:
            # Добавляем к названию файла папку, аргумент
            # confidence показывает с какой точностью искать
            location = pyautogui.locateOnScreen('btn/btn_signal/' + screen, confidence=0.78)
            list_points.append({screen[:-4]: location})
            pyautogui.click(location)
        else:
            pass
    return list_points


def main():
    list_samples = logic_check()
    exist_files = get_all_files_if_exist()
    for i in list_samples:
        name_file = correct_name_file_csv(i['Name'], i['Press'])
        if name_file in exist_files:
            print(i['Name'], 'Уже существует')
            pass
        else:
            screens = get_files_edit(path_btn_signal)
            list_point = first_point(screens)
            search_eco(i['Time'])
            save_file_csv(i['Name'], i['Press'])
            wait_loading('btn/btn_signal/save/2.png')
            print(i['Name'], 'Готово')


main()
