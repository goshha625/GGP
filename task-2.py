import tkinter as tk

# Размеры поля
WIDTH = 600
HEIGHT = 600

# Размер клетки
CELL_SIZE = WIDTH // 8

# Создание окна
master = tk.Tk()
master.title("Шахматная доска")

# Создание холста
canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
canvas.pack()

# Рисование клеток
for row in range(8):
    for col in range(8):
        # Определение цвета клетки
        color = "white" if (row + col) % 2 == 0 else "black"

        # Рисование прямоугольника
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

master.mainloop()
