fixed_num = 100

def mod100(x):
    return fixed_num/x

try:
    client_num = int(input(f'Введите целое число, на которое будет поделено число {fixed_num}: '))
except ValueError:
    print('Заданое значение не является числом!')
except ZeroDivisionError:
    print('Нельзя делить на 0!')
else:
    result = mod100(client_num)
    print(result)
finally:
    print('Завершение программы.')