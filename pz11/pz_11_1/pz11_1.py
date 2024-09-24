# Формируем текстовый файл с числами
numbers = [-10, 23, -5, 40, -3, 17, 5, -12]
with open('numbers.txt', 'w') as f:
    f.write(' '.join(map(str, numbers)))

# Читаем файл и обрабатываем данные
with open('numbers.txt', 'r') as f:
    data = list(map(int, f.read().split()))

# Вычисляем необходимые параметры
total_elements = len(data)
sum_elements = sum(data)
min_element = min(data)
multiplied_elements = [x * min_element for x in data]

# Записываем результат в новый файл
with open('result.txt', 'w') as f:
    f.write(f"Исходные данные: {data}\n")
    f.write(f"Количество элементов: {total_elements}\n")
    f.write(f"Сумма элементов: {sum_elements}\n")
    f.write(f"Элементы, умноженные на минимальный элемент: {multiplied_elements}\n")

print("Задача 1 выполнена: данные записаны в 'result.txt'")