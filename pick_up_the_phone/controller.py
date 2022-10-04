import contact_ops
import database_ops
import view
import ui
import export
import import_to


# загрузить интерфейс

def show_ui():
    ui.start()


# def add_new_phonebook():
#     global phone_book
#     if phone_book == False:
#         view.warning_delete_phonebook()
    
#     phone_book = database_ops.new_phone_book()
#     return phone_book


def start(phone_book: list):
        
    show_ui()
    
    var = int(view.get_variant())
    match var:
        case 1:# создать новую телефонную книгу
            phone_book = database_ops.new_phone_book()
        
        case 2:# добавить новый контакт
            phone_book.append(contact_ops.new_contact(phone_book))
                    
        case 3:# удалить контакт
            id = int(view.get_id_delete())
            answer = view.get_confirmation()
            if answer == 'y' or answer == 'Y':
                contact_ops.delete_contact(phone_book, id)
            
        case 4:# распечатать книгу
            view.print_phonebook(phone_book)
                
        case 5:# экспорт в csv
            export.export_to_csv(phone_book)
            
        case 6:# импорт из csv
            import_to.import_to_csv(phone_book)
            
        case 7:    
            export.export_to_json(phone_book)
        
        case 8:
            import_to.import_from_json(phone_book)
            
        case 9:    
            exit()
        
        case _:
            print('Input another variant!!')
    
    start(phone_book)
            
