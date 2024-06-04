from ru.final_work.password_generator.ask_user import *
from ru.final_work.password_generator.password_gen import *


# read_and_print_records читает текстовый файл архив паролей
def read_and_print_records(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            if not lines:
                print("-------------------")
                print("Архив паролей пуст")
            else:
                for line in lines:
                    print("-------------------")
                    print(line.strip())
        print("-------------------")

    except FileNotFoundError:
        print("Файл не найден.")


# очищает текстовый файл архив паролей
def clear_password_archive(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("")
        print("Архив паролей успешно очищен.")
    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, укажите корректный путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка при очистке архива паролей: {str(e)}")


# Выводит на печать пароль и записывает его в текстовый файл архив паролей
def print_password(password, length):
    symbol_down = '▼' * length
    symbol_up = '▲' * length
    print(f"\n* * * 3 шаг - Получение пароля"
          f"\nВаш пароль: \n\n{symbol_down}   \n{password}\n{symbol_up}\n")
    with open('passwords_archive.txt', 'a', encoding='utf-8') as file:
        file.write(password + '\n')
    return


# Запуск программы и меню
def run():
    print("\n* * * Добро пожаловать в программу для создания случайных паролей \n"
          "* * * Следуйте инструкциям программы для получения случайного пароля необходимой длины и сложности")
    path = "passwords_archive.txt"
    action = ask_action_one_five_seven()
    while action != 1:
        if action == 1:
            break
        elif action == 5:
            print("\n Вы выбрали:"
                  "\n >> 5. Вывести архив паролей\n")
            read_and_print_records(path)
            action = ask_action_one_five_seven()
        elif action == 6:
            print("\n Вы выбрали:"
                  "\n >> 6. Очистить архив паролей\n")
            clear_password_archive(path)
            action = ask_action_one_five_seven()
        elif action == 7:
            break

    length = 5
    requirements = 0
    while action != 6:
        if action == 1:
            print("\n Вы выбрали:"
                  "\n >> 1. Создать новый пароль")
            length = ask_length()
            requirements = ask_password_requirements()
            password = generate_password(requirements, length)
            print_password(password, length)
        elif action == 2:
            print("\n Вы выбрали:"
                  "\n >> 2. Изменить длину пароля")
            length = ask_length()
            password = generate_password(requirements, length)
            print_password(password, length)
        elif action == 3:
            print("\n Вы выбрали:"
                  "\n >> 3. Изменить сложность пароля")
            requirements = ask_password_requirements()
            password = generate_password(requirements, length)
            print_password(password, length)
        elif action == 4:
            print("\n Вы выбрали:"
                  "\n >> 4. Создать новый пароль не изменяя длину и сложность")
            password = generate_password(requirements, length)
            print_password(password, length)
        elif action == 5:
            print("\n Вы выбрали:"
                  "\n >> 5. Вывести архив паролей\n")
            read_and_print_records(path)
        elif action == 6:
            print("\n Вы выбрали:"
                  "\n >> 6. Очистить архив паролей\n")
            clear_password_archive(path)
        elif action == 7:
            print("\n Вы выбрали:"
                  "\n >> 7. Завершить работу программы"
                  "\n\n Программа завершает работу!")
            break
        action = ask_action()
    return


run()
