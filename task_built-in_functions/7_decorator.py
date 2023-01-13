"""Решение задачи №7 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""

from time import time


def func_time(func):
    """Декоратор, считает время выполнения функции и выводит результат в консоль"""

    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f"Функция {func.__name__} выполнялась {time() - start_time} сек")

    return wrapper


@func_time
def some_func():
    sum(range(10 ** 6))


some_func()
