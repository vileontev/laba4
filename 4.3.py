# import datetime
# date = '02.11.2022'
# magic_date = datetime.datetime.strptime(date, "%d.%m.%Y").date() 

# def isMagic(x):
#     if x == magic_date:
#         return True
#     else:
#         return False

# try:

# # print(datetime.datetime.strptime(magic_date, "%d.%m.%Y").date())
#     client_date = input('Введите дату для магической проверки в формате дд.мм.гггг : ')
#     result = isMagic(datetime.datetime.strptime(client_date, "%d.%m.%Y").date())
# except ValueError:
#     print('Введена дата в неверном формате!')
# else:
#     print(result)
# finally:
#     print('Завершение программы.')
#     # Сделать проверку форматов в функции и создать условие Магической считается дата, в которой произведениедня и месяца равно двум последним цифрам года

def is_magical_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))

        # Получаем две последние цифры года
        year_last_two_digits = year % 100

        # Проверяем условие магической даты
        if day * month == year_last_two_digits:
            return True
        else:
            return False

    except ValueError:
        # Обработка ошибки, если ввод пользователя некорректен
        print("Ошибка: Введите дату в формате 'дд.мм.гггг'")
        return False

user_input = input("Введите дату в формате 'дд.мм.гггг': ")

if is_magical_date(user_input):
    print("Это магическая дата!")
else:
    print("Это не магическая дата.")
