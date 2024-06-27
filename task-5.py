import tkinter

def show_key(event):
    keysym = event.keysym
    char = chr(event.keycode) if event.char else ""
    keysym_num = event.keycode
    keycode = event.keycode

    # Вывод информации о нажатой клавише
    label.config(text=f"keysym: {keysym}\nchar: {char}\nkeysym_num: {keysym_num}\nkeycode: {keycode}")

master = tkinter.Tk()
label = tkinter.Label(master, text="Нажмите любую клавишу...")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
