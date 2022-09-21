'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 0,56 -> 11'''

# a = -123456.56123
# b = sum(list(map(int, str(a).split('.')[1])))
# print(a, ' -> ', b)


'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
# from math import factorial

# n = int(input("Input an integer number:"))
# b = [factorial(i) for i in range(1, n + 1)]
# print(b)

'''Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.'''

# k = int(input("Input an integer number:"))
# b = [(1 + i/k)**k for i in range(1, k + 1)]
# sum_b = sum(b)
# print(b, sum_b)


'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях.'''

# from random import randrange


# n = int(input("Input an integer number:"))
# b = [randrange(-n, n+1) for i in range(1, n + 1)]
# print(b)

# print(f"Input positions of above mentioned lists' elements would you like to multiply (in range 1 to {n})")
# print('Use space bar for divide indexes')
# pos = input().split()
# pos = list(map(int, pos))

# sum = sum([b[i - 1] for i in pos])

# print(sum)

'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12'''

# a = [2, 3, 5, 9, 3, 7, 9, 15]
# odd_pos = [a[i] for i in range(1, len(a), 2)]
# sum_odd_pos = sum(odd_pos)
# print(a, ' -> ', odd_pos, ' sum = ', sum_odd_pos)

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

# k = int(input("Input the number ",))
# fibonacci = lambda num: num if num <= 1 else (fibonacci(num - 1) + fibonacci(num - 2))
# list_fibonacci = list(map(fibonacci, range(0, k + 1, 1)))
# list_negafibonacci = [int(list_fibonacci[i]*(-1)**(i + 1)) for i in range(k, 0, -1)]
# result = list_negafibonacci + list_fibonacci
# print(result)
