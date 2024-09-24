# Генератор для перевода символов строки в верхний регистр
def to_uppercase(string):
    return (char.upper() for char in string)

# Пример использования
string = "привет, мир!"
uppercase_gen = to_uppercase(string)

# Вывод результата
print("Строка в верхнем регистре:", ''.join(uppercase_gen))
