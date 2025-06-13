# Создаем список чисел от 1 до 20
numbers = list(range(1, 21))

# 1. Фильтруем четные числа
filtered_even = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Увеличиваем каждое число на 10
incremented = list(map(lambda x: x + 10, filtered_even))

# 3. Сортируем по убыванию
result = sorted(incremented, reverse=True)

print(result)
