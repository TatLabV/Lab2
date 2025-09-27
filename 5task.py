#Создаем список чисел от 1 до 20
numbers = list(range(1, 21))

#Фильтруем четные числа
filtered_even = list(filter(lambda x: x % 2 == 0, numbers))

#Увеличиваем каждое число на 10
incremented = list(map(lambda x: x + 10, filtered_even))

#Сортируем по убыванию
result = sorted(incremented, reverse=True)

print(result)

