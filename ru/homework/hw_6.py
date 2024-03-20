# Задание №6 от 13.03.24 по Python
#1) Дан текст. Найти сумму имеющихся в нем цифр.

text = "Дан текст с цифрами 123 и 456"
sum_of_digits = 0
for char in text:
    if char.isdigit():
        sum_of_digits += int(char)
print(sum_of_digits)

#2) Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно.

input_string = "abracadabra"
output_string = ""
for char in input_string:
    if char == 'a':
        output_string += 'A'
    elif char == 'b':
        output_string += 'B'
    else:
        output_string += char
print(output_string)

#3) Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

input_string = "Дана строка, состоящая из слов..."
word_count = input_string.count(' ') + 1
print(f"Количество слов в строке: {word_count}")

#4) Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.

input_string = "переворачиваем строку"
words = input_string.split()
output_string = ''
for word in words:
    output_string = word + ' ' + output_string
output_string = output_string.rstrip()
print(output_string)

# 5) Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

input_string = "habcdh"
first_h_idx = input_string.find('h')
last_h_idx = input_string.rfind('h')
reversed_section = ''
inside_h = False
idx = 0
while idx < len(input_string):
    if idx == first_h_idx:
        inside_h = True
    elif idx == last_h_idx:
        inside_h = False
    if inside_h:
        reversed_section = input_string[idx] + reversed_section
    else:
        reversed_section += input_string[idx]
    idx += 1
output_string = input_string[:first_h_idx + 1] + reversed_section + input_string[last_h_idx:]
print(output_string)

#6) Определить, является ли строка палиндромом.
#Палиндром – это число, слово или фраза, одинаково читающиеся в обоих направления.

input_string = str(input())
is_palindrome = True
idx = 0
reverse_idx = len(input_string) - 1
while idx < len(input_string) and reverse_idx >= 0:
    if input_string[idx] != input_string[reverse_idx]:
        is_palindrome = False
        break
    idx += 1
    reverse_idx -= 1
if is_palindrome:
    print(f"Строка '{input_string}' - палиндром!")
else:
    print(f"Строка '{input_string}' - не палиндром.")

#7) Дана строка, состоящая из английских слов, разделенных пробелами и знаками препинания.
#Определить длину самого короткого слова.

input_string = "One two, three? four..."
min_length = float('inf')
current_length = 0
in_word = False
idx = 0
while idx < len(input_string):
    char = input_string[idx]
    if char.isalnum():
        current_length += 1
        in_word = True
    else:
        if in_word:
            min_length = min(min_length, current_length)
            current_length = 0
            in_word = False
    idx += 1
if in_word:
    min_length = min(min_length, current_length)
print(f"Длина самого короткого слова в строке '{input_string}' равна {min_length}.")

#8) Дана строка. Определите общее количество символов '+' и '-' в ней.

input_string = "++-+-+-++---"
count_plus = 0
count_minus = 0
idx = 0
while idx < len(input_string):
    if input_string[idx] == '+':
        count_plus += 1
    elif input_string[idx] == '-':
        count_minus += 1
    idx += 1
print(f"Количество символов '+' в строке: {count_plus}.")
print(f"Количество символов '-' в строке: {count_minus}.️")

# 9) Дана строка. Вывести первые три символа и последние три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.

input_string = "abcddadd"
if len(input_string) > 5:
    print("Первые три символа:", end=" ")
    for idx in range(3):
        print(input_string[idx], end=" ")
    print()
    print("Последние три символа:", end=" ")
    for idx in range(-3, 0):
        print(input_string[idx], end=" ")
else:
    print(f"Первый символ {input_string[0]} повторен {len(input_string)} раз:", end=" ")
    idx = 0
    while idx < len(input_string):
      print(input_string[0], end=" ")
      idx += 1

# 10) Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.

input_string = "abcwdefwxyz"
found_w = False
found_x = False
idx = 0
while idx < len(input_string) and (not found_w or not found_x):
    if not input_string.__contains__('w'):
        print("Символ 'w' отсутствует в строке.")
        break
    elif not input_string.__contains__('x'):
        print("Символ 'x' отсутствует в строке.")
        break
    elif input_string[idx] == 'w' and found_x == False:
        print("'w' встречается раньше!")
        print("'x' встречается позже!")
        found_w = True
        found_x = True
        break
    elif input_string[idx] == 'x' and found_w == False:
        print("'x' встречается раньше!")
        print("'w' встречается позже!")
        found_w = True
        found_x = True
        break
    idx += 1

# 11) Даны две строки. Вывести большую по длине строку столько раз, на сколько символов отличаются строки.

str1 = "Один"
str2 = "Восемь"
len_str1 = len(str1)
len_str2 = len(str2)
diff = abs(len_str1 - len_str2)
if len_str1 > len_str2:
    big_str = str1
else:
    big_str = str2
count = 0
while count < diff:
    print(big_str)
    count += 1