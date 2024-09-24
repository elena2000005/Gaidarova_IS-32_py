# Функция для генерации матрицы с заменой нечетных элементов на 0
def generate_matrix_with_zeros(rows, cols):
    return [[0 if (i * cols + j + 1) % 2 != 0 else (i * cols + j + 1)
             for j in range(cols)] for i in range(rows)]

# Пример использования
rows, cols = 3, 3
matrix = generate_matrix_with_zeros(rows, cols)

print("Матрица с заменой нечетных элементов на 0:")
for row in matrix:
    print(row)
