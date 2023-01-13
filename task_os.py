"""Решение задач из блока "Модуль os"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""

import os
import sys
from typing import List


# 1
def get_files_from_folder(folder_path: str) -> List[str]:
    """Возвращает список файлов в папке"""

    result = next(os.walk(folder_path))[2]
    print(result)
    return result


# 2
def get_current_dir() -> str:
    """Возвращает текущую рабочую директорию"""

    result = os.getcwd()
    print(result)
    return result


# 3
def create_folder_in_current_dir(folder_name: str) -> None:
    """Создает папку в текущей директории"""

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        print(f"Папка {folder_name} успешно создана")
        return
    print(f"Операция не выполнена: папка {folder_name} уже существует")


# 4
def join_folder_and_file(folder_path: str, filename: str) -> str:
    """Возвращает склеенный путь из папки и файла"""

    result = os.path.join(folder_path, filename)
    print(result)
    return result


# 5
def load_stat_to_file(filename: str) -> None:
    """Считает сколько в каталоге python:
    - папок;
    - файлов с расширением ".py";
    - файлов с расширением ".exe";
    - всего файлов.
    Выводит статистику в файл

    Args:
        filename: имя файла, в который вывести статистику

    Returns:
        None
    """

    python_path = os.path.dirname(sys.executable)

    stat = {
        "files": 0,
        "folders": 0,
        "py_files": 0,
        "exe_files": 0,
    }

    for _, dirs, files in os.walk(python_path):
        stat["files"] += len(files)
        stat["folders"] += len(dirs)
        for file in files:
            if file.endswith(".py"):
                stat["py_files"] += 1
            elif file.endswith(".exe"):
                stat["exe_files"] += 1

    with open(filename, "w") as fout:
        for key, val in stat.items():
            fout.write(f"{key}: {val}\n")

    print("Файл успешно создан" if os.path.isfile(filename) else "Ошибка при создании файла")
