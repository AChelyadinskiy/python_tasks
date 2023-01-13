"""Решение задачи №4 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""


def swap_max_min(data: list) -> None:
    """Меняет местами самый большой и самый маленький элементы списка"""

    print("Исходный список:", data)
    ind_max = data.index(max(data))
    ind_min = data.index(min(data))
    data[ind_max], data[ind_min] = data[ind_min], data[ind_max]
    print("Список после преобразования:", data)


test_data = [1, 2, 3, 4, 5]
swap_max_min(test_data)
assert test_data == [5, 2, 3, 4, 1]

test_data = [2, 10, 3, 1, 5]
swap_max_min(test_data)
assert test_data == [2, 1, 3, 10, 5]
