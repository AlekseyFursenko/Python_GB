'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет'''

#day_week = None
#while not day_week in range(1,8):
#    print('Input a day of week (in range from 1 to 7 where 1 is Monday and 7 is Sunday)', end=' ')
#    day_week = int(input())
#    if day_week in range(1, 8):
#        if day_week < 6:
#            print('This day is not weekend')
#        else:
#            print('This is weekend')
#    else:
#        print('You input a wrong number, please try again!')


'''Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

combinations = 8 #Колличество возможных комбинаций при трёх преременных 2^3=8
true_count = 0 # счётчик истинности утверждения при различных значениях предикат

print(' X  Y  Z   ¬(X ⋁ Y ⋁ Z)  =   ¬X ⋀ ¬Y ⋀ ¬Z')

# for i in range(0,combinations):
#     num = format(i, '0>3b')
#     left_part = bool(not((int(num[2]) or int(num[1])) or int(num[0])))
#     right_part = bool((not(int(num[2])) and not(int(num[1]))) and not(int(num[0])))

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            left_part = bool(not((x or y) or z))
            right_part = bool((not(x) and not(y)) and not(z))
            result = (bool(left_part == right_part))
            print(f'{x, y, z}    {left_part}       {result}    {right_part}')
            if result == True:
                true_count +=1
                
if true_count == combinations:
    print(f'Statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is True for all values of predicate')
else:
    print(f'Statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is False')



'''Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

# print('Please, input integer coordinates X and Y (X ≠ 0 and Y ≠ 0)')
# x = int(input('X = '))
# y = int(input('Y = '))

# if (x > 0) and (y > 0):
#     print(f'x={x}, y={y} -> 1')
# elif (x < 0) and (y > 0):
#     print(f'x={x}, y={y} -> 2')
# elif (x < 0) and (y < 0):
#     print(f'x={x}, y={y} -> 3')
# elif (x > 0) and (y < 0):
#     print(f'x={x}, y={y} -> 4')
# else:
#     print('Your input is wrong!')


'''Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).'''

# print('Please, input number of interested quarter (1, 2, 3 or 4)', end=' ')
# qtr = int(input())

# if qtr == 1:
#     print(f'Range of coordinates for {qtr} quarter for x are (0, +infinity), for y are (0, +infinity)')
# elif qtr == 2:
#     print(f'Range of coordinates for {qtr} quarter for x are (0, -infinity), for y are (0, +infinity)')
# elif qtr == 3:
#     print(f'Range of coordinates for {qtr} quarter for x are (0, -infinity), for y are (0, -infinity)')
# elif qtr == 4:
#     print(f'Range of coordinates for {qtr} quarter for x are (0, +infinity), for y are (0, -infinity)')
# else:
#     print('Your input is wrong!')

'''Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''

# from math import sqrt


# print('Please, input integer coordinates X and Y for point A:')
# x1 = int(input('xA = '))
# y1 = int(input('yA = '))
# print('Please, input integer coordinates X and Y for point B:')
# x2 = int(input('xB = '))
# y2 = int(input('yB = '))

# dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)

# print(f'Length of the segment (AB) is {round(dist,2)}')
