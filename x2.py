import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r'\b\d+(?:\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Викликаємо generator_numbers для отримання генератора чисел
    numbers_generator = func(text)
    # Підсумовуємо всі числа з генератора
    total = sum(numbers_generator)
    return total