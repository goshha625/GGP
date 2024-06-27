import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)

# Координаты вершин пятиконечной звезды
p1 = (400.0, 300.0)
p2 = (331, 395)
p3 = (219, 359)
p4 = (200, 241)
p5 = (330, 205)

# Рисуем линии звезды
canvas.create_line(p3, p5, p2, p4, p1, p3, fill='red', width=3)

canvas.pack()
master.mainloop()
