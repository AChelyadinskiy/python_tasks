def is_digit_phone_number(num: str) -> bool:
    if '+' in num and num[0] == '+':
        num = num[1:]
    parts = num.replace('-', ' ').split()
    return all(map(str.isdigit, parts)) if parts else False


assert is_digit_phone_number("8-999-777-1111") is True
assert is_digit_phone_number("+7 999 333 2222") is True
assert is_digit_phone_number("+7 999-555-11-11") is True
assert is_digit_phone_number("+7 999+555-11-11") is False
assert is_digit_phone_number("+7 999-555-OO0-l1") is False
assert is_digit_phone_number("+") is False
