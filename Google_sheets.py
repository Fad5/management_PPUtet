import pandas as pd
import csv
import json
import pprint
from Hadler_file import JsonHandler

def write_json(name_file, data):
    with open(f"{name_file}.json", "w", encoding='utf-8') as fh:
        json.dump(data, fh)
        
def create_cvs_file() -> None:
    """
    Функция забирает онлайн таблицу google, проходится pandas и создает csv с данными
    :return: None
    """
    df = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/10HsBr1OrPiev5bqHZ8HwoG7WfkqpSuzZY5CYfIqyujU/export?format=csv')
    column_names = df.keys().tolist()

    new_df = df[
        [column_names[0], column_names[1], column_names[2], column_names[3], column_names[4], column_names[5],
         column_names[6], column_names[7], column_names[8],
         column_names[9], column_names[10], column_names[11], column_names[12], column_names[13],
         column_names[14], column_names[15], column_names[16], column_names[17]]]  # Выберем из даты фрейма столбцы и сохраним в новый дате фрейм
    new_df.to_csv('data_base.csv', index=False)  # Экспорт в CSV файл

# create_cvs_file()

with open('data_base.csv', newline='', encoding='utf-8') as File:
    reader = csv.reader(File)
    js = []
    for row in reader:
        if 'СТ-' in row[0]:
            if  row[2] and row[3] and row[4] :
                 js.append({
                        'Name': row[0],
                        'Width': row[5],
                        'Length': row[10],
                        'Height': row[15],
                        'Weight': row[16],
                        'Press': row[17]
                    })
print(js)

JsonHandler.write_json('goo.json', js)
aaaa = JsonHandler.read_json('goo.json')

pprint.pprint(aaaa)