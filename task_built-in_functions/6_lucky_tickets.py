def lucky_tickets_count() -> int:
    def is_lucky(ticket_num: int) -> bool:
        nums = [*map(int, str(ticket_num))]
        return sum(nums[:-3]) == sum(nums[-3:])

    return sum(1 for ticket_num in range(10 ** 6) if is_lucky(ticket_num))


assert lucky_tickets_count() == 55252
