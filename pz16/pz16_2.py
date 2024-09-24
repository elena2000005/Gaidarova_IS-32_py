class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # вес фрукта

    def __str__(self):
        return f"Фрукт: {self.name}, Вес: {self.weight} кг"

class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color  # цвет яблока

    def __str__(self):
        return f"Фрукт: {self.name}, Вес: {self.weight} кг, Цвет: {self.color}"

class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color  # цвет апельсина

    def __str__(self):
        return f"Фрукт: {self.name}, Вес: {self.weight} кг, Цвет: {self.color}"

# Пример использования
apple = Apple("Яблоко", 0.2, "Зеленый")
orange = Orange("Апельсин", 0.3, "Оранжевый")

print(apple)
print(orange)
