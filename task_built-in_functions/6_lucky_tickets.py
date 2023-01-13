"""Решение задачи №6 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""


def lucky_tickets_count() -> int:
    """Считает количество счастливых билетов в интервале от 000000 до 999999"""

    def is_lucky(ticket_num: int) -> bool:
        """Проверяет, является ли билет счастливым"""

        nums = [*map(int, str(ticket_num))]
        return sum(nums[:-3]) == sum(nums[-3:])

    result = sum(1 for ticket_num in range(10 ** 6) if is_lucky(ticket_num))
    print(result)
    return result


assert lucky_tickets_count() == 55252
