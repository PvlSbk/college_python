# 1) Заполните массив случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.

import random
n = 10
array = [None] * n
count_zeros = 0
count_ones = 0
i = 0
while count_zeros <= count_ones:
    array[i] = random.choice([0, 1])
    if array[i] == 0:
        count_zeros += 1
    else:
        count_ones += 1
    i += 1
for j in range(i, n):
    array[j] = random.choice([0, 1])
print(array)

# 2) Проверьте, является ли данный массив возрастающим или убывающим.

arr = [3, 5, 8, 12, 13, 15, 23]
increasing = True
i = 1
while i < len(arr):
    if arr[i] <= arr[i-1]:
        increasing = False
        break
    i += 1
decreasing = True
i = 1
while i < len(arr):
    if arr[i] >= arr[i-1]:
        decreasing = False
        break
    i += 1
if increasing:
    print("Массив является возрастающим.")
elif decreasing:
    print("Массив является убывающим.")
else:
    print("Массив не является ни возрастающим, ни убывающим.")

# 3) В данном массиве найдите два наименьших элемента.

array = [8, 3, 12, 5, 1, 7]
min1 = float('inf')
min2 = float('inf')
i = 0
while i < len(array):
    if array[i] < min1:
        min2 = min1
        min1 = array[i]
    elif array[i] < min2:
        min2 = array[i]
    i += 1
print("Два наименьших элемента в массиве:", min1, min2)

# 4) В массиве заменить все числа, большие данного числа, на среднее арифметическое всех чисел массива.

array = [3, 8, 5, 2, 7, 10]
average = sum(array) / len(array)
i = 0
while i < len(array):
    if array[i] > average:
        array[i] = round(average, 2)
    i += 1
print(array)

# 5) Удалить в массиве все числа, которые повторяются более двух раз.

arr = [3, 4, 3, 5, 5, 3, 7, 8, 3, 5]
elems = []
i = 0
while i < len(arr):
    count = arr.count(arr[i])
    if count <= 2:
        elems.append(arr[i])
    i += 1
print(elems)

# 6) В данном массиве найти максимальное количество одинаковых элементов.

array = [3, 4, 3, 5, 5, 3, 7, 7, 7, 5, 5, 5]
max = 0
count = 1
current = array[0]
i = 1
while i < len(array):
    if array[i] == array[i - 1]:
        count += 1
    else:
        count = 1
    if count > max:
        max = count
        current = array[i]
    i += 1
print(f"Максимальное количество одинаковых элементов: {max} для элемента {current}")

# 7) Найдите наименьший четный элемент массива.

array = [3, 8, 5, 2, 7, 10]
min = None
i = 0
while i < len(array):
    if array[i] % 2 == 0:
        if min is None or array[i] < min:
            min = array[i]
    i += 1
if min is not None:
    print("Наименьший четный элемент в массиве:", min)
else:
    print("В массиве нет четных элементов")

# 8) Удалите в целочисленном массиве все положительные числа, которые являются палиндромами.

array = [121, 123, 131, 1331, 1441, 101, 55, 676, 787, 22, 45, 989]
i = 0
while i < len(array):
    if array[i] > 0:
        num_str = str(array[i])
        if num_str == num_str[::-1]:
            array.pop(i)
            i -= 1
    i += 1
print(array)

# 9) Найти наиболее часто встречающийся элемент в массиве целых чисел.

array = [3, 4, 3, 5, 5, 3, 7, 7, 7, 5, 5, 5]
max = 0
common = None
i = 0
while i < len(array):
    current_count = 1
    j = i + 1
    while j < len(array):
        if array[i] == array[j]:
            current_count += 1
        j += 1
    if current_count > max:
        max = current_count
        common = array[i]
    i += 1
print(f"Наиболее часто встречающийся элемент: {common} (встречается {max} раз)")

# 10) Дан массив. Найдите два соседних элемента, сумма которых минимальна.

array = [4, 2, 5, 7, 2, 9, 5]
min_sum = array[0] + array[1]
min_pair = (array[0], array[1])
i = 1
while i < len(array) - 1:
    current_sum = array[i] + array[i + 1]
    if current_sum < min_sum:
        min_sum = current_sum
        min_pair = (array[i], array[i + 1])
    i += 1
print("Два соседних элемента с минимальной суммой:", min_pair, "сумма:", min_sum)