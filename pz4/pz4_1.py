# Ввод цены за 1 кг конфет
price_per_kg = float(input("Введите цену за 1 кг конфет: "))

# Вывод стоимости для весов от 1.2 до 2 кг
for weight in range(12, 21, 2):  # используем целые числа от 12 до 20 для веса
    cost = (weight / 10) * price_per_kg  # пересчитываем вес в кг
    print(f"Стоимость {weight / 10} кг конфет: {cost:.2f} рублей")