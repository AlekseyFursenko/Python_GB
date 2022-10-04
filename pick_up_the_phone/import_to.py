import csv
import json
from pathlib import Path


# импорт csv
def import_to_csv(phone_book: list):
    
    csv_file = Path.cwd()/'pick_up_the_phone'/'contacts.csv'
    
    with open(csv_file, encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter = ",")
    
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
    
    # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'File consist following fields: {", ".join(row)}')
            # Ввод полей csv файла в phonebook
            phone_book.append({'id':row['id'],
                            'Name':row['Name'],
                            'Surname':row['Surname'],
                            'Phone_number':row['Phone_number'],
                            'Description':row['Description']})
            
            count += 1
    print(f'Total imported {count + 1} rows.')


# импорт json
def import_from_json(phone_book: list):
    
    json__file = Path.cwd()/'pick_up_the_phone'/'contacts.json'
    
    with open(json__file, 'r') as jsonf:
        json_data = json.load(jsonf)
        
        for item in json_data:
            phone_book.append(item)
    
    return phone_book