"""Напишите функцию для транспонирования матрицы.."""


def transpose_matrix(matrix):
    """Транспонирование матрицы"""
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix


my_matrix = [[1, 2, 9], [4, 5, 6]]
print(transpose_matrix(my_matrix))
