import pandas as pd
import csv
from managmant_files_dirs.Hadler_file import JsonHandler


def create_csv_file(url, name_save_file) -> None:
    """
    Загружает онлайн-таблицу Google, обрабатывает её с помощью pandas и сохраняет в CSV-файл.
    """
    df = pd.read_csv(url)

    # Выбираем только нужные столбцы
    selected_columns = df.columns[:18]  # Берем первые 18 столбцов
    new_df = df[selected_columns]

    # Экспортируем в CSV
    new_df.to_csv(f'{name_save_file}.csv', index=False)
    print("CSV-файл успешно создан.")

    
def process_csv(name_file='data_base', mode='default'):
    """
    Читает CSV-файл и преобразует данные в JSON-формат.
    
    Параметры:
    - name_file (str): Имя файла без расширения.
    - mode (str): Режим обработки ('default' или 'signal').
    
    Возвращает:
    - data (list): Данные в формате JSON.
    """
    with open(f'{name_file}.csv', newline='', encoding='utf-8') as file:
        reader_csv = csv.reader(file)
        
        key_map = {
            'default': [('Name', 0), ('Width', 5), ('Length', 10),
                         ('Height', 15), ('Weight', 16), ('Press', 17)],
            'signal': [('Time', 0), ('Name', 1), ('Press', 2)]
        }
        
        if mode not in key_map:
            raise ValueError("Неверный режим обработки. Используйте 'default' или 'signal'.")
        
        return [
            {key: row[idx] for key, idx in key_map[mode]}
            for row in reader_csv if 'СТ-' in row[key_map[mode][0][1]]
             and all(row[i[1]] for i in key_map[mode])
        ]
