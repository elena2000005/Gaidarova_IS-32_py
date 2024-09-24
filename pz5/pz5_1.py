# Функция для рисования горизонтальной линии
def draw_horizontal_line(length):
    print('-' * length)

# Функция для рисования вертикальной линии
def draw_vertical_line(height):
    for _ in range(height):
        print('|')

# Функция для обрамления слова рамкой
def draw_box_around_word(word):
    word_length = len(word) + 2  # длина слова + отступы для рамки
    draw_horizontal_line(word_length)  # верхняя линия
    print(f"| {word} |")  # само слово с вертикальными границами
    draw_horizontal_line(word_length)  # нижняя линия

# Пример использования
word = input("Введите слово: ")
draw_box_around_word(word)