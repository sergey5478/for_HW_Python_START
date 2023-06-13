"""Напишите функцию для транспонирования матрицы.."""


def transpose_matrix(matrix):
    """Находим длину и ширину матрицы, меняем местами и создаём пустую."""
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


my_matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(my_matrix))
