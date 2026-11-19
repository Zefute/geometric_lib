def area(a, b):

    """
    Возвращает площадь прямоугольника.

    :param a: длина (int/float)
    :param b: ширина (int/float)
    :return: площадь прямоугольника

    Пример вызова:
        >>> area(3, 4)
        12
    """
    
    return a * b


def perimeter(a, b):

    """
    Возвращает периметр прямоугольника.

    :param a: длина (int/float)
    :param b: ширина (int/float)
    :return: периметр прямоугольника

    Пример вызова:
        >>> perimeter(3, 4)
        14
    """

    return 2 * (a + b)