import os

import pyautogui
import keyboard
from managmant_files_dirs.Hadler_file import JsonHandler
from config import coordinates_input_trials

coordinates = {}


def save_coordinates(list_text, count, name_save_field):
    print(count - 1)
    x, y = pyautogui.position()
    field_name = f"{name_save_field}{count}"
    coordinates[field_name] = (x, y)
    print(f"Сохранена координата {list_text[count - 1]}: {x}, {y}")
    if count == len(list_text):
        pass
    else:
        print('NEXT_____________________________________')
        print('\nНажмите на ' + list_text[count])
    count += 1
    return count


def get_coordinates_(list_text, name_save_field):
    field_index_ = 1
    print("Нажмите Enter для сохранения координат")
    print('\nНажмите на ' + list_text[field_index_ - 1])
    while True:
        if keyboard.is_pressed("enter"):
            field_index_ = save_coordinates(list_text, field_index_, name_save_field)
            keyboard.wait("enter")
        if len(list_text) == field_index_ - 1:
            break


def save_json():
    JsonHandler.write_json('settings', coordinates)


def list_current_text(count_trials):
    current_list = []
    count = 1
    for range_i in range(count_trials):
        for i in coordinates_input_trials:
            current_list.append(i + ' ' + str(count))
        count += 1
    return current_list


def logic_poit_trial():
    list_fails = os.listdir()
    if 'settings.json' in list_fails:
        resave = input("У вас уже есть сохраненные координаты перезаписать? 1.Да 2.Нет ")
        if resave == "1":
            count_trials = int(input('Введите количество испытаний: '))
            current_text = list_current_text(count_trials=count_trials)
            get_coordinates_(list_text=current_text, name_save_field='field_trials_')
            save_json()
        else:
            pass
    else:
        count_trials = int(input('Введите количество испытаний: '))
        current_text = list_current_text(count_trials=count_trials)
        get_coordinates_(list_text=current_text, name_save_field='field_trials_')
        save_json()