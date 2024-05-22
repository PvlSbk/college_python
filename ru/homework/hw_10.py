# Задание №10 от 12.04.24 по Python

# 1. Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
#вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
#Считайте четыре действительных числа и выведите результат работы этой функции.

import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
result = distance(x1, y1, x2, y2)
print(f"Расстояние между точкой ({x1}, {y1}) и точкой ({x2}, {y2}) равно {result}")

#2. Написать функцию, которая возвращает среднее арифметическое нескольких переданных ей аргументов (параметров).

def average():
    numbers = input("Введите числа, разделенные пробелом: ")
    number_list = [float(num) for num in numbers.split()]
    if len(number_list) == 0:
        return 0
    average = sum(number_list) / len(number_list)
    return average
result = average()
print(f"Среднее арифметическое введенных чисел: {result}")

# 3. Напишите функцию, находящую наименьшее из четырех данных чисел.

def find_min():
    numbers = input("Введите четыре числа, разделенные пробелом: ")
    number_list = [float(num) for num in numbers.split()]
    if len(number_list) != 4:
        print("Введите ровно четыре числа.")
        return None
    min_number = min(number_list)
    return min_number
result = find_min()
if result is not None:
    print(f"Наименьшее из введенных чисел: {result}")

# 4. Напишите "функцию голосования", возвращающую то значение (true или false),
# которое среди значений ее аргументов x, y, z встречается чаще.

def voting_function(x, y, z):
    votes = [x, y, z]
    true_count = votes.count(True)
    false_count = votes.count(False)

    if true_count > false_count:
        return True
    else:
        return False
# Пример
result = voting_function(True, False, True)
print(result)

# 5. Напишите функцию, которая проверят число простое оно или нет

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
user_number = int(input("Введите число для проверки: "))
if is_prime(user_number):
    print(f"{user_number} - простое число")
else:
    print(f"{user_number} - составное число")

# 6. Напишите функцию, которая переводит число из десятичного вида в систему счисления с основанием n (1 < n < 10)

def decimal_to_base_n():
    decimal_number = int(input("Введите число в десятичной системе: "))
    base = int(input("Введите основание системы счисления (от 2 до 9): "))
    if base < 2 or base > 9:
        return "Основание системы счисления должно быть в диапазоне от 2 до 9."
    if decimal_number == 0:
        return "0"
    converted_num = ""
    while decimal_number > 0:
        remainder = decimal_number % base
        converted_num = str(remainder) + converted_num
        decimal_number = decimal_number // base
    return converted_num

result = decimal_to_base_n()
print(f"Число в новой системе счисления: {result}")

# 7. Напишите функцию, которая подсчитывает количество гласных русских букв в строке (а, я, у, ю, о, е, ё, э, и, ы)

def count_vowels(text):
    vowels = "аяуюоеёэиы"
    count = sum(1 for char in text.lower() if char in vowels)
    return count

text = "Пример строки для подсчёта гласных букв"
vowels_count = count_vowels(text)
print(f"Количество гласных русских букв в строке: {vowels_count}")

# 8. Напишите функцию, которая проверяет, является ли строка палиндромом

def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]
user_input = input("Введите строку для проверки на палиндром: ")
if is_palindrome(user_input):
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром.")

# 9. Напишите функцию, которая принимает два списка и возвращает список,
# содержащий только уникальные элементы из обоих списков.

def unique_elements(list1, list2):
    unique_set = set(list1 + list2)
    unique_list = sorted(list(unique_set))
    return unique_list
list1 = [1, 2, 3, 3, 4]
list2 = [3, 4, 5, 6]
result = unique_elements(list1, list2)
print(result)

# 10. Проверьте, является ли число n числом Армстронга (сумма цифр числа в степени, равной количеству цифр, равна самому числу).
# Реализовать функцию

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    if armstrong_sum == number:
        return True
    else:
        return False
number = int(input("Введите число для проверки:"))
result = is_armstrong_number(number)
if result:
    print(f'{number} - это число Армстронга!')
else:
    print(f'{number} - не является числом Армстронга.')
