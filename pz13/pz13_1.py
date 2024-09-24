# Функция для возведения элементов второго столбца в квадрат
def square_second_column(matrix):
    for row in matrix:
        row[1] = row[1] ** 2
    return matrix

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_second_column(matrix)
print("Матрица после возведения второго столбца в квадрат:")
for row in new_matrix:
    print(row)
