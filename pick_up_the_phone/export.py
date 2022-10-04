import csv
import json
from pathlib import Path


# экспорт csv
def export_to_csv(phone_book: list):
    
    csv_file = Path.cwd()/'pick_up_the_phone'/'contacts.csv'
    
    with open(csv_file, 'w', newline='') as csvf:
        field_names = ['id', 'Name', 'Surname', 'Phone_number', 'Description']
        writer = csv.DictWriter(csvf, fieldnames=field_names)

        writer.writeheader()
        for item in phone_book:
            writer.writerow(item)
        
# экспорт json

def export_to_json(phone_book: list):
    
    json_file = Path.cwd()/'pick_up_the_phone'/'contacts.json'
    
    with open(json_file, 'w') as jsonf:
        json.dump(phone_book, jsonf)
        