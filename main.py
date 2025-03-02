# Запуск signal 
# Запуск PPUtest
import pprint

from Google_sheets import process_csv_signal, create_csv_file
from config import LINK_TIME_SAMPLE
from managmant_files_dirs.Hadler_file import JsonHandler

# Создание json
# create_csv_file('https://docs.google.com/spreadsheets/d/10HsBr1OrPiev5bqHZ8HwoG7WfkqpSuzZY5CYfIqyujU/export?format=csv')
# js = process_csv()
# JsonHandler.write_json('goo.json', js)
# aaaa = JsonHandler.read_json('goo.json.json')



# create_csv_file(f'{LINK_TIME_SAMPLE}/export?format=csv', 'data_for_signal')
# aaaa = process_csv_signal('data_for_signal')
# pprint.pprint(aaaa)
# JsonHandler.write_json('data_for_signal', aaaa)