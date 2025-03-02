import pyautogui
import json
from config import path_btn_signal


def first_point(list_screens):
    """
    Получает список координат всех инпутов и возвращает 

    Аргументы:
    - list_scrins - список скпиншотов инпутов в формате PNG

    Возвращает:
    - list_points - координаты инпутов 
    """
    list_points = []
    for screen in list_screens:  # Проходмся по списку циклом
        try:
            # Добавляем к названию файла папку, аргумент
            # confidence показывает с какой точностью искать
            location = pyautogui.locateOnScreen('btn_pputest/' + screen, confidence=0.95)
            list_points.append({screen[:-4]: location})

            # pyautogui.doubleClick(location)
            # pyautogui.write('Hello world!', interval=0.1)

        except pyautogui.ImageNotFoundException:
            print(f'ImageNotFoundException: {screen}')
    return list_points


def delete_input_txt(locations):
    """
    Функция для удаления данных в инпуте 

    Аргументы:
    - locations - координаты инпутов 

    Возвращает:None
    """
    for location in locations:
        pyautogui.doubleClick(location)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')


def get_key(i_need_this_dict):
    for key in i_need_this_dict:
        value = i_need_this_dict[key]
        return key, value


def enter_data(data, locations):
    for location in locations:
        print(location)
        key, value = get_key(location)
        pyautogui.doubleClick(value)
        print(data[key])
        pyautogui.write(data[key], interval=0.1)

    # pyautogui.typewrite(data)
    # pass


def get_data(name_file):
    with open(name_file, "r") as fh:
        data = json.load(fh)
        return data


def get_keys_or_value(data):
    """
    Получение списка со значениями или ключами 
    
    Аргументы:
    - data - словарь
    
    Возвращает:
    - list_keys - список со значениями или ключами
    """
    list_keys = []
    for i in data:
        key = get_key(i)
        list_keys.append(key[1])
    print(list_keys)
    return list_keys


def main():
    list_points = first_point(path_btn_signal)
    data = get_data('dimensions.json')
    for i in data:
        print(i)
        enter_data(data=i, locations=list_points)
        # Функция для ввода данных о пригрузе и о файле с испытаниями
        delete_input_txt(get_keys_or_value(list_points))


main()
