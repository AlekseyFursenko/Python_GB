import view

# новый контакт
def new_contact(phone_book):
    new_id = get_new_id(phone_book)
    contact = view.get_contact_data(new_id)
    return contact
    

def get_new_id(phone_book):
    max_id = 0
    for item in phone_book:
        if item['id'] > max_id:
            max_id = item['id'] 
    
    max_id += 1
    return max_id        

# удалить контакт
def delete_contact(phone_book: list, id):
    for item in phone_book:
        if item['id'] == id:
            phone_book.remove(item)
            return phone_book
    
    return phone_book
        
            
# редактировать контакт