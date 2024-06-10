import pyodbc
import datetime

server = 'DESKTOP-KT7NQ8U\\SQLEXPRESS'
database = 'clinic'

conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};\
            SERVER=' + server + ';\
            DATABASE=' + database + ';\
            Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Соединение с БД прошло успешно!")
except pyodbc.Error as ex:
    print("Ошибка соединения с БД:", ex)


def print_menu():
    print("Добро пожаловать в приёмную больницы Клиника!")
    print("Выберите вариант меню:")
    print("1. Информация о пациентах")
    print("2. Создать запись к врачу")
    print("3. Проверить запись к врачу")
    print("4. Удалить запись к врачу")
    print("5. Выход из программы")


def fetch_all_patients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")

    print("Информация о пациентах:")
    for row in cursor:
        print(row)


def check_patient_ssn(conn, ssn):
    cursor = conn.cursor()
    cursor.execute("SELECT patient_ssn FROM patients WHERE patient_ssn=?", (ssn,))
    return cursor.fetchone() is not None


def select_doctor(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT doctor_name, doctor_id FROM doctors")

    print("Врачи:")
    for row in cursor:
        print(f"Doctor ID: {row.doctor_id}, Doctor Name: {row.doctor_name}")


def select_doctor_hours(conn, doctor_id):
    cursor = conn.cursor()
    cursor.execute("SELECT doctor_name, doctor_hours_from, doctor_hours_to FROM doctors WHERE doctor_id=?",
                   (doctor_id,))
    row = cursor.fetchone()

    if row:
        print(f"Выберите врача: {row.doctor_name}")
        print(f"Часы работы: {row.doctor_hours_from} - {row.doctor_hours_to}")
    else:
        print("Врач не найден.")


def make_appointment(conn):
    ssn = input("Введите SSN пациента: ")
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id FROM patients WHERE patient_ssn = ?", (ssn,))
    row = cursor.fetchone()

    if row:
        patient_id = row.patient_id
        select_doctor(conn)
        doctor_id = input("Введите ID врача: ")
        select_doctor_hours(conn, doctor_id)

        appointment_date_str = input("Введите желаемую дату (YYYY-MM-DD): ")
        appointment_time_str = input("Введите желаемое время (HH:MM): ")
        appointment_datetime_str = f"{appointment_date_str} {appointment_time_str}"

        try:
            appointment_datetime = datetime.datetime.strptime(appointment_datetime_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Ошибка ввода. Введите дату и время строго придерживаясь формату YYYY-MM-DD HH:MM.")
            return

        room_number = input("Введите номер кабинета: ")

        cursor.execute(
            "INSERT INTO appointments (appointments_doctor, appointments_room, appointments_datetime, appointments_ssn) VALUES (?, ?, ?, ?)",
            (doctor_id, room_number, appointment_datetime, patient_id))
        conn.commit()

        print("Приём назначен на ", appointment_datetime_str, "в кабинете ", room_number)

    else:
        print("Пациент SSN", ssn, "не найден. Невозможно назначить приём у врача.")


def check_appointments(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")

    print("Назначенные приёмы:")
    for row in cursor:
        print(
            f"ID врача: {row.appointments_doctor}, кабинет: {row.appointments_room}, дата: {row.appointments_datetime}, "
            f"ID пациента: {row.appointments_ssn}")


def remove_appointment(conn):
    appointment_id = input("Введите ID приёма для удаления из базы: ")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE appointment_id=?", (appointment_id,))
    appointment = cursor.fetchone()

    if appointment:
        print("Приём найден:")
        print(
            f"Врач ID: {appointment.appointments_doctor}, кабинет: {appointment.appointments_room}, "
            f"дата: {appointment.appointments_datetime}, ID пациента: {appointment.appointments_ssn}")

        confirmation = input("Вы уверены, что хотите удалить запись? (Y/N): ")

        if confirmation.upper() == "Y":
            confirm_again = input("Пожалуйста подтвердите удаление (Y/N): ")

            if confirm_again.upper() == "Y":
                cursor.execute("DELETE FROM appointments WHERE appointment_id=?", (appointment_id,))
                conn.commit()
                print("Запись успешно удалена.")
            else:
                print("Удаление прервано. Запись не найдена.")
        else:
            print("Удаление прервано. Запись не удалена.")
    else:
        print("Запись не найдена по 1ID:", appointment_id)


def main(conn):
    while True:
        print_menu()
        choice = input("Выберите вариант меню: ")

        if choice == "1":
            fetch_all_patients(conn)
        elif choice == "2":
            make_appointment(conn)
        elif choice == "3":
            check_appointments(conn)
        elif choice == "4":
            remove_appointment(conn)
        elif choice == "5":
            print("Программа завершает свою работу! 👋")
            conn.close()
            break
        else:
            print("Ошибка ввода. Выберите подходящее значение.")


if __name__ == "__main__":
    main(conn)
