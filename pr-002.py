import tkinter

master = tkinter.Tk()
canvas = tkinter. Canvas (master, bg="white", width=600, height=600)
for i in range(75, 601, 75):
    canvas.create_line((i, 0), (i, 600), fill="blue")
    canvas.create_line((0, i), (600, i), fill="blue")
canvas.pack()
master.mainloop()