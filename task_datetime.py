"""Решение задач из блока "Модуль datetime"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""

import calendar
from datetime import datetime, timedelta


# 1
def add_5_days() -> str:
    """Возвращает текущую дату +5 дней в формате ДД.ММ.ГГ"""

    result = (datetime.now() + timedelta(days=5)).strftime("%d.%m.%y")
    print(result)
    return result


# 2
def get_current_date() -> str:
    """Возвращает текущую дату в формате ДД.ММ.ГГГГ"""

    result = datetime.now().strftime("%d.%m.%Y")
    print(result)
    return result


# 3
def print_10_days_after_03_05_13():
    """Прибавляет к дате 03.05.13 10 дней и выводит в формате ДД.ММ.ГГГГ"""

    start_date = datetime.strptime("03.05.13", "%d.%m.%y")
    result_date = (start_date + timedelta(days=10)).strftime("%d.%m.%Y")
    print(result_date)


# 4
def print_first_day_of_current_month():
    """Выводит дату в формате ДД.ММ.ГГ, эта дата должна быть первым днем месяца"""

    print(datetime.now().replace(day=1).strftime("%d.%m.%y"))


# 5
def print_last_day_of_current_month():
    """Выводит дату в формате ДД.ММ.ГГ, эта дата должна быть последним днем месяца"""

    now = datetime.now()
    last_day = calendar.monthrange(now.year, now.month)[-1]
    print(datetime.now().replace(day=last_day).strftime("%d.%m.%y"))


# 6
def print_month_after_current_date():
    """Прибавляет к текущей дате 1 месяц и выводит в формате ДД.ММ.ГГГГ"""

    now = datetime.now()
    current_month_days = calendar.monthrange(now.year, now.month)[-1]
    print((now + timedelta(days=current_month_days)).strftime("%d.%m.%Y"))


# 7
def change_month(date: str, months: int) -> str:
    """Прибавляет/вычитает переданное кол-во месяцев к дате

    Args:
        date: исходная дата в формате ДД.ММ.ГГ
        months: количество месяцев, которое необходимо прибавить/вычесть

    Returns:
        Дата в формате ДД.ММ.ГГ через months месяцев
    """

    current_date = datetime.strptime(date, "%d.%m.%y")
    direct = 1 if months > 0 else -1
    for _ in range(abs(months)):
        current_month_days = calendar.monthrange(current_date.year, current_date.month)[-1]
        current_date += timedelta(days=current_month_days) * direct
    return current_date.strftime("%d.%m.%y")


assert change_month("12.12.12", 7) == "12.07.13"
assert change_month("01.11.10", -5) == "01.06.10"
assert change_month("28.02.10", 15) == "28.05.11"
assert change_month("31.08.15", -2) == "30.06.15"
