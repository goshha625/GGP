import tkinter as tk

root = tk.Tk()
root.title("Шашки")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

cell_size = 75

for i in range(8):
    for j in range(8):
        x = j * cell_size
        y = i * cell_size

        # Рисуем доску
        if (i + j) % 2 != 0:
            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="black")

        # Рисуем шашки
        if (i + j) % 2 == 0:
            if i < 3:
                canvas.create_oval(x + cell_size // 2 - 25, y + cell_size // 2 - 25, 
                                   x + cell_size // 2 + 25, y + cell_size // 2 + 25, fill="black")
            elif i > 4:
                canvas.create_oval(x + cell_size // 2 - 25, y + cell_size // 2 - 25, 
                                   x + cell_size // 2 + 25, y + cell_size // 2 + 25, fill="white")

root.mainloop()
