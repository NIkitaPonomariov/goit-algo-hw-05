def caching_fibonacci():
    cache = {}  # Створюємо порожній словник кешу

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевіряємо, чи число вже є у кеші
            return cache[n]
        else:
            # Обчислюємо число Фібоначчі за допомогою рекурсії
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result  # Зберігаємо результат у кеші
            return result

    return fibonacci