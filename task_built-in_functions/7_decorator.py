from time import time


def func_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f"Функция {func.__name__} выполнялась {time() - start_time} сек")

    return wrapper


@func_time
def some_func():
    sum(range(10 ** 6))


some_func()
