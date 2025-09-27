num1 = input("Введите первое число: ")
if not num1.replace('.', '').isdigit():  #Проверка "это число?"
    print("Ошибка: нужно вводить числа!")
else:
    num1 = float(num1)
    num2 = input("Введите второе число: ")
    if not num2.replace('.', '').isdigit():
        print("Ошибка: нужно вводить числа!")
    else:
        num2 = float(num2)
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя!")
        else:
            print(f"Результат: {num1 / num2:.2f}")

