import tkinter
import random

def draw(event):
    # Случайный размер круга
    radius = random.randint(20, 100)
    # Случайное положение центра круга
    x_center = random.randint(radius, 600 - radius)
    y_center = random.randint(radius, 600 - radius)

    # Рисуем круг
    canvas.create_oval(
        x_center - radius, y_center - radius,
        x_center + radius, y_center + radius,
        fill='#EE6C4D'
    )

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='#98C1D9', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
