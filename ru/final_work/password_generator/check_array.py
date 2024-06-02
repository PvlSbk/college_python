import string


# Возвращает False если переданный массив не содержит латинские буквы
def check_arr_for_latin(array):
    for word in array:
        for char in word:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                return True
    return False


# Возвращает False если переданный массив не содержит латинские буквы в нижнем регистре
def check_arr_for_latin_lower(array):
    for word in array:
        for char in word:
            if 'a' <= char <= 'z':
                return True
    return False


# Возвращает False если переданный массив не содержит кириллицу
def check_arr_for_cyrillic(array):
    for word in array:
        for char in word:
            if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
                return True
    return False


# Возвращает False если переданный массив не содержит кириллицу в верхнем регистре
def check_arr_for_cyrillic_upper(array):
    for word in array:
        for char in word:
            if 'А' <= char <= 'Я':
                return True
    return False


# Возвращает False если переданный массив не содержит цифры
def check_arr_for_digits(array):
    for word in array:
        for char in word:
            if char.isdigit():
                return True
    return False


# Возвращает False если переданный массив не содержит специальных символов
def check_arr_for_special_characters(array):
    special_chars = set(string.punctuation)
    for word in array:
        for char in word:
            if char in special_chars:
                return True
    return False
