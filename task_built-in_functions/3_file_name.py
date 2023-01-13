"""Решение задачи №3 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""


def get_file_name(path: str) -> str:
    """Выделяет имя файла(без расширения) из его полного имени"""

    result = path.split('\\')[-1].split('.')[0]
    print(result)
    return result


assert get_file_name(r"C:\development\inside\test-project_management\inside\myfile.txt") == "myfile"
assert get_file_name(r"C:\Users\ag.chelyadinskiy\PycharmProjects\pythonProject\config.ini") == "config"
