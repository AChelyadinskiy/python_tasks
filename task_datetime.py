import calendar
from datetime import datetime, timedelta

# 1
print((datetime.now() + timedelta(days=5)).strftime("%d.%m.%y"))

# 2
print(datetime.now().strftime("%d.%m.%Y"))

# 3
result_date = datetime.strptime("03.05.13", "%d.%m.%y") + timedelta(days=10)
print(result_date.strftime("%d.%m.%Y"))

# 4
print(datetime.now().replace(day=1).strftime("%d.%m.%y"))

# 5
now = datetime.now()
last_day = calendar.monthrange(now.year, now.month)[-1]
print(datetime.now().replace(day=last_day).strftime("%d.%m.%y"))

# 6
now = datetime.now()
current_month_days = calendar.monthrange(now.year, now.month)[-1]
print((now + timedelta(days=current_month_days)).strftime("%d.%m.%Y"))


# 7
def change_month(date, months):
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
