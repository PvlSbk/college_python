# Функция возвращает номер опции меню
def ask_action():
    action = int(input("\n Выберите необходимое действие (введите номер действия из предложенного списка):"
                       "\n 1. Создать новый пароль"
                       "\n 2. Изменить длину пароля"
                       "\n 3. Изменить сложность пароля"
                       "\n 4. Создать новый пароль не изменяя длину и сложность"
                       "\n 5. Завершить работу программы"                       
                       "\n >> "))
    return action

# Функция возвращает длину пароля, которую она запрашивает у пользователя
def ask_length():
    length = int(input("\n* * * 1 шаг - Введите необходимую длину пароля от 5 до 100: "))
    while length < 5 or length > 100:
        if length < 5:
            print("Длина пароля должна быть не меньше 5 символов, попробуйте ещё раз:")
        elif length > 20:
            print("Длина пароля должна быть не больше 100 символов")
        length = int(input("\n* * * 1 шаг - Введите необходимую длину пароля от 5 до 100, попробуйте ещё раз: "))
    return length


# Функция возвращает полученный от пользователя ответ в виде Y или 1 = ДА, N или 0 = НЕТ
def ask_question(question):
    answer = input(question + " (Y или 1 = ДА, N или 0 = НЕТ): ").strip().lower()
    while answer not in ['y', 'n', '0', '1']:
        print("Неправильный ввод, ответ должен содержать Y, N, 0 или 1, попробуйте ещё раз: ")
        answer = input(question + " (Y или 1 = ДА, N или 0 = НЕТ): ").strip().lower()
    return answer


# Функция возвращает требования к паролю, которые получает от пользователя, в виде словаря
def ask_password_requirements():
    print("\n* * * 2 шаг - необходимо выбрать сложность пароля, а именно кол-во и тип символов, "
          "которые должны в нём содержаться. * * *\n"
          "Ответ должен содержать либо Y - да, N - нет или 1 - да, 0 - нет \n")
    requirements = {'latin_letters': ask_question(
        "* * * * * \nПароль должен содержать буквы латинского алфавита? "),
        'cyrillic_letters': ask_question(
            "* * * * * \nПароль должен содержать буквы кириллического алфавита? ")
    }
    if requirements['latin_letters'] in ['N', '0'] and requirements['cyrillic_letters'] in ['N', '0']:
        requirements['lower_case_only'] = '0'
        requirements['upper_case_only'] = '0'
        pass
    else:
        requirements['upper_lower_letters'] = ask_question(
            "* * * * * \nПароль должен содержать символы верхнего и нижнего регистров? ")
        if requirements['upper_lower_letters'] == 'n' or requirements['upper_lower_letters'] == '0':
            requirements['lower_case_only'] = ask_question(
                "* * * * * \nПароль должен содержать символы только нижнего регистра? "
                "(Y или 1 = ДА, N или 0 = НЕТ)")
            if requirements['lower_case_only'] == 'n' or requirements['lower_case_only'] == '0':
                requirements['upper_case_only'] = '1'
            else:
                requirements['upper_case_only'] = '0'
        else:
            requirements['lower_case_only'] = '0'
            requirements['upper_case_only'] = '0'
    requirements['digits'] = ask_question("* * * * * \nПароль должен содержать арабские цифры от 0 до 9? "
                                          "(Y или 1 = ДА, N или 0 = НЕТ)")

    requirements['special_symbols'] = ask_question(
        "* * * * * \nПароль должен содержать специальные символы (!\"№;%:?*()_+~`@#$^&[]{}\\)?")

    if requirements['latin_letters'] in ['N', '0'] \
            and requirements['cyrillic_letters'] in ['N', '0'] \
            and requirements['digits'] in ['N', '0'] \
            and requirements['special_symbols'] in ['N', '0']:
        print("\n* * * * * \n!!! ВНИМАНИЕ Ошибка ввода: пароль должен содержать символы и/или буквы"
              "\nВернитесь к шагу №2 и попробуйте ещё раз"
              "\n* * * * *")
        return 0
    return requirements
