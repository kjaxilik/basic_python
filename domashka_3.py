<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, 
предусмотреть обработку ситуации деления на ноль.
"""

def delitel(*args):

    try:
        chislo1 = int(input("Введите делимое число "))
        chislo2 = int(input("Введите число делитель "))
        res = chislo1 / chislo2
        return res
    except ValueError:
        return 'Ошибка! Введите число без скобок и других символов'
    except ZeroDivisionError:
        return "Ошибка 0! Нельзя делить сумму на 0, результат бесконечность! "

    

    '''
    более простой вариант:
    if chislo2 != 0:
        return chislo1 / chislo2
    else:
        print("Ошибка! Нельзя делить на 0! Результат бесконечность! ")
    '''


print(f'result  {delitel()}')


'''
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

name = 'Иван'  # input('Введите имя')
surname = 'Иванов' # input('Введите фамилию')
b_date = '07/07/1977' # input('Введите дату рождения')
city = 'Алматы' # input('Введите город проживания')
email = 'i.ivanov@mail.ru' # input('Введите email')
phone = '+7 707 123 4567' # input('Введите теkефон')

def print_client(name, surname, b_date, city, email, phone):
    print('имя: ', name, 'фамилия: ', surname, 'дата рождения: ', b_date, 'город: ', city, 'email: ', email, 'телефон: ', phone)

print_client(name, surname, b_date, city, email, phone)

'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''

a = int(input('введите цифру a '))
b = int(input('введите цифру b '))
c = int(input('введите цифру c '))

def my_func(a, b, c):
    lst = [a, b, c]
    max1 = max(lst)
    lst.remove(max1)
    max2 = max(lst)
    
    print(max1 + max2)

my_func(a, b, c)
    



'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

x = int(input('Введите положительное число x '))
y = int(input('Введите отрицательное число y '))    
    
def my_funt(x, y):
    if y < 0:
        y = abs(y)
        for el in range(y-1):
            x= x * (x)
        return print('вывод через цикл: ', 1/x)
    elif y ==0:
        print(1)
    else:
        for el in range(y-1):
            x= x * (x)
        return print('вывод через цикл: ', x)

my_funt(x, y)

print('Вывод через **: ', x**y )



'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить 
ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
и после этого завершить программу.
'''

def summa ():
    sum_res = 0
    ex = False
    while ex == False:
        numb = input('Введите числа через пробел или введите Q чnобы остановить счетчик - ').split()

        res = 0
        for el in range(len(numb)):
            if numb[el] == 'q' or numb[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(numb[el])
        sum_res = sum_res + res
        print(f'Сумма введенных чисел: {sum_res}')
    print(f'Сумма чисел до знака Q: {sum_res}')


summa() 


'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв 
и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. 
В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(t):
    return print(t.title())

# int_func('kairat')

lat_slova = input('Введите слова на латинице ')

int_func(lat_slova)








=======
# -*- coding: utf-8 -*-
"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, 
предусмотреть обработку ситуации деления на ноль.
"""

def delitel(*args):

    try:
        chislo1 = int(input("Введите делимое число "))
        chislo2 = int(input("Введите число делитель "))
        res = chislo1 / chislo2
        return res
    except ValueError:
        return 'Ошибка! Введите число без скобок и других символов'
    except ZeroDivisionError:
        return "Ошибка 0! Нельзя делить сумму на 0, результат бесконечность! "

    

    '''
    более простой вариант:
    if chislo2 != 0:
        return chislo1 / chislo2
    else:
        print("Ошибка! Нельзя делить на 0! Результат бесконечность! ")
    '''


print(f'result  {delitel()}')


'''
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

name = 'Иван'  # input('Введите имя')
surname = 'Иванов' # input('Введите фамилию')
b_date = '07/07/1977' # input('Введите дату рождения')
city = 'Алматы' # input('Введите город проживания')
email = 'i.ivanov@mail.ru' # input('Введите email')
phone = '+7 707 123 4567' # input('Введите теkефон')

def print_client(name, surname, b_date, city, email, phone):
    print('имя: ', name, 'фамилия: ', surname, 'дата рождения: ', b_date, 'город: ', city, 'email: ', email, 'телефон: ', phone)

print_client(name, surname, b_date, city, email, phone)

'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''

a = int(input('введите цифру a '))
b = int(input('введите цифру b '))
c = int(input('введите цифру c '))

def my_func(a, b, c):
    lst = [a, b, c]
    max1 = max(lst)
    lst.remove(max1)
    max2 = max(lst)
    
    print(max1 + max2)

my_func(a, b, c)
    



'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

x = int(input('Введите положительное число x '))
y = int(input('Введите отрицательное число y '))    
    
def my_funt(x, y):
    if y < 0:
        y = abs(y)
        for el in range(y-1):
            x= x * (x)
        return print('вывод через цикл: ', 1/x)
    elif y ==0:
        print(1)
    else:
        for el in range(y-1):
            x= x * (x)
        return print('вывод через цикл: ', x)

my_funt(x, y)

print('Вывод через **: ', x**y )



'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить 
ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
и после этого завершить программу.
'''

def summa ():
    sum_res = 0
    ex = False
    while ex == False:
        numb = input('Введите числа через пробел или введите Q чnобы остановить счетчик - ').split()

        res = 0
        for el in range(len(numb)):
            if numb[el] == 'q' or numb[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(numb[el])
        sum_res = sum_res + res
        print(f'Сумма введенных чисел: {sum_res}')
    print(f'Сумма чисел до знака Q: {sum_res}')


summa() 


'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв 
и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. 
В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(t):
    return print(t.title())

# int_func('kairat')

lat_slova = input('Введите слова на латинице ')

int_func(lat_slova)








>>>>>>> 3524ff00d981e58c7ca29953261be85d488df95d
