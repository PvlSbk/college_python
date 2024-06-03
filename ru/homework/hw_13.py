# Задание №13 от 08.05.24 по Python
#
# 1) Зачет в олимпиаде проводится без деления на классы. Выведите фамилию и имя победителя олимпиады.
# Если таких несколько - выведите только их количество.
# Примеры:
# входные данные
# Иванов Сергей 9 90
# Сергеев Петр 10 95
# Петров Иван 11 85
# Выходные данные:
# Сергеев Петр
# Входные данные:
# Иванов Сергей 9 90
# Сергеев Петр 10 85
# Петров Иван 11 90
# Выходные данные:
# 2
#
# сделал 2 заполнения файлов входных данных, как в примерах, раскоментировать только нужный

with open('task_1.txt', 'w', encoding='utf-8') as f:  # файл входных данных примера 1
    f.write('')
with open('task_1.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 9 90\n')
    f.write('Сергеев Петр 10 95\n')
    f.write('Петров Иван 11 85\n')

with open('task_1.txt', 'w', encoding='utf-8') as f:  # файл входных данных примера 2
    f.write('')
with open('task_1.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 9 90\n')
    f.write('Сергеев Петр 10 85\n')
    f.write('Петров Иван 11 90\n')

with (open('task_1.txt', 'r', encoding='utf-8') as f):  # решение задачи
    max_score = 0
    number = 0
    winner = ''
    for line in f:
        s = line.split()
        if int(s[3]) > max_score:
            max_score = int(s[3])

with (open('task_1.txt', 'r', encoding='utf-8') as f):
    for line in f:
        s = line.split()
        if int(s[3]) == max_score:
            number += 1
            winner = (s[0], s[1])

    if number == 1:
        print(*winner)
    elif number > 1:
        print(number)

# 2) Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший
# балл среди всех участников в данном классе.
# Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.
# Выходные данные:
# Выведите три целых числа.
# Примеры:
# Входные данные:
# Иванов Сергей 9 80
# Сергеев Петр 10 82
# Петров Василий 11 82
# Васильев Андрей 9 81
# Андреев Александр 10 81
# Александров Роман 9 81
# Романов Иван 11 83
# Выходные данные:
# 80 81 82

with open('task_2.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_2.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 9 80\n')
    f.write('Сергеев Петр 10 82\n')
    f.write('Петров Василий 11 82\n')
    f.write('Васильев Андрей 9 81\n')
    f.write('Андреев Александр 10 81\n')
    f.write('Александров Роман 9 81\n')
    f.write('Романов Иван 11 83\n')

with open('task_2.txt', 'r', encoding='utf-8') as f:
    class9, class10, class11 = set(), set(), set()
    for line in f:
        s = line.split()
        if s[2] == '9':
            class9.add(s[3])
        elif s[2] == '10':
            class10.add(s[3])
        elif s[2] == '11':
            class11.add(s[3])
    sort_class9 = sorted(list(class9), reverse=True)
    sort_class10 = sorted(list(class10), reverse=True)
    sort_class11 = sorted(list(class11), reverse=True)
    print(sort_class9[1], sort_class10[1], sort_class11[1])

# 3) Результаты олимпиады подводятся без деления на классы. Победителем олимпиады становятся те, кто набрал больше всего
# баллов. Призерами олимпиады становятся участники, следующие за победителями.
# Определите наибольший балл, который набрали призеры олимпиады и количество участников олимпиады, набравших такой балл.
# Выходные данные:
# Выведите два числа: наибольший балл призера и количество участников, имеющий такой балл.
# Примеры:
# Входные данные:
# Иванов Сергей 9 92
# Сергеев Петр 10 91
# Петров Василий 11 92
# Васильев Иван 9 93
# Выходные данные:
# 92 2

with open('task_3.txt', 'w', encoding='utf-8') as f:  # файл входных данных примера
    f.write('')
with open('task_3.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 9 92\n')
    f.write('Сергеев Петр 10 91\n')
    f.write('Петров Василий 11 92\n')
    f.write('Васильев Иван 9 93\n')

with (open('task_3.txt', 'r', encoding='utf-8') as f): # решение задачи
    score = set()
    for line in f: # находим множество баллов
        s = line.split()
        score.add(s[3])
    sort_score = sorted(list(score), reverse=True)  # конвертируем множество в список, сортируем в обратном порядке
    second_max_score = sort_score[1]

with (open('task_3.txt', 'r', encoding='utf-8') as f):
    number = 0
    for line in f: # находим количество призеров
        s = line.split()
        if (s[3]) == second_max_score:
            number += 1

print(second_max_score, number)

# 4) В условиях предыдущей задачи выведите фамилию и имя участника олимпиады, набравшего наибольший балл, но не ставшего
# победителем. Если таких школьников несколько - выведите их количество.
# Примеры:
# Входные данные:
# Иванов Сергей 9 93
# Сергеев Петр 10 91
# Петров Василий 11 92
# Васильев Иван 9 93
# Выходные данные:
# Петров Василий

