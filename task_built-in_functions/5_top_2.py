"""Решение задачи №5 блока "Встроенные функции python"
https://online.sbis.ru/shared/disk/f16da2c9-564c-46de-a7fb-0198bcb4a18e
"""

from typing import List, Dict


def top_2(goods: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """Находит ТОП-2 самых дорогих товаров и выводит их в том же формате

    Args:
        goods: список из товаров вида {"наименование": str, "цена": int}

    Returns:
        Список из двух самых дорогих товаров
    """

    result = sorted(goods, key=lambda x: x["цена"], reverse=True)[:2]
    print(result)
    return result


test_goods = [{"наименование": "Спички", "цена": 1},
              {"наименование": "Лук", "цена": 37},
              {"наименование": "Апельсин", "цена": 25},
              {"наименование": "Соль", "цена": 18},
              ]

assert top_2(test_goods) == [{"наименование": "Лук", "цена": 37},
                             {"наименование": "Апельсин", "цена": 25},
                             ]
