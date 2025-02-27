import check_files
import os
from config import SAVE_DIR

list_files = check_files.logic_check()

name_sample = []
for i in list_files:
    name_sample.append(i['Name'])


def create_dir(list_name):
    for i in list_name:
        os.makedirs(SAVE_DIR + '/' + str(i), exist_ok=True)


def logic_dir():
    create_dir(list(set(name_sample)))
