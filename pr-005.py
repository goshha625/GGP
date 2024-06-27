import tkinter

def show_key(event):
    label.config(text=f"{event.keysym}[{event.keysym_num}], {event.char}[{event.keycode}]")

master = tkinter.Tk()
label = tkinter.Label(master, text="Hello, world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()