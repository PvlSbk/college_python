#1) Два числа называются дружественными,
# если каждое из них равно сумме всех делителей второго не считая самого этого числа.
# Найдите все пары дружественных чисел на отрезке [a;b].

import random
a = random.randint(1, 1000)
b = random.randint(1, 1000)
for num1 in range(a, b+1):
    sum_divisors1 = 0
    i = 1
    while i * i <= num1:
        if num1 % i == 0:
            sum_divisors1 += i
            if i * i != num1 and i != 1:
                sum_divisors1 += num1 // i
        i += 1
    for num2 in range(num1 + 1, b + 1):
        sum_divisors2 = 0
        j = 1
        while j * j <= num2:
            if num2 % j == 0:
                sum_divisors2 += j
                if j * j != num2 and j != 1:
                    sum_divisors2 += num2 // j
            j += 1
        if sum_divisors1 == num2 and sum_divisors2 == num1:
            print(f"Found friendly pair: ({num1}, {num2})")

# 2) Натуральное число называется совершенным, если оно равно сумме всех своих делителей, не равных самому числу.
# Найдите все совершенные числа, меньшие данного натурального числа n.

n = 10000
for num in range(2, n):
    sum_of_divisors = 0
    test_num = 1
    while test_num * test_num <= num:
        if num % test_num == 0:
            if test_num * test_num == num:
                sum_of_divisors += test_num
            else:
                sum_of_divisors += test_num + (num // test_num)
        test_num += 1
    sum_of_divisors -= num
    if sum_of_divisors == num:
        print(num)

# 3) Назовем автобусный билет несчастливым, если сумма цифр его шестизначного номера делится на 13.
# Могут ли два идущих подряд билета оказаться несчастливыми?

ticket_number = 999999  # начинаем с последнего возможного номера
happy_tickets = 0
while happy_tickets < 2:
    ticket_number -= 1
    digits_sum = sum(int(digit) for digit in str(ticket_number))  # сумма цифр номера билета
    if digits_sum % 13 == 0:
        continue  # пропускаем несчастливые билеты
    print(f'Несчастливый билет: {ticket_number}')
    happy_tickets += 1

# 4) Найдите, сколько точек с целочисленными координатами попадает в круг радиуса r  с центром в точке (x,y).

x = 2
y = 3
r = 5
count = 0
for i in range(x - r, x + r + 1):
    for j in range(y - r, y + r + 1):
        if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
            count += 1
print(count)

# 5) Вывести ряд чисел: десять десяток, девять девяток, восемь восьмерок, ... , одну единицу.
# Найти сумму всех этих чисел.

total_sum = 0
number = 10
while number > 0:
    print(f'{number} {number * str(number)}')
    total_sum += number * int(str(number))
    number -= 1
print(f'Сумма всех чисел: {total_sum}')

# 6) Из натурального числа удалить заданную цифру. Число и цифру вводить с клавиатуры.

# Ввод натурального числа
number = input("Введите натуральное число: ")
while not number.isdigit():
    number = input("Введите натуральное число: ")
# Ввод цифры, которую нужно удалить
digit = input("Введите цифру для удаления: ")
while not digit.isdigit() or int(digit) < 0 or int(digit) > 9:
    digit = input("Введите одну цифру от 0 до 9: ")
# Удаление заданной цифры из числа
new_number = ""
for num in number:
    if num != digit:
        new_number += num
# Вывод результата
if new_number:
    print(f"Число после удаления цифры {digit}: {int(new_number)}")
else:
    print(f"Результат после удаления цифры {digit}: 0")

# 7) Написать программу, в которой вводятся два числа-операнда x и y и знак арифметической операции (+, –, /, *).
# Вычислить результат z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции, а также на ввод y=0 при делении.
# Организовать возможность многократных вычислений без перезагрузки программы (то есть построить цикл).
# В качестве символа прекращения вычислений принять '0'.

while True:
    x = float(input("Введите первое число x: "))
    y = float(input("Введите второе число y: "))
    operation = input("Введите операцию (+, -, /, *): ")
    if operation == '0':
        print("Программа завершена.")
        break
    if operation not in ['+', '-', '*', '/']:
        print("Неверный знак операции. Попробуйте еще раз.")
        continue
    if operation == '/' and y == 0:
        print("Ошибка: деление на ноль. Попробуйте еще раз.")
        continue
    if operation == '+':
        z = x + y
    elif operation == '-':
        z = x - y
    elif operation == '*':
        z = x * y
    elif operation == '/':
        z = x / y
    print(f"Результат операции: {x} {operation} {y} = {float(z)}")

# 8) С клавиатуры вводятся целые числа до первого числа, которое меньше двух.
# Написать программу, которая определяет сколько простых чисел было введено.
# Простые числа - это натуральные числа больше единицы, которые делятся нацело только на единицу и на себя.
# Например, число 3 простое, так как нацело делится только на 1 и 3. Число 4 сложное,
# так как нацело делится не только на 1 и 4, но также на число 2.

count_primes = 0
number = int(input("Введите целое число: "))
while number >= 2:
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        count_primes += 1
    number = int(input("Введите целое число: "))
print(f"Количество простых чисел: {count_primes}")

# 9) Гипотеза Сиракуз: возьмем любое натуральное число.
# Если оно четное - разделим его пополам, если нечетное - умножим на 3, прибавим 1 и разделим пополам.
# Повторим эти действия с вновь полученным числом. Гипотеза гласит,
# что независимо от выбора первого числа рано или поздно мы получим 1.
# Проверить гипотезу Сиракуз для всех чисел от 20 до 30.

for number in range(20, 31):
    original_number = number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
            number = number // 2
    print(f'Для числа {original_number} гипотеза верна.')

# 10) Требуется вывести на экран двумерную таблицу умножения.
# Подобное реализуется с помощью двух циклов. При этом один цикл должен быть вложен в другой.

num1 = 1
while num1 <= 10:
    num2 = 1
    while num2 <= 10:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        num2 += 1
    num1 += 1