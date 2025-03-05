from tkinter import filedialog

from Google_sheets import process_csv, create_csv_file
from config import LINK_TIME_SAMPLE, SAMPLE
from managmant_files_dirs.Hadler_file import JsonHandler
from signal_ import management_signal


def path_save() -> tuple:
    """
    Открывает два диалоговых окна для выбора директорий.

    Первое окно позволяет выбрать папку, в которой находятся файлы экофизики.
    Второе окно позволяет выбрать папку для сохранения файлов.

    Возвращает:
        tuple: Кортеж из двух строк, каждая из которых содержит путь к выбранной папке.
               Filepath — путь к папке с файлами экофизики,
               save_path — путь к папке для сохранения.
    """
    filepath = filedialog.askdirectory(title="Выберите папку в которой находятся файлы экофизики")
    save_path = filedialog.askdirectory(title="Выберите папку сохранения")
    return filepath, save_path


def download_files() -> None:
    """
    Функция для скачивания csv файлов и преобразования из в json файлы
    """
    create_csv_file(f'{SAMPLE}/export?format=csv')
    sample_sizes = process_csv()
    JsonHandler.write_json('goo.json', sample_sizes)

    create_csv_file(f'{LINK_TIME_SAMPLE}/export?format=csv', 'data_for_signal')
    sample_time = process_csv('data_for_signal', 'signal')
    JsonHandler.write_json('data_for_signal', sample_time)


def main() -> None:
    save_path, filepath = path_save()
    download_files()
    management_signal(save_path, filepath)


"""
Логика программы 

1. Запускается программа, у пользователя спрашивает из какой папки брать файлы экофизики, 
и как сохранять данные после обработке

2.Переменные находятся в файле майне и запускается функцией main()

3. Сохраняется в файле под название setting.json
"""
