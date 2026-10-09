import math


def area(r):
    """
    Вычисляет площадь круга по данному радиусу.

    Args:
        r (float): радиус круга.

    Returns:
        float: площадь круга.

    Example:
        >>> area(5)
        78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по данному радиусу.

    Args:
        r (float): радиус круга.

    Returns:
        float: длина окружности.

    Example:
        >>> perimeter(5)
        31.41592653589793
    """
    return 2 * math.pi * r

