# Инициализация словаря с произвольными элементами
my_dict = {
    "фрукт": "банан",
    "овощ": "морковь",
    "напиток": "вода"
}

# Вывод первоначального словаря
print("Первоначальный словарь:", my_dict)

# Проверка наличия элемента с ключом "фрукт" и значением "яблоко"
if my_dict.get("фрукт") != "яблоко":
    my_dict["фрукт"] = "яблоко"  # Добавляем или изменяем элемент

# Вывод измененного словаря
print("Измененный словарь:", my_dict)