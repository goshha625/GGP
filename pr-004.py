from random import randint, choice
import tkinter

def draw(event):
    color = choice(["red", "blue", "green", "yellow", "orange", "purple", "brown"])
    x0 = randint(0, 600)
    y0 = randint(0, 600)
    x1 = randint(0, 600)
    y1 = randint(0, 600)
    canvas.create_oval((x0, y0), (x1, y1), fill=color)

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="white", width=600, height=600)
canvas.pack()
canvas.bind("<KeyPress>", draw)
canvas.focus_set()
master.mainloop()