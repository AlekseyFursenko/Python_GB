'''Вычислить число c заданной точностью d
Пример:
при $d = 0.001, π = 3.141'''

# def pi():
#     arctg_1_5 = 0
#     arctg_1_239 = 0
#     for i in range(1, 37):
#         arctg_1_5 = arctg_1_5 + (((-1)**(i - 1) * ((1/5)**(2 * i - 1))) / (2 * i - 1))
#         arctg_1_239 = arctg_1_239 + (((-1)**(i - 1) * ((1/239)**(2 * i - 1))) / (2 * i - 1))
#     pi = 16 * arctg_1_5 - 4 * arctg_1_239
#     return pi

# def roundpi(d):
#     degree = 1
#     while 1/10**(degree) > d:
#         degree += 1
#     print(str(pi())[:degree+2])

# d = float(input('Please input decimal parameter for "pi" number ',))

# roundpi(d)


'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"20" -> [2, 2, 5]'''

# from math import sqrt


# def prime_factr(n): # Решето Эратосфена
#     prm_fctr_lst = []
#     while n % 2 == 0:
#         prm_fctr_lst.append(2)
#         n = n / 2
#     for i in range(3,int(sqrt(n)) + 1, 2):
#         while n % i == 0:
#             prm_fctr_lst.append(i)
#             n = n / i
#     if n > 2:
#         prm_fctr_lst.append(int(n))
#     return prm_fctr_lst
        

# n = int(input('Input a number ',))
# print(prime_factr(n))

'''Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]'''

# def del_reptd(lst):
#     new_lst = []
#     for n in lst:
#         if lst.count(n) == 1:
#             new_lst.append(n)
    
#     return new_lst

# lst = [1, 1, 2, 4, 5, 5, 60, -89, 57, 57]

# print(del_reptd(lst))


'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:

k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

# from random import randrange


# def polynom(k):
#     with open(r'C:\Users\Master\Desktop\Python\GB_seminars\polynom.txt', 'w') as file:
        
#         koeff_list = []
#         for i in range(0, k + 1):
#             koeff_list.append(randrange(0, 101))
#         print(koeff_list)
        
#         plus = 0
#         for i in range(0, k + 1):
#             if koeff_list[i] == 0:
#                 continue
            
#             if plus > 0:
#                 file.write(' + ')
            
#             if i < k - 1:
#                 if koeff_list[i] == 1:
#                     file.write('x^')
#                     file.write(str(k - i))
#                 else:
#                     file.write(str(koeff_list[i]))
#                     file.write('*x^')
#                     file.write(str(k - i))
            
#             if i == k - 1:
#                 if koeff_list[i] == 1:
#                     file.write('x')
#                 else:
#                     file.write(str(koeff_list[i]))
#                     file.write('*x')
                
#             if i == k:
#                 if plus > 0:
#                     file.write(str(koeff_list[i]))
#                 else:
#                     file.write('0')
            
#             plus += 1
            
#         file.write(' = 0')
#     return file

# k = int(input('Input k - ',))
# polynom(k)


'''Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.'''


# # Разложение полинома на степени и коэффициенты и запись их в словарь

# def koeff_poly(poly):
#     poly = poly.replace(' = 0','')
#     poly = poly.split(' ')

#     koeff = {}
#     sign = 1
#     for i in poly:
#         if i == '+':
#             sign = 1
#             continue
        
#         if i == '-':
#             sign = -1
#             continue
        
#         if '*x^' in i:
#             index = i.find('^')
#             degree = int(i[index + 1:])
#             k = int(i[:index - 2]) * sign
#             koeff[degree] = k
        
#         elif '*x' in i:
#             index = i.find('x')
#             degree = 1
#             k = int(i[:index - 1]) * sign
#             koeff[degree] = k
        
#         else:
#             degree = 0
#             k = int(i) * sign
#             koeff[degree] = k
#     return koeff


# poly = '25*x^2 - 3*x^5 + 4*x - 6 = 0'
# poly2 = '3*x - 5 = 0'

# print(poly)
# print(poly2)

# # Создаём словари с коэффициетами многочленов
# k1 = koeff_poly(poly)
# k2 = koeff_poly(poly2)

# # складываем словари и значения коэффициентов
# summ_poly = k1.copy()

# for k, v in k2.items():
#     if summ_poly[k]:
#         summ_poly[k] += v
#     else:
#         summ_poly[k] = v

# # сортируем словарь по убыванию

# sorted_summ_tuple = sorted(summ_poly.items(), key=lambda x: x[0], reverse=True)
# summ_poly = dict(sorted_summ_tuple)

# # создаём результат суммы двух многочлениов

# new_poly = ''
# plus = 0

# for i,v in summ_poly.items():
#     if summ_poly[i]:
#         if v == 0: # исключение нулевых коэффициентов
#             continue
        
#         if plus > 0 and v > 0: # расставляем + и -
#             new_poly += ' + '
#         if v < 0:
#             new_poly += ' - '
        
#         new_poly += str(abs(v)) # добавляем значения коэффициентов и степеней
                
#         if i > 1:
#             new_poly += '*x^' + str(i)
#         elif i == 1:
#             new_poly += '*x'
                    
#         plus += 1
            
# new_poly += ' = 0'

# print('Result of sum of two above mentioned polynoms is:')
# print(new_poly)