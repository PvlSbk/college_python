#1) Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

print("Задание №1")
max_number = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    if num > max_number:
        max_number = num
print("Наибольший элемент в последовательности:", max_number)

#2) Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите индекс наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
print("Задание №2")
max_number = 0
max_index = 0
index = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    if num > max_number:
        max_number = num
        max_index = index
    index += 1
print("Индекс наибольшего элемента в последовательности:", max_index)

#3) Определите количество четных элементов в последовательности, завершающейся числом 0.

print("Задание №3")
count_even = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    if num % 2 == 0:
        count_even += 1
print("Количество четных элементов в последовательности:", count_even)

#4) Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

print("Задание №4")
count_greater = 0
prev_num = int(input("Введите число: "))
current_num = int(input("Введите число: "))
while current_num != 0:
    if current_num > prev_num:
        count_greater += 1
    prev_num = current_num
    current_num = int(input("Введите число: "))
print("Количество элементов в последовательности, которые больше предыдущего элемента:", count_greater)

# 5) Найдите количество целых чисел от a до b включительно, которые делятся на 12.

print("Задание №5")
a = int(input("Введите начало диапазона (a): "))
b = int(input("Введите конец диапазона (b): "))
count_divisible_by_12 = 0
for num in range(a, b+1):
    if num % 12 == 0:
        count_divisible_by_12 += 1
print("Количество целых чисел от", a, "до", b, "включительно, которые делятся на 12:", count_divisible_by_12)

# 6) Пользователь вводит ненулевые числа до тех пор пока не введет ноль. Найдите сумму этих чисел.

print("Задание №6")
sum_numbers = 0
while True:
    num = int(input("Введите число (введите 0 для завершения): "))
    if num == 0:
        break
    sum_numbers += num
print("Сумма введенных чисел:", sum_numbers)

# 7) Пользователь вводит ненулевые целые числа до тех пор, пока не введет ноль.
# Найдите количество четных чисел, которые он ввел.

print("Задание №7")
count_even = 0
while True:
    num = int(input("Введите целое число (введите 0 для завершения): "))
    if num == 0:
        break
    if num % 2 == 0:
        count_even += 1
print("Количество четных чисел, которые вы ввели:", count_even)

# 8) Найдите четырехзначные числа, сумма цифр которых равна 15.

print("Задание №8")
num = 1000
while num < 10000:
    sum_of_digits = sum(int(digit) for digit in str(num))
    if sum_of_digits == 15:
        print(num)
    num += 1

# 9) Найдите наибольшую цифру в данном натуральном числе.

print("Задание №9")
num = int(input("Введите целое число (введите 0 для завершения): "))
max_digit = 0
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num //= 10
print("Наибольшая цифра в числе:", max_digit)

# 10) Дано натуральное число. Найдите количество четных цифр.

print("Задание №10")
number = int(input("Введите натуральное число: "))
count_even_digits = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        count_even_digits += 1
    number //= 10
print("Количество четных цифр в числе:", count_even_digits)