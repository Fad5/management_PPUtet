from menegmant_keyboard import check_files
import os
from config import SAVE_DIR


def get_data_in_js() -> list:
    """
    Функция запускает логику работы проверки фалов
    которые есть на экофизике и в таблице google sheets,
    получает json, заберет только название для дальнейшего создания папок

    Возвращает:
    - list_files - список названия папок которые нужно создать
    """
    list_files = check_files.logic_check()
    name_sample = []
    for i in list_files:
        name_sample.append(i['Name'])
    return list_files


def create_dir(list_names: list) -> None:
    """
    Функция создания папок, на вход принимает список с названиями фалов
    """
    for name in list_names:
        os.makedirs(SAVE_DIR + '/' + str(name), exist_ok=True)


def logic_dir() -> None:
    """
    Логика работы функции
    """
    list_name_dir = get_data_in_js()
    # Получает список, переводит в set, для того чтобы получить уникальные значения
    # И обратно переводит в list для дальнейше работы
    create_dir(list(set(list_name_dir)))


logic_dir()
