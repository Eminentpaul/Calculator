from tkinter import *
from tkinter import ttk, messagebox as mgs
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image

root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.minsize(245, 240)
root.resizable(0, 0)

def on_click(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"{current}{number}")

def delete():
    entry.delete(0, END)

def plus():
    try:
        global first_num
        global operation

        operation = "plus"

        first_number = entry.get()
        first_num = float(first_number)
        entry.delete(0, END)
    except:
        pass

def minus():
    try:
        global first_num
        global operation

        operation = "minus"

        first_number = entry.get()
        first_num = float(first_number)
        entry.delete(0, END)
    except:
        pass

def times():
    try:
        global first_num
        global operation

        operation = "times"

        first_number = entry.get()
        first_num = float(first_number)
        entry.delete(0, END)
    except:
        pass

def divide():
    try:
        global first_num
        global operation

        operation = "divide"

        first_number = entry.get()
        first_num = float(first_number)
        entry.delete(0, END)
    except:
        pass

def equal_to():
    global operation
    second_number = float(entry.get())
    entry.delete(0, END)

    if operation == "plus":
        result = entry.insert(0, first_num + second_number)
        return result
    elif operation == "minus":
        result = entry.insert(0, first_num - second_number)
        return result
    elif operation == "times":
        result = entry.insert(0, first_num * second_number)
        return result
    elif operation == "divide":
        result = entry.insert(0, first_num / second_number)
        return (result)

def sqr():
    try:
        first = entry.get()
        entry.delete(0, END)

        first_num = int(first)

        result = entry.insert(0, first_num ** 0.5)
        return result
    except:
        pass

def square():
    first = entry.get()
    entry.delete(0, END)

    first_num = int(first)

    result = entry.insert(0, first_num * first_num)
    return result

def percent():
    try:
        first = entry.get()
        entry.delete(0, END)

        first_num = int(first)

        result = int(entry.insert(0, first_num / 100))
        return result
    except:
        pass

entry = ttk.Entry(root, justify="right", width=23, font=("tahoma", 12, "bold"))
entry.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

divisionImage = PhotoImage(Image.open("images/divi.png"))
squareImage = PhotoImage(file="images/square.png")
rootImage = PhotoImage(file="images/sqr.png")
perImage = PhotoImage(file="images/percentw.png")
delImage = PhotoImage(file="images/del.png")

rootbtn = ttk.Button(root, image=rootImage, command=sqr).place(x=3, y=35)
squarebtn = ttk.Button(root, image=squareImage, command=square).place(x=65, y=35)
perbtn = ttk.Button(root, image=perImage, command=percent).place(x=127, y=35)
delbtn = ttk.Button(root, text="C", width=1, command=delete).place(x=192, y=35)

btn7 = ttk.Button(root, text="7", width=1, command=lambda: on_click(7)).place(x=4, y=70)
btn8 = ttk.Button(root, text="8", width=1, command=lambda: on_click(8)).place(x=67, y=70)
btn9 = ttk.Button(root, text="9", width=1, command=lambda: on_click(9)).place(x=129, y=70)
divibtn = ttk.Button(root, text="/", width=1, command=divide).place(x=194, y=70)

btn4 = ttk.Button(root, text="4", width=1, command=lambda: on_click(4)).place(x=4, y=105)
btn5 = ttk.Button(root, text="5", width=1, command=lambda: on_click(5)).place(x=67, y=105)
btn6 = ttk.Button(root, text="6", width=1, command=lambda: on_click(6)).place(x=129, y=105)
timesbtn = ttk.Button(root, text="*", width=1, command=times).place(x=194, y=105)

btn1 = ttk.Button(root, text="1", width=1, command=lambda: on_click(1)).place(x=4, y=140)
btn2 = ttk.Button(root, text="2", width=1, command=lambda: on_click(2)).place(x=67, y=140)
btn3 = ttk.Button(root, text="3", width=1, command=lambda: on_click(3)).place(x=129, y=140)
minusbtn = ttk.Button(root, text="-", width=1, command=minus).place(x=194, y=140)

btn0 = ttk.Button(root, text="0", width=1, command=lambda: on_click(0)).place(x=4, y=175)
pointbtn = ttk.Button(root, text=".", width=1, command=lambda: on_click(".")).place(x=67, y=175)
equalbtn = ttk.Button(root, text="=", width=1, command=equal_to).place(x=129, y=175)
plusbtn = ttk.Button(root, text="+", width=1, command=plus).place(x=194, y=175)

root.mainloop()