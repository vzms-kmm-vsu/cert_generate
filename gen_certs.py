import csv
import os
import argparse

data = {
    'gender': 'AUTHORGENDER',
    'fio': 'AUTHORFIO',
    'doc': 'AUTHORDOC'
}

parser = argparse.ArgumentParser(description='Скрипт генерации сертификатов участников')
parser.add_argument('sample_name', type=str, help='Полное имя используемого шаблона в формате .fodf')
parser.add_argument('authors_list', type=str, help='Таблица с данными авторов в формате .csv, требуемые столбцы: gender; fio; doc')
args = parser.parse_args()

cert_folder = f"./cert/{args.sample_name.split('.')[0]}"

os.makedirs(cert_folder, exist_ok=True)

with open(args.sample_name, 'r', encoding='utf-8') as fodtfile:
    fodt_str = fodtfile.read()

with open(args.authors_list, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    headers = reader.fieldnames
    for row in reader:
        print(' '.join([row[x] for x in headers]))
        fodt_new = fodt_str[:]
        for x, y in data.items():
            fodt_new = fodt_new.replace(y, row[x])
        with open(f'{cert_folder}/{row["fio"]}.fodt', 'w', encoding='utf-8') as new_fodt:
            new_fodt.write(fodt_new)
