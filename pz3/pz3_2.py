# Ввод трехзначного числа
card_number = int(input("Введите трехзначное число (первая цифра — масть, две последние — достоинство): "))

# Разбор числа на масть и достоинство
suit_number = card_number // 100  # первая цифра — масть
rank_number = card_number % 100   # две последние цифры — достоинство

# Определение масти
if suit_number == 1:
    suit = "пики"
elif suit_number == 2:
    suit = "трефы"
elif suit_number == 3:
    suit = "бубны"
elif suit_number == 4:
    suit = "червы"
else:
    suit = "неизвестная масть"

# Определение достоинства
if rank_number == 11:
    rank = "валет"
elif rank_number == 12:
    rank = "дама"
elif rank_number == 13:
    rank = "король"
elif rank_number == 14:
    rank = "туз"
else:
    rank = str(rank_number)  # если это число от 2 до 10

# Вывод названия карты
if 6 <= suit_number <= 9 or not (2 <= rank_number <= 14):
    print("Некорректный ввод.")
else:
    print(f"{rank} {suit}")