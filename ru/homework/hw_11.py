# 1) Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Вход
# 1 2 3 2 1
# Выход
# 3

def count_unique_numbers(input_list):
    unique_numbers = set(input_list)
    return len(unique_numbers)
input_numbers = [1, 2, 3, 2, 1]
result = count_unique_numbers(input_numbers)
print(f"В списке встречается {result} различных чисел.")

# 2) Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# Вход
# 1 3 2
# 4 3 2
# Выход
# 2

def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements)
list1 = [1, 3, 2]
list2 = [4, 3, 2]
result = count_common_elements(list1, list2)
print(f"Кол-во чисел, содержащихся одновременно в обоих списках: {result}.")

# 3) Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.
# Вход
# 1 3 2
# 4 3 2
# Выход
# 2 3

def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = sorted(set1.intersection(set2))
    return common_elements
list1 = [1, 3, 2]
list2 = [4, 3, 2]
result = find_common_elements(list1, list2)
print("Числа, входящие в оба списка и отсортированные по возрастанию:")
for num in result:
    print(num, end=" ")

# 4) Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
# Вход
# 1 2 3 2 3 4
# Выход
# NO
# NO
# NO
# YES
# YES
# NO

def check_previous_occurrences(sequence):
    numbers_set = set()
    for number in sequence:
        if number in numbers_set:
            print("YES")
        else:
            print("NO")
            numbers_set.add(number)
input_sequence = input("Введите последовательность чисел через пробел: ").split()
check_previous_occurrences(input_sequence)

# 5) Аня и Боря любят играть в разноцветные кубики,
# причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету.
# Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
# Для этого они занумеровали все цвета случайными числами от 0 до 108.
# На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
# В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
# Найдите три множества:
# номера цветов кубиков, которые есть в обоих наборах;
# номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори.
# Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
# Вход
# 4 3
# 0
# 1
# 10
# 9
# 1
# 3
# 0
# Выход
# 2
# 0 1
# 2
# 9 10
# 1
# 3

def find_cube_colors_intersection(N, M, Ania_colors, Borya_colors):
    Ania_set = set(Ania_colors)
    Borya_set = set(Borya_colors)

    intersection_set = Ania_set.intersection(Borya_set)
    Ania_only_set = Ania_set.difference(Borya_set)
    Borya_only_set = Borya_set.difference(Ania_set)

    print(len(intersection_set))
    print(' '.join(str(color) for color in sorted(intersection_set)))

    print(len(Ania_only_set))
    print(' '.join(str(color) for color in sorted(Ania_only_set)))

    print(len(Borya_only_set))
    print(' '.join(str(color) for color in sorted(Borya_only_set)))
N, M = input().split()
N = int(N)
M = int(M)
Ania_colors = []
for i in range(N):
    color = int(input())
    Ania_colors.append(color)
Borya_colors = []
for i in range(M):
    color = int(input())
    Borya_colors.append(color)
find_cube_colors_intersection(N, M, Ania_colors, Borya_colors)

# 6) Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Вход
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
# Выход
# 19

def count_unique_words(num_lines, lines):
    words_set = set()
    for line in lines:
        words = line.split()
        for word in words:
            words_set.add(word)
    return len(words_set)
num_lines = 4
lines = []
for _ in range(num_lines):
    line = input()
    lines.append(line)
result = count_unique_words(num_lines, lines)
print(result)


# 7) Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданныъх вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
# В первой строке задано n - максимальное число, которое мог загадать Август.
# Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.
# Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
# Вход
# 10
# 1 2 3 4 5
# YES
# 2 4 6 8 10
# NO
# HELP
# Выход
# 1 3 5

n = int(input())
possible_numbers = set(range(1, n+1))
while True:
    try:
        question = input("Август загадал натуральное число").split()
        answer = input()
        if answer == 'YES':
            possible_numbers.intersection_update(map(int, question))
        elif answer == 'NO':
            possible_numbers.difference_update(map(int, question))
        elif answer == 'HELP':
            break
    except EOFError:
        break
print(" ".join(map(str, sorted(possible_numbers))))

# 8) Август и Беатриса продолжают играть в игру, но Август начал жульничать.
# На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO,
# чтобы множество возможных задуманных чисел оставалось как можно больше.
# Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2,
# то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.
# Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел,
# то Август из вредности всегда отвечает NO. Н
# аконец, Август при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы на них,
# то есть множество возможных задуманных чисел уменьшается.
# Первая строка содержит наибольшее число, которое мог загадать Август.
# Каждая следующая строка содержит очередной вопрос Беатрисы: набор чисел, разделенных пробелами.
# Последняя строка входных данных содержит одно слово HELP.
# Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос.
# После этого выведите через пробел, в порядке возрастания, все числа, которые мог загадать Август после ответа на все вопросы Беатрисы.
#
# Вход
# 10
# 1 2 3 4 5
# 2 4 6 8 10
# HELP
# Выход
# NO
# YES
# 6 8 10

n = int(input())
possible_numbers = set(range(1, n + 1))
half = n // 2
while True:
    question = input().split()
    if question[0] == 'HELP':
        break
    if len(possible_numbers) > half:
        answer = 'YES'
        for num in question:
            if int(num) not in possible_numbers:
                answer = 'NO'
                break
    else:
        answer = 'NO'
    print(answer)
    if answer == 'YES':
        possible_numbers.intersection_update(set(map(int, question)))
    elif answer == 'NO':
        possible_numbers.difference_update(set(map(int, question)))
print(" ".join(map(str, sorted(possible_numbers))))

# 9) Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков.
# Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
# В первой строке задано количество школьников.
# Для каждого из школьников сперва записано количество языков, которое он знает,
# а затем - названия языков, по одному в строке.
# В первой строке выведите количество языков, которые знают все школьники.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. ,
# Языки нужно выводить в лексикографическом порядке, по одному на строке.
# Начиная со второй строки - список таких языков.
#
# Вход
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
# Выход
# 1
# English
# 3
# English
# Japanese
# Russian

def read_languages():
    num_students = int(input())
    all_languages = set()
    each_languages = []
    for _ in range(num_students):
        num_languages = int(input())
        languages = set()
        for _ in range(num_languages):
            language = input()
            languages.add(language)
            all_languages.add(language)
        each_languages.append(languages)
    return all_languages, each_languages
all_languages, each_languages = read_languages()
intersect_languages = set.intersection(*each_languages)
intersect_languages = sorted(intersect_languages)
union_languages = sorted(all_languages)
print(len(intersect_languages))
for lang in intersect_languages:
    print(lang)
print(len(union_languages))
for lang in union_languages:
    print(lang)

# 10) Политическая жизнь одной страны очень оживленная.
# В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку.
# Дни, когда хотя бы одна из партий объявляет забастовку, при условии,
# что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.
# i-я партия объявляет забастовки строго каждые b_i дней,
# начиная с дня с номером a_i.
# То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д.
# Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.
# В календаре страны N дней, пронумерованных, начиная с единицы.
# Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.
# В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок.
# i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.
# Вход
# 19 3
# 2 3
# 3 5
# 9 8
# Выход
# 8

def count_strikes(N, K, strike_schedule):
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    total_strikes = 0
    for day in range(1, N + 1):
        if days_of_the_week[day % 7] not in ['Saturday', 'Sunday']:
            for i in range(K):
                a_i, b_i = strike_schedule[i]
                if (day - a_i) % b_i == 0:
                    total_strikes += 1
                    break
    return total_strikes
N, K = map(int, input().split())
strike_schedule = [list(map(int, input().split())) for _ in range(K)]
print(count_strikes(N, K, strike_schedule))