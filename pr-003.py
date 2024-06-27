import tkinter

master = tkinter.Tk()
canvas = tkinter. Canvas (master, bg="white", width=600, height=600)

for i in range(0, 600, 75):
    canvas.create_line((i+75, 0), (i+75, 600), fill="blue")
    canvas.create_line((0, i+75), (600, i+75), fill="blue")
    if i<225:
        color = "red"
    elif i>=375:
        color="blue"
    else:
        continue
    for j in range(0, 600, 150):
        if (i<150 and i>=75) or (i<525 and i>=450):
            canvas.create_oval((j+75, i), (j+150, i+75), fill=color)
        else:
            canvas.create_oval((j, i), (j+75, i+75), fill=color)
        
canvas.pack()
master.mainloop()