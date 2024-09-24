# Ввод строки и числа K
sentence = input("Введите строку-предложение на русском языке: ")
K = int(input("Введите число K (0 < K < 10): "))

# Русский алфавит без 'ё'
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
upper_alphabet = alphabet.upper()

# Функция для шифрования
def encrypt_char(char, K):
    if char in alphabet:
        return alphabet[(alphabet.index(char) + K) % len(alphabet)]
    elif char in upper_alphabet:
        return upper_alphabet[(upper_alphabet.index(char) + K) % len(upper_alphabet)]
    else:
        return char  # не изменяем символы, которые не являются буквами

# Шифруем строку
encrypted_sentence = ''.join(encrypt_char(char, K) for char in sentence)

# Вывод результата
print("Зашифрованная строка:", encrypted_sentence)