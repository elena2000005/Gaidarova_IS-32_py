# Задаем размер
N = int(input("Введите целое число N (> 2): "))

# Инициализация списка Фибоначчи
fibonacci = [1, 1]

# Генерация первых 10 элементов
for i in range(2, 10):
    next_fib = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_fib)

# Вывод списка
print("Первые 10 элементов последовательности Фибоначчи:", fibonacci)
