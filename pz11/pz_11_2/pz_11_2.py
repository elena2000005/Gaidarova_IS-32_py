# Открываем файл text18-5.txt и выводим его содержимое на экран
try:
    # Попробуем открыть файл в кодировке cp1251
    with open('text18-5.txt', 'r', encoding='utf-16') as f:
        content = f.read()
        print("Содержимое файла:")
        print(content)

        # Подсчитываем количество символов
        num_symbols = len(content)
        print(f"Количество символов в тексте: {num_symbols}")

    # Преобразуем символы нижнего регистра в верхний
    upper_content = content.upper()

    # Записываем результат в новый файл
    with open('new_text18-5.txt', 'w', encoding='utf-16') as f:
        f.write(upper_content)

    print("Задача 2 выполнена: текст преобразован и записан в 'new_text18-5.txt'")

except FileNotFoundError:
    print("Файл 'text18-5.txt' не найден.")
except UnicodeDecodeError:
    print("Ошибка при чтении файла: неподдерживаемая кодировка.")
