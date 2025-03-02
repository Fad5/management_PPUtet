import pandas as pd
import csv
import json
import pprint
from managmant_files_dirs.Hadler_file import JsonHandler


def create_csv_file(url) -> None:
    """
    Загружает онлайн-таблицу Google, обрабатывает её с помощью pandas и сохраняет в CSV-файл.
    """
    df = pd.read_csv(url)

    # Выбираем только нужные столбцы
    selected_columns = df.columns[:18]  # Берем первые 18 столбцов
    new_df = df[selected_columns]

    # Экспортируем в CSV
    new_df.to_csv('data_base.csv', index=False)
    print("CSV-файл успешно создан.")


def process_csv():
    with open('data_base.csv', newline='', encoding='utf-8') as file:
        reader_csv = csv.reader(file)
        js = [
            {
                'Name': row_[0], 'Width': row_[5], 'Length': row_[10],
                'Height': row_[15], 'Weight': row_[16], 'Press': row_[17]
            }
            for row_ in reader_csv if 'СТ-' in row_[0] and all(row_[i] for i in [2, 3, 4])
        ]
    return js


