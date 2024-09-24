# Ввод целого числа N
N = int(input("Введите целое число N (> 0): "))

# Инициализация переменных для количества цифр и их суммы
digit_count = 0
digit_sum = 0

# Обработка числа
while N > 0:
    digit = N % 10  # взятие последней цифры
    digit_sum += digit  # добавляем цифру к сумме
    digit_count += 1  # увеличиваем счетчик цифр
    N //= 10  # удаляем последнюю цифру

# Вывод результата
print(f"Количество цифр: {digit_count}")
print(f"Сумма цифр: {digit_sum}")