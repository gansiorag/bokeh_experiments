import random

def get_list(num:int, field:int) -> list:
    """

    :param num: length of list
    :param field: order number - 1,2 .. 9  or 10,11..99
    :return: list
    """
    rez_list = [int(random.random()*(10**field)) for k in range(num)]
    return rez_list