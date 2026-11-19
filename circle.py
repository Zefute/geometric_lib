import math


def area(r):

    """
    Возвращает площадь круга.

    :param r: радиус круга (int/float)
    :return: площадь круга

    Пример вызова:
        >>> area(2)
        12.566370614359172
    """

    return math.pi * r * r


def perimeter(r):

    """
    Возвращает длину окружности (периметр круга).

    :param r: радиус круга (int/float)
    :return: длина окружности

    Пример вызова:
        >>> perimeter(2)
        12.566370614359172
    """

    return 2 * math.pi * r
