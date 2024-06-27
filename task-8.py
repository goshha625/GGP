import tkinter

def key_pressed(event):
    global start_x, start_y  

    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)

    # Проверяем нахождение круга в центральном квадрате
    x1, y1, x2, y2 = canvas.coords(oval)
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    if 200 <= center_x <= 400 and 200 <= center_y <= 400:
        canvas.itemconfig(oval, fill='green')
    else:
        canvas.itemconfig(oval, fill='red')

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')

# Инициализируем начальные координаты
start_x = 300
start_y = 300

canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
