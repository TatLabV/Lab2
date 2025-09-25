import re

# Читаем файл
with open('text.txt', 'r') as file:
    text = file.read()

# Ищем все даты в формате DD.MM.YYYY
dates = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', text)

# Преобразуем даты в формат YYYY-MM-DD
converted_dates = []
for date in dates:
    day, month, year = date
    converted_dates.append(f"{year}-{month}-{day}")

# Сохраняем результат в файл
with open('dates.txt', 'w') as file:
    for date_str in converted_dates:
        file.write(date_str + '\n')

# Сортируем даты по возрастанию
# сортируем как строки 
converted_dates.sort()

# Выводим отсортированные даты
print("Отсортированные даты:")
for date in converted_dates:
    print(date)

