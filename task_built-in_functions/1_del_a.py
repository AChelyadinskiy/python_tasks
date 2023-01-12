from typing import Tuple


def del_a(string: str) -> Tuple[str, int]:
    new_str = string.replace('a', '')
    return new_str, len(string) - len(new_str)


assert del_a("bcde") == ("bcde", 0)
assert del_a("abrakadabra") == ("brkdbr", 5)
assert del_a("aaaa") == ("", 4)
