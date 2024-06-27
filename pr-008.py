import tkinter

def key_pressed(event):
    if event.keysym == "Up":
        canvas.move(oval, 0, -10)
    elif event.keysym == "Down":
        canvas.move(oval, 0, 10)
    elif event.keysym == "Left":
        canvas.move(oval, -10, 0)
    elif event.keysym == "Right":
        canvas.move(oval, 10, 0)
    
    centre = ((canvas.coords(oval)[0] + canvas.coords(oval)[2])/2, (canvas.coords(oval)[1] + canvas.coords(oval)[3])/2)
    if (((300 - centre[0]) ** 2 + (300 - centre[1]) ** 2) ** 0.5) <= 100:
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