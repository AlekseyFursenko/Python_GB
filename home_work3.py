'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12'''

# def even_pos_sum(list):
#     sum = 0
#     for i in range(1, len(list), 2):
#         sum += list[i]
#     return sum

# list = [2, 3, 5, 9, 3, 5, 0, 5]
# print(list)
# print('Sum of list elements on even indexes is ', even_pos_sum(list))

'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# def pair_list(list):
#     pair_multplr = []
#     for i in range(0, int(len(list)/2 + 0.5)):
#         pair_multplr.append(list[i] * list[(-1 * i - 1)])
#     return pair_multplr

# list = [2, 3, 4, 5, 6]
# print('initial list ', list)
# print('new list', pair_list(list))

'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 10.01] => 0.19'''

# def diff(list):
#     max_fractial = list[0]%1
#     min_fractial = list[0]%1
#     for i in list[1:]:
#         if i%1 > max_fractial:
#             max_fractial = i%1
#         if i%1 < min_fractial:
#             min_fractial = i%1
#     return (max_fractial - min_fractial)

# list = [1.1, 1.29, 3.1, 10.01]
# print(list)
# print('Differance between max and min fractional parts of lists elements is ', round(diff(list), 2))            

'''Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# def into_binnary(n):
#     match n:
#         case 1:
#             return '1'
#         case _:
#             return str(into_binnary(int(n / 2))) + str(n % 2)
    
# n = int(input('Input the number ',))
# print(n, ' -> ', into_binnary(n))

    

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

# def list_fib_negafib(n):
#     list = [0, 1]
#     for i in range(2, n + 1):
#         list.append(list[i - 1] + list[i - 2])
#     list2 = []
#     for i in range(n, 0, -1):
#         list2.append(list[i]*(-1)**(i+1))
    
#     return list2 + list

# n = int(input("Input the number ",))
# print(list_fib_negafib(n))