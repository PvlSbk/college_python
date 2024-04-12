# 1) Создать квадратную матрицу из случайных чисел из [0, 9], на побочной диагонали которой находятся единицы.

import random
n = 5
matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
for i in range(n):
    matrix[i][n - i - 1] = 1
for row in matrix:
    print(row)

# 2) Заполнить матрицу так, чтобы сумма элементов в каждой строке была равна номеру этой строки.

import random
n = 5
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    row_sum = i
    while row_sum > 0:
        col = random.randint(0, n - 1)
        if matrix[i][col] < 9:
            matrix[i][col] += 1
            row_sum -= 1
for row in matrix:
    print(row)

# 3) Дана целочисленная матрица размера 5×5. Переставить местами 4 и 5 строку.

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
matrix[3], matrix[4] = matrix[4], matrix[3]
print("\nМатрица после перестановки 4 и 5 строк:")
for row in matrix:
    print(row)

# 4) В данной матрице найти наименьший элемент в каждой строке.

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
for i, row in enumerate(matrix):
    min_element = row[0]
    for element in row[1:]:
        if element < min_element:
            min_element = element
    print(f"Наименьший элемент в строке {i + 1}: {min_element}")

# 5) Cоздать матрицу 3 x 4, заполнить ее числами 0 и 1 так,
# чтобы в одной строке была ровно одна единица, и вывести на экран.

import random
matrix = [[0, 0, 0, 0] for _ in range(3)]
for row in matrix:
    index = random.randint(0, 3)
    row[index] = 1
for row in matrix:
    print(row)

# 6) Дана матрица. Вывести на экран все четные строки, то есть с четными номерами.

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
for i in range(0, len(matrix), 2):
    print(matrix[i])

# 7) Дана матрица. Вывести на экран все нечетные столбцы, у которых первый элемент больше последнего.

matrix = [
    [1, 2, 3, 4, 5],
    [10, 7, 8, 9, 6],
    [15, 12, 13, 14, 11],
    [16, 17, 18, 19, 20],
    [26, 22, 23, 24, 25]
]
num_cols = len(matrix[0])
for j in range(1, num_cols, 2):
    if matrix[0][j] > matrix[-1][j]:
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

# 8) Дан двухмерный массив 5×5. Найти сумму модулей отрицательных нечетных элементов.

matrix = [
    [1, -2, 3, 4, -5],
    [-6, 7, -8, 9, 10],
    [11, -12, 13, -14, 15],
    [-16, 17, -18, 19, 20],
    [21, -22, 23, 24, -25]
]
sum_negative_odd = 0
for row in matrix:
    for num in row:
        if num < 0 and num % 2 != 0:
            sum_negative_odd += abs(num)
print("Сумма модулей отрицательных нечетных элементов в массиве:")
print(sum_negative_odd)

# 9) Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.

n = 5
matrix = [[2 if i < j else 1 if i == j else 0 for j in range(n)] for i in range(n)]
for row in matrix:
    print(row)

# 10) Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.
# Пример для матрицы 3 на 4:
# . * . *
# * . * .
# . * . *

n = 3
m = 4
matrix = [["*" if (i + j) % 2 == 0 else "." for j in range(m)] for i in range(n)]
matrix[0][0] = "."
for row in matrix:
    print(' '.join(row))