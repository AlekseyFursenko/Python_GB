FIELDS_NAMES = ['Name', 'Surname', 'Phone_number', 'Description']

def get_fields_names():
    global FIELDS_NAMES
    heads = FIELDS_NAMES.insert(0, 'id')
    return heads

def get_contact_data(id):
    contact = {}
    contact['id'] = id
    for item in FIELDS_NAMES:
        data = input(f"Input {item}:")
        contact[item] = data
    return contact

def warning_delete_phonebook():
    print("У вас есть записи в текущей книге и они будут удалены!!!")
    input()
    
def print_phonebook(phone_book):
    for item in phone_book:
        print(item)
    input()
        
def get_variant():
    var = input("Choose your variant - ",)
    return var

def get_id_delete():
    id_del = input("Choose id number your want to delete from phonebook - ",)
    return id_del

def get_confirmation():
    a = input('A you sure (y/n) ', )
    match a:
        case 'y' | 'Y' | 'n' | 'N':
            return a
        case _:
            print('input y or n')
            get_confirmation()
            