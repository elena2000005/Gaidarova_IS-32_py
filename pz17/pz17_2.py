import tkinter as tk
from tkinter import messagebox


def calculate_distance():
    try:
        # Получение данных из полей ввода
        V1 = float(entry_V1.get())
        V2 = float(entry_V2.get())
        S = float(entry_S.get())
        T = float(entry_T.get())

        # Суммарная скорость
        total_speed = V1 + V2

        # Общий путь, пройденный автомобилями
        total_distance = total_speed * T

        # Расстояние между автомобилями через T часов
        distance = abs(S - total_distance)

        # Вывод результата в метку и консоль
        result_label.config(text=f"Расстояние через {T} часов: {distance:.2f} км")
        print(f"Расстояние между автомобилями через {T} часов: {distance:.2f} км")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")


# Создание главного окна
root = tk.Tk()
root.title("Расчёт расстояния между автомобилями")

# Поля для ввода данных
tk.Label(root, text="Скорость первого автомобиля (км/ч):").grid(row=0, column=0, padx=10, pady=5)
entry_V1 = tk.Entry(root)
entry_V1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Скорость второго автомобиля (км/ч):").grid(row=1, column=0, padx=10, pady=5)
entry_V2 = tk.Entry(root)
entry_V2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Начальное расстояние (км):").grid(row=2, column=0, padx=10, pady=5)
entry_S = tk.Entry(root)
entry_S.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Время движения (ч):").grid(row=3, column=0, padx=10, pady=5)
entry_T = tk.Entry(root)
entry_T.grid(row=3, column=1, padx=10, pady=5)

# Кнопка для расчёта
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_distance)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Метка для вывода результата
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Запуск цикла обработки событий
root.mainloop()
