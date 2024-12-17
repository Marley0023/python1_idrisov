print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
vibor = input("Введите номер операции: ")
if vibor in ['1', '2', '3', '4']:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
    except ValueError:
        print("Введите корректные числа")
    else:
        if vibor == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif vibor == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif vibor == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif vibor == '4':
            if num2 == 0:
                print("Нельзя делить на ноль")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Введите корректный номер операции")
