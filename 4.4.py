def is_lucky_ticket(ticket_number):
    # Проверяем, что количество цифр в билете - чётно
    if len(ticket_number) % 2 != 0:
        return False
    
    # Получаем цифры из номера как список целых чисел
    digits = [int(char) for char in ticket_number]

    # Разделяем список на две равные части
    half_length = len(digits) // 2
    first_half = digits[:half_length]
    second_half = digits[half_length:]

    # Сравниваем суммы двух половин
    return sum(first_half) == sum(second_half)

ticket_number = input("Введите номер билета (с четным количеством цифр): ")
if is_lucky_ticket(ticket_number):
    print("Этот билет счастливый!")
else:
    print("Этот билет не счастливый...")
