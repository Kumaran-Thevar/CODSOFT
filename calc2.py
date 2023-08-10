from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

frame = Frame(root)
frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),
    ("0", 3, 0),
    (".", 3, 1),
    ("=", 3, 2),
    ("+", 3, 3),
]

for button_text, row, column in buttons:
    button = Button(frame, text=button_text, width=5, padx=10, pady=10)
    button.grid(row=row, column=column)
    button.config(command=lambda text=button_text: button_click(text))

clear_button = Button(frame, text="C", width=5, padx=10, pady=10, command=button_clear)
clear_button.grid(row=3, column=0)

equal_button = Button(frame, text="=", width=5, padx=10, pady=10, command=button_equal)
equal_button.grid(row=3, column=2)

root.mainloop()
