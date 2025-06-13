import re

# Шаг 1: Читаем файл
with open('text.txt', 'r') as file:
    text = file.read()

# Шаг 2: Ищем все даты в формате DD.MM.YYYY
dates = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', text)

# Шаг 3: Преобразуем даты в формат YYYY-MM-DD
converted_dates = []
for date in dates:
    day, month, year = date
    converted_dates.append(f"{year}-{month}-{day}")

# Шаг 4: Сохраняем результат в файл
with open('dates.txt', 'w') as file:
    for date_str in converted_dates:
        file.write(date_str + '\n')

# Шаг 5: Сортируем даты по возрастанию
# Просто сортируем как строки - они уже в формате YYYY-MM-DD, который хорошо сортируется
converted_dates.sort()

# Выводим отсортированные даты
print("Отсортированные даты:")
for date in converted_dates:
    print(date)