with open('task_4.txt', 'w', encoding='utf-8') as f:  # файл входных данных примера
    f.write('')
with open('task_4.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 9 93\n')
    f.write('Сергеев Петр 10 91\n')
    f.write('Петров Василий 11 92\n')
    f.write('Васильев Иван 9 93\n')

with (open('task_4.txt', 'r', encoding='utf-8') as f):
    score = set()
    for line in f:
        s = line.split()
        score.add(s[3])
    sort_score = sorted(list(score), reverse=True)
    second_max_score = sort_score[1]

with (open('task_4.txt', 'r', encoding='utf-8') as f):
    number = 0
    winner = ''
    for line in f:
        s = line.split()
        if (s[3]) == second_max_score:
            number += 1
            winner = (s[0], s[1])

if number == 1:
    print(*winner)
elif number > 1:
    print(number)

# 5) В олимпиаде по информатике принимало участие \(N\) человек.
# Определите школы, из которых в олимпиаде принимало участие
# больше всего участников. В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех
# участниках, а только подсчитывая число участников для каждой школы.
# Входные данные
# Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
# фамилия имя школа балл
# Фамилия и имя — текстовые строки, не содержащие пробелов.
# Школа — целое число от 1 до 99. Балл — целое число от 0 до 100.
# Выходные данные
# Выведите номера этих школ в порядке возрастания.
# Примеры:
# Входные данные:
# Иванов Сергей 14 56
# Сергеев Петр 23 74
# Петров Василий 3 99
# Васильев Андрей 3 56
# Андреев Роман 14 75
# Романов Иван 27 68
# Выходные данные:
# 3 14

with open('task_5.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_5.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 14 56\n')
    f.write('Сергеев Петр 23 74\n')
    f.write('Петров Василий 3 99\n')
    f.write('Васильев Андрей 3 56\n')
    f.write('Андреев Роман 14 75\n')
    f.write('Романов Иван 27 68\n')

with (open('task_5.txt', 'r', encoding='utf-8') as f):
    school_dict = dict()
    for line in f:
        s = line.split()
        school_dict[s[2]] = school_dict.get(s[2], 0) + 1
        school_max = 0
        for i in school_dict:
            if school_dict[i] > school_max:
                school_max = school_dict[i]
        school_max_list = []
        for i in school_dict:
            if school_dict[i] == school_max:
                school_max_list.append(int(i))
sorted_school_max_list = sorted(school_max_list)
print(*sorted_school_max_list)

# 6) В условиях предыдущей задачи определите школы, из которых в олимпиаде принимало участие меньше всего участников
# (но был хотя бы один участник).
# Выходные данные
# Выведите номера этих школ в порядке возрастания.
# Примеры:
# Входные данные:
# Иванов Сергей 14 56
# Сергеев Петр 23 74
# Петров Василий 3 99
# Васильев Андрей 3 56
# Андреев Роман 14 75
# Романов Иван 27 68
# Выходные данные:
# 23 27

with open('task_6.txt', 'w', encoding='utf-8') as f:  # файл входных данных примера
    f.write('')
with open('task_6.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 14 56\n')
    f.write('Сергеев Петр 23 74\n')
    f.write('Петров Василий 3 99\n')
    f.write('Васильев Андрей 3 56\n')
    f.write('Андреев Роман 14 75\n')
    f.write('Романов Иван 27 68\n')

with (open('task_6.txt', 'r', encoding='utf-8') as f): # решение задачи
    school_dict = dict()
    school_min = 0
    for line in f:
        s = line.split()
        school_dict[s[2]] = school_dict.get(s[2], 0) + 1
        school_min += 1
    for i in school_dict:
        if school_dict[i] < school_min:
            school_min = school_dict[i]
    school_min_list = []
    for i in school_dict:
        if school_dict[i] == school_min:
            school_min_list.append(int(i))
sorted_school_min_list = sorted(school_min_list)
print(*sorted_school_min_list)

# 7) Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
# Примеры:
# Входные данные:
# Иванов Сергей 14 56
# Сергеев Петр 23 74
# Петров Василий 3 99
# Васильев Андрей 3 56
# Андреев Роман 14 75
# Романов Иван 27 68
# Выходные данные:
# Андреев Роман 75
# Васильев Андрей 56
# Иванов Сергей 56
# Петров Василий 99
# Романов Иван 68
# Сергеев Петр 74

with open('task_7.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_7.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 14 56\n')
    f.write('Сергеев Петр 23 74\n')
    f.write('Петров Василий 3 99\n')
    f.write('Васильев Андрей 3 56\n')
    f.write('Андреев Роман 14 75\n')
    f.write('Романов Иван 27 68\n')

