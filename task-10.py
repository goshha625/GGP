import tkinter as tk
import math

def draw_star(n, canvas):
    
    vertices = [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(1, n + 1)]

    for i in range(n):
        canvas.create_line(
            vertices[i][0] * 100 + 150, 
            vertices[i][1] * 100 + 150,
            vertices[(i + int(n/2)) % n][0] * 100 + 150, 
            vertices[(i + int(n/2)) % n][1] * 100 + 150,
            width=4,  # Увеличиваем толщину линии
            fill="red"  # Добавляем цвет
        )

# Создаем окно
root = tk.Tk()
root.title("Звезда")

# Создаем холст
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Получаем число n от пользователя
n = int(input("Введите натуральное число n>1: "))

# Рисуем звезду
draw_star(n, canvas)

root.mainloop()
