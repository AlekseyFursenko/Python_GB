'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 0,56 -> 11'''

# number = input('please enter your number ')
# summ = 0
# for i in range(0,len(number)):
#     if (number[i] == ',') or (number[i] == '.'):
#         continue
#     summ += int(number[i])
# print(f'The sum of digits of the number is - {summ}')


'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
'''Variant 1'''
# from math import factorial


# number = int(input('please enter your number '))
# print(f'Factorals for each number in range from 1 to {number}')
# for i in range(1, number+1):
#     print(factorial(i), end=(' '))

'''Variant 2'''
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         n = n * fact(n-1)
#         return n
        
# number = int(input('please enter your number '))
# print(f'Factorals for each number in range from 1 to {number}')
# for i in range(1, number+1):
#     print(fact(i), end=(' '))

'''Variant 3 match/case'''
# def fact(n):
#     match n:
#         case 0 | 1:
#             return 1
#         case _:
#             return n * fact(n - 1)
        
# number = int(input('please enter your number '))
# print(f'Factorals for each number in range from 1 to {number}')
# for i in range(1, number+1):
#     print(fact(i), end=(' '))
    
    
'''Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.'''

# k = int(input('please enter integer positive number '))
# list = []

# for i in range(1, k):
#     list.append((1 + 1/i)**i)
# print(list)

'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях.'''

# from random import random, randrange


# n = int(input('please enter integer positive number '))
# list = []

# for i in range(0, n):
#     list.append(randrange(-n, n+1))
# print(list) 
    
# print(f"Input indexes of above mentioned lists' elements would you like to multiply (in range 0 to {n - 1})")
# print('Use space bar for divide indexes')
# indexes = input()

# list_idexes = indexes.split(' ')
# mult_elements = list[int(list_idexes[0])]

# for i in range(1, len(list_idexes)):
#     mult_elements *= list[int(list_idexes[i])]
    
# print(mult_elements)    

'''Реализуйте алгоритм перемешивания списка.'''

# from random import random, randrange


# lst = list(range(1, 11))
# print('Initial list ', lst)

# for i in range(0, len(lst)):
#     removed = lst.pop(i)
#     lst.insert(randrange(0, len(lst)), removed)
    
# print(lst)
    