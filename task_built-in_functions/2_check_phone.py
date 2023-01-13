"""Решение задачи №2 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""


def is_digit_phone_number(num: str) -> bool:
    """Проверяет, что номер телефона состоит только из цифр
    Номер может начинаться с «+», цифры могут быть разделены пробелами и дефисами «-»
    """

    if '+' in num and num[0] == '+':
        num = num[1:]
    parts = num.replace('-', ' ').split()
    result = all(map(str.isdigit, parts)) if parts else False
    print(f"Номер телефона {num} корректный" if result else f"Номер телефона {num} некорректный")
    return result


assert is_digit_phone_number("8-999-777-1111") is True
assert is_digit_phone_number("+7 999 333 2222") is True
assert is_digit_phone_number("+7 999-555-11-11") is True
assert is_digit_phone_number("+7 999+555-11-11") is False
assert is_digit_phone_number("+7 999-555-OO0-l1") is False
assert is_digit_phone_number("+") is False
