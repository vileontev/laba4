def mod3(x):
    if x % 3 == 0:
        print("Число", x, "делится на 3")
    else:
        print("Число", x, "НЕ делится на 3")

start_num = int(input("Введите число: "))
result = mod3(start_num)