with (open('task_7.txt', 'r', encoding='utf-8') as f):
    student_list = []
    for line in f:
        s = line.split()
        student_list.append([s[0], s[1], s[3]])

for i in sorted(student_list):
    print(*i)

# 8) В условиях предыдущей задачи выведите в порядке возрастания номера школ, в которых есть хотя бы один победитель
# олимпиады.
# Примеры:
# Входные данные:
# Иванов Сергей 13 80
# Сергеев Петр 26 70
# Сергеев Андрей 35 80
# Петров Василий 13 80
# Иванов Роман 35 70
# Иванов Иван 26 70
# Выходные данные:
# 13 35
#
with open('task_8.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_8.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 13 80\n')
    f.write('Сергеев Петр 26 70\n')
    f.write('Сергеев Андрей 35 80\n')
    f.write('Петров Василий 13 80\n')
    f.write('Иванов Роман 35 70\n')
    f.write('Иванов Иван 26 70\n')

with (open('task_8.txt', 'r', encoding='utf-8') as f):
    max_score = 0
    for line in f:
        s = line.split()
        if int(s[3]) > max_score:
            max_score = int(s[3])
with (open('task_8.txt', 'r', encoding='utf-8') as f):
    winner_school_list = set()
    for line in f:
        s = line.split()
        if int(s[3]) == max_score:
            winner_school_list.add(s[2])
sorted_winner_school_list = sorted(list(winner_school_list))
print(*sorted_winner_school_list)

# 9) В условиях предыдущей задачи выведите в порядке возрастания номера школ, средний балл учащихся которых выше, чем
# средний балл всех участников олимпиады (то есть необходимо вычислить средний балл для каждой школы и средний балл по всем участникам).
# Примеры:
# Входные данные:
# Иванов Сергей 13 80
# Сергеев Петр 26 70
# Сергеев Андрей 35 80
# Петров Василий 13 80
# Иванов Роман 35 70
# Иванов Иван 26 70
# Выходные данные:
# 13

with open('task_9.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_9.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 13 80\n')
    f.write('Сергеев Петр 26 70\n')
    f.write('Сергеев Андрей 35 80\n')
    f.write('Петров Василий 13 80\n')
    f.write('Иванов Роман 35 70\n')
    f.write('Иванов Иван 26 70\n')

with (open('task_9.txt', 'r', encoding='utf-8') as f):
    overall_summ_school_score = 0
    count_school = 0
    for line in f:
        s = line.split()
        overall_summ_school_score += int(s[3])
        count_school += 1
overall_average_school_score = overall_summ_school_score/count_school

with (open('task_9.txt', 'r', encoding='utf-8') as f):
    school_student_count = dict()
    for line in f:
        s = line.split()
        school_student_count[s[2]] = school_student_count.get(s[2], 0) + 1

with (open('task_9.txt', 'r', encoding='utf-8') as f):
    school_summ_score = dict()
    for line in f:
        s = line.split()
        school_summ_score[s[2]] = school_summ_score.get(s[2], 0) + int(s[3])

school_list = []
for i in school_student_count:
    if school_summ_score[i]/school_student_count[i] > overall_average_school_score:
        school_list.append(int(i))
print(*sorted(school_list))

# 10)
# В условиях предыдущей задачи выведите в порядке возрастания номера школ, из которых наибольшее количество участников
# стало победителями олимпиады.
# Примеры:
# Входные данные:
# Иванов Сергей 13 70
# Сергеев Петр 13 60
# Сергеев Андрей 20 70
# Петров Василий 20 70
# Иванов Роман 70 60
# Иванов Иван 70 60
# Выходные данные:
# 20

with open('task_10.txt', 'w', encoding='utf-8') as f:
    f.write('')
with open('task_10.txt', 'a', encoding='utf-8') as f:
    f.write('Иванов Сергей 13 70\n')
    f.write('Сергеев Петр 13 60\n')
    f.write('Сергеев Андрей 20 70\n')
    f.write('Петров Василий 20 70\n')
    f.write('Иванов Роман 70 60\n')
    f.write('Иванов Иван 70 60\n')

with (open('task_10.txt', 'r', encoding='utf-8') as f):
    max_score = 0
    for line in f:
        s = line.split()
        if int(s[3]) > max_score:
            max_score = int(s[3])
with (open('task_10.txt', 'r', encoding='utf-8') as f):
    school_score_dict = dict()
    for line in f:
        s = line.split()
        if int(s[3]) == max_score:
            school_score_dict[s[2]] = school_score_dict.get(s[2], 0) + 1
winner_count = 0
for i in school_score_dict:
    if school_score_dict[i] > winner_count:
        winner_count = school_score_dict[i]
school_list = []
for i in school_score_dict:
    if school_score_dict[i] == winner_count:
        school_list.append(i)
print(*sorted(school_list))
