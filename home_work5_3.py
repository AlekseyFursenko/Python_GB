''' Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''

def rle_encoding(data):
    encoding = ''
    prev_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char != prev_char: #если текущий и предыдущий символы не совпадают
                encoding += str(count) + prev_char # записываем в кодировку
                count = 1
                prev_char = char
        else:
            count += 1
            
    encoding += str(count) + prev_char # завершение кодировки последним набором символов
    
    return encoding

def rle_decode(data):
    decode = ''
    count = ''
    
    for char in data:
        if char.isdigit(): # Если это число, то count увеличиваем на это число
            count = char
        else:
            decode += char * int(count) # если не число добавляем в строку decode
            count = ''
    
    return decode

data = 'AAABBBBCCCCCDDDDEEQ'
code_data = rle_encoding(data)
decode_data = rle_decode(code_data)

print(data)
print(code_data)
print(decode_data)
    