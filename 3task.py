import math_operations as mo  # Импортируем модуль под коротким именем

# Примеры использования функций
a = 10
b = 3

print(f"{a} + {b} = {mo.add(a, b)}")
print(f"{a} - {b} = {mo.subtract(a, b)}")
print(f"{a} * {b} = {mo.multiply(a, b)}")

try:
    print(f"{a} / {b} = {mo.divide(a, b)}")
except ValueError:
    print("Ошибка: деление на ноль!")
