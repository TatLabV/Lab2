def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
    """
    Возвращает результат деления a на b.
    Обрабатывает деление на ноль.
    """
    if b == 0:
        raise ValueError("Ошибка: деление на ноль!")
    return a / b
