import json
import csv


class JsonHandler:
    """
    Клас предназначен для работы с json файлами
    """

    @staticmethod
    def write_json(path, data):
        """
        Функция для записи json файлов

        Аргументы:
        - path - путь к файлу
        - data - данные для записи 
        """
        with open(f"{path}.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def read_json(path):
        """
        Функция для чтения json файлов

        Аргументы:
        - path - путь к файлу
        """
        with open(f"{path}.json", "r") as file:
            data = json.load(file)
        return data


class CsvHandler:
    @staticmethod
    def read_csv(path, encoding='utf-8'):
        """
        Функция для чтения csv файлов

        Аргументы:
        - path - путь к файлу
        """
        with open(f'{path}.csv', newline='', encoding=encoding) as File:
            data = csv.reader(File)
        return data
