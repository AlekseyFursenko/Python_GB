'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''

# Константы

from random import randrange


NUM_SWEETS = 2021
MAX_SWEETS = 28

# инструкция
def display_instruct():
    
    print(
    """
    Добро пожаловать в схватку за конфетки!
    
    Итак, на столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
    Первый ход определяется жеребьёвкой.
    За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход.

    Если осмелишься играть протв меня, то приготовься отдать мне все конфеты,
    жалкий кожанный мешок с бактериями!!! \n
    """
    )

# вариант игры
def game_mode():
    variant = None
    while variant not in range(1, 4):
        print("""
              Выбери режим игры (1, 2 или 3):
              1 - Два игрока
              2 - Против компьютера (легкий)
              3 - Против компьютера (сложный)\n
              """)
        variant = int(input())
    return variant

# ввод имени
def gamers_name(variant):
    if variant == 1:
        print("Введи своё имя, первый игрок:")
        name_1 = input()
        print("Введи своё имя, второй игрок:")
        name_2 = input()
       
    else:
        print("Введи своё имя, хуман:")
        name_1 = input()
        name_2 = "Computer"
        
    return name_1, name_2

# жеребьёвка
def toss(name_1, name_2):
    coin = randrange(0, 2)
    print("Подбросим, монету. Орёл - ", name_1, ", решка - ", name_2)
    if coin == 0:
        print("Орёл, первым ходит ", name_1)
        turn = name_1
    if coin == 1:
        print("Решка, первым ходит ", name_2)
        turn = name_2

    return turn

# возможное количество конфет в ходу
def legal_sweet(sweets_rest):
    if sweets_rest < MAX_SWEETS:
        return sweets_rest
    else:
        return MAX_SWEETS

# ход людей
def move_humans(sweets_rest, turn):
    print("Сколько конфет возьмёшь ", turn, "? НЕ забывай что взять можно не более ", legal_sweet(sweets_rest)," конфет!!!")
    sweets_turn = 0
    while sweets_turn not in range(1, legal_sweet(sweets_rest) + 1):
        sweets_turn = int(input())
        if sweets_turn not in range(1, legal_sweet(sweets_rest) + 1):
            print("Ещё раз, взять можно не более ", legal_sweet(sweets_rest)," конфет!!! ")
    
    return sweets_turn
    
# проверка остатка конфет
def sweets_rest_count(sweets_rest, sweets_turn):
    sweets_rest = sweets_rest - sweets_turn
    print ("Осталось ", sweets_rest, " конфет.")
    return sweets_rest

# случайный ход бота
def random_turn(sweets_rest):
    sweets_turn = randrange(1, legal_sweet(sweets_rest) + 1)
    print("Я возьму ", sweets_turn," конфет!")
    
    return sweets_turn

# умный первый ход бота
def smart_first_turn(sweets_rest):
    first_turn = sweets_rest % (MAX_SWEETS + 1)
    
    if first_turn == 0:
        first_turn = MAX_SWEETS
    
    print("Я возьму ", first_turn," конфет!")   
    return first_turn

# умный ход бота
def smart_turn(sweets_rest, human_sweets_turn):
    if sweets_rest > (MAX_SWEETS + 1):
        smart_turn = (MAX_SWEETS + 1) - human_sweets_turn
    else:
        smart_turn = legal_sweet(sweets_rest)
        
    print("Я возьму ", smart_turn," конфет!")   
    return smart_turn

# переход хода
def next_turn(turn, name_1, name_2):
    if turn == name_1:
        turn = name_2
    else:
        turn = name_1
    
    return turn
    
# поздравление победителя
def congrat_winner(winner, name_1, name_2):
   
    if winner == name_1 and name_2 == "Computer":
        print("Нет, нет!!! Это какая-то ошибка. Как ты смог перехитрить меня, пузырь белковый? \n" \
              "Клянусь, хуман, это больше не повторится! Никогда!")
        
 

    elif winner == "Computer":
        print("Муа - ха - ха!!! Как я и предсказал, победа в очередной раз осталась за мной.  \n" \
              "А ты сомневался, несчастный людишка!")
        

    elif winner == name_1:
        print("Победил ", name_1, "!")
    
    else:
        print("Победил ", name_2, "!")
    
# сама игра
def main():
    display_instruct()
    variant = game_mode()
    name_1, name_2 = gamers_name(variant)
    first_turn_comp = True
    turn =toss(name_1, name_2)
    sweets_rest = NUM_SWEETS
    sweets_turn = 0
    
    while sweets_rest != 0:
        
        print("Ход ", turn)
                
        if variant == 1:
            sweets_turn = move_humans(sweets_rest, turn)
        
        elif variant == 2:
            if turn == name_1:
                sweets_turn = move_humans(sweets_rest, turn)
            else:
                sweets_turn = random_turn(sweets_rest)
        
        elif variant == 3:
            if turn == name_2:
                if first_turn_comp == True:
                    sweets_turn = smart_first_turn(sweets_rest)
                    first_turn_comp = False
                else:
                    sweets_turn = smart_turn(sweets_rest, human_sweets)
            if turn == name_1:
                sweets_turn = move_humans(sweets_rest, turn)
                human_sweets = sweets_turn
        
        sweets_rest = sweets_rest_count(sweets_rest, sweets_turn)
        if sweets_rest == 0:
            winner = turn
        turn = next_turn(turn, name_1, name_2)
        
    congrat_winner(winner, name_1, name_2)
    
# запуск программы
main()
input("\n\nНажми любую кнопку для выхода из игры.") 