class NegativeRadiusError(Exception):
    """Принимает радиус, возвращает описание."""

    def __init__(self, my_r):
        self.my_r = my_r
        super().__init__(self.my_r)

    def __str__(self):
        return f'Радиус = {self.my_r}, не может быть отрицательным.'
