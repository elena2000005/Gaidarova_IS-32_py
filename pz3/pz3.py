# Ввод данных
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

# Проверка истинности высказывания
result = A > 0 or B < -2

# Вывод результата
print(f"Высказывание «A > 0 или B < -2» является {'истинным' if result else 'ложным'}.")