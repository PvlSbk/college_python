from ru.final_work.password_generator.ask_user import *
from ru.final_work.password_generator.password_gen import *


# Выводит на печать пароль
def print_password(password, length):
    symbol_down = '▼' * length
    symbol_up = '▲' * length
    print(f"\n* * * 3 шаг - Получение пароля"
          f"\nВаш пароль: \n\n{symbol_down}   \n{password}\n{symbol_up}\n")
    return


# Запуск программы и меню
def run():
    print("\n* * * Добро пожаловать в программу для создания случайных паролей \n"
          "* * * Следуйте инструкциям программы для получения случайного пароля необходимой длины и сложности")
    length = ask_length()
    requirements = ask_password_requirements()
    password = generate_password(requirements, length)
    print_password(password, length)
    action = 0

    while action != 5:
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

        while requirements == 0:
            requirements = ask_password_requirements()
        action = ask_action()
        if action == 5:
            print("\n Вы выбрали:"
                  "\n >> 5. Завершить работу программы"
                  "\n\n Программа завершает работу!")
    return


run()
