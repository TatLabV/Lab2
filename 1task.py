import random

# 1. Создаем файл data.txt и записываем 10 случайных чисел (от 1 до 100)
with open('data.txt', 'w') as file:
    for _ in range(10):  # 10 чисел
        number = random.randint(1, 100)  # случайное число от 1 до 100
        file.write(f"{number}\n")  # записываем в файл

# 2. Читаем числа из файла
numbers = []
with open('data.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))  # добавляем в список

# 3. Вычисляем сумму, среднее, максимум и минимум
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# 4. Записываем результаты в result.txt
with open('result.txt', 'w') as file:
    file.write(f"Сумма: {sum_numbers}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум: {maximum}\n")
    file.write(f"Минимум: {minimum}\n")

print("Готово!")
