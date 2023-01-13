"""Решение задачи №1 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""

from typing import Tuple


def del_a(string: str) -> Tuple[str, int]:
    """Удаляет из строки все буквы 'а' и считает количество удаленных символов"""

    new_str = string.replace('a', '')
    print(new_str, len(string) - len(new_str))
    return new_str, len(string) - len(new_str)


assert del_a("bcde") == ("bcde", 0)
assert del_a("abrakadabra") == ("brkdbr", 5)
assert del_a("aaaa") == ("", 4)
