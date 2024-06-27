import tkinter

def key_pressed(event):
    if event.keysym == "Up":
        canvas.move(oval, 0, -10)
    elif event.keysym == "Down":
        canvas.move(oval, 0, 10)
    if canvas.coords(oval)[0] == 300 and canvas.coords(oval)[1] == 300:
        canvas.itemconfig(oval, fill="green")
    else:
        canvas.itemconfig(oval, fill="red")

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="white", width=600, height=600)
oval = canvas.create_oval((300, 300), (310, 310), fill="green")
canvas.pack()
canvas.bind("<KeyPress>", key_pressed)
canvas.focus_set()
master.mainloop()