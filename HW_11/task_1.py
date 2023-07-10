"""Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц"""


class Matrix:
    """Сравнение, сложение и умножение"""

    def __init__(self, rows, cols):
        """Конструктор"""
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        """Печать"""
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        """Сравнение"""
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        """Сложение"""
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Matrices error.")

    def __mul__(self, other):
        """Умножение"""
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("First matrix must match.")


matrix_a = Matrix(2, 3)
matrix_a.data = [[1, 2, 3], [4, 5, 6]]
print("Матрица A:")
print(matrix_a)

matrix_b = Matrix(2, 3)
matrix_b.data = [[7, 8, 9], [10, 11, 12]]
print("Матрица B:")
print(matrix_b)

matrix_sum = matrix_a + matrix_b
print("Сумма матриц A и B:")
print(matrix_sum)

matrix_c = Matrix(3, 2)
matrix_c.data = [[1, 2], [3, 4], [5, 6]]
print("Матрица C:")
print(matrix_c)

matrix_product = matrix_a * matrix_c
print("Произведение матриц A и C:")
print(matrix_product)
