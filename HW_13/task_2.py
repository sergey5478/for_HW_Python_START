"""Создайте исключение."""
import math

from task_3 import NegativeRadiusError


class Circle:
    """Высчитывает периметр и площадь."""

    def __init__(self, my_r):
        if my_r < 0:
            raise NegativeRadiusError(my_r)
        self.radius = my_r

    def circumference(self):
        """Периметр."""
        return 2 * math.pi * self.radius

    def area(self):
        """Площадь."""
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    negative_circle = Circle(5)
