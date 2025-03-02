from managmant_files_dirs import check_files
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
    return name_sample


def create_dirs(list_names: list) -> None:
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
    create_dirs(list(set(list_name_dir)))


def get_all_files_if_exist() -> list:
    """
    Получение уже существующих фалов

    Возвращает:
    - is_files - список существующих файлов
    """
    dirs = list(set(get_data_in_js()))
    is_files = []
    for dir_save in dirs:
        files = os.listdir(SAVE_DIR + '/' + dir_save)
        if files:
            for file in files:
                is_files.append(file[:-4])
    return is_files




