def area(a, h):

    """
    Возвращает площадь треугольника через основание и высоту.

    :param a: основание (int/float)
    :param h: высота (int/float)
    :return: площадь треугольника

    Пример вызова:
        >>> area(6, 4)
        12.0
    """

    return a * h / 2


def perimeter(a, b, c):

    """
    Возвращает периметр треугольника.

    :param a: первая сторона (int/float)
    :param b: вторая сторона (int/float)
    :param c: третья сторона (int/float)
    :return: периметр треугольника

    Пример вызова:
        >>> perimeter(3, 4, 5)
        12
    """

    return a + b + c