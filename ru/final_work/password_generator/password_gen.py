import random

from ru.final_work.password_generator.check_array import *


def array_to_uppercase(arr):
    result_array = []

    for word in arr:
        result_array.append(word.upper())

    return result_array


def array_to_lowercase(arr):
    result_array = []

    for word in arr:
        result_array.append(word.lower())

    return result_array


def random_latin():
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def random_cyrillic():
    cyrillic_letters = [chr(i) for i in range(0x0410, 0x0450) if chr(i).isalpha()]
    return random.choice(cyrillic_letters)


def get_random_digit():
    return random.randint(0, 9)


def generate_password(password_requirements, length):
    global password
    array = []
    while len(array) < length:
        # Latin
        if password_requirements['latin_letters'] in ['Y', '1', 'y']:
            array.append(random_latin())
        # Cyrillic
        if password_requirements['cyrillic_letters'] in ['Y', '1', 'y'] and len(array) < length:
            array.append(random_cyrillic())
        # Digits
        if password_requirements['digits'] in ['Y', '1', 'y'] and len(array) < length:
            array.append(str(get_random_digit()))
        # Symbol
        if password_requirements['special_symbols'] in ['Y', '1', 'y'] and len(array) < length:
            array.append(random.choice(string.punctuation))
    if password_requirements['lower_case_only'] in ['Y', '1', 'y']:
        password = ''.join(array_to_lowercase(array))
        return password
    elif password_requirements['upper_case_only'] in ['Y', '1', 'y']:
        password = ''.join(array_to_uppercase(array))
        return password
    else:
        password = ''.join(array)
        return password
