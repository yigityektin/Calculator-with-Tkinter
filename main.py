from tkinter import *
import math
import numpy

# from PIL import ImageTk,Image


root = Tk()
root.title("My Calculator with Tkinter")
menubar = Menu(root)

entry_bar = Entry(root, width=30, borderwidth=5, bg='#bbffff')
entry_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# img_of_square_root = ImageTk.PhotoImage(Image.open("square root.png"))


def button_click(number):
    current_variable = entry_bar.get()
    entry_bar.delete(0, END)
    entry_bar.insert(0, str(current_variable) + str(number))


def button_clear():
    entry_bar.delete(0, END)


def button_add():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "addition"
    entry_bar.delete(0, END)


def button_equal():
    second_number = entry_bar.get()
    entry_bar.delete(0, END)
    global answer

    if math1 == "addition":
        entry_bar.insert(0, fst_number + int(second_number))
    elif math1 == "subtraction":
        entry_bar.insert(0, fst_number - int(second_number))
    elif math1 == "multiplication":
        entry_bar.insert(0, fst_number * int(second_number))
    elif math1 == "division":
        entry_bar.insert(0, fst_number / int(second_number))
    elif math1 == "square root":
        entry_bar.insert(0, math.sqrt(fst_number))
    elif math1 == "log":
        entry_bar.insert(0, math.log(fst_number, 10))
    elif math1 == "ln":
        entry_bar.insert(0, numpy.log(fst_number))
    elif math1 == "power":
        entry_bar.insert(0, math.pow(fst_number, int(second_number)))
    elif math1 == "square":
        entry_bar.insert(0, math.pow(fst_number, 2))
    elif math1 == "factorial":
        entry_bar.insert(0, math.factorial(fst_number))
    elif math1 == "power on 10":
        entry_bar.insert(0, math.pow(10, fst_number))
    elif math1 == "sin":
        entry_bar.insert(0, math.sin(fst_number))
    elif math1 == "cos":
        entry_bar.insert(0, math.cos(fst_number))


def button_subtract():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "subtraction"
    entry_bar.delete(0, END)


def button_multiply():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "multiplication"
    entry_bar.delete(0, END)


def button_divide():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "division"
    entry_bar.delete(0, END)


def button_square_root():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "square root"


def button_log():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "log"


def button_ln():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "ln"


def button_pow():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "power"
    entry_bar.delete(0, END)


def button_square():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "square"


def button_factorial():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "factorial"


def button_sin():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "sin"


def button_cos():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "cos"


def button_power_on_10():
    first_number = entry_bar.get()
    global fst_number
    fst_number = int(first_number)
    global math1
    math1 = "power on 10"


##################
##################


main_menu = Menu(menubar, tearoff=0)
main_menu.add_command(label="Exit", command=root.quit)

button_0 = Button(root, text="0", padx=39, pady=20, command=lambda: button_click(0), bg='#686161', fg='#FFFFFF')
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg='#686161', fg='#FFFFFF')
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg='#686161', fg='#FFFFFF')
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg='#686161', fg='#FFFFFF')
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg='#686161', fg='#FFFFFF')
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg='#686161', fg='#FFFFFF')
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg='#686161', fg='#FFFFFF')
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg='#686161', fg='#FFFFFF')
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg='#686161', fg='#FFFFFF')
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg='#686161', fg='#FFFFFF')
button_add = Button(root, text="+", padx=38, pady=20, command=button_add, bg='#686161', fg='#FFFFFF')
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal, bg='#686161', fg='#FFFFFF')
button_clear = Button(root, text="C", padx=87, pady=20, command=button_clear, bg='#686161', fg='#FFFFFF')
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract, bg='#686161', fg='#FFFFFF')
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply, bg='#686161', fg='#FFFFFF')
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide, bg='#686161', fg='#FFFFFF')
button_square_root = Button(root, text="√", padx=47, pady=20, command=button_square_root, bg='#686161', fg='#FFFFFF')
button_log = Button(root, text="log", padx=43, pady=20, command=button_log, bg='#686161', fg='#FFFFFF')
button_ln = Button(root, text="ln", padx=46, pady=20, command=button_ln, bg='#686161', fg='#FFFFFF')
button_pow = Button(root, text="x^y", padx=40, pady=20, command=button_pow, bg='#686161', fg='#FFFFFF')
button_square = Button(root, text="x^2", padx=40, pady=20, command=button_square, bg="#686161", fg="#FFFFFF")
button_factorial = Button(root, text="n!", padx=45, pady=20, command=button_factorial, bg="#686161", fg="#FFFFFF")
button_power_on_10 = Button(root, text="10^x", padx=36, pady=20, command=button_power_on_10, bg="#686161", fg="#FFFFFF")
button_sin = Button(root, text="sin", padx=43, pady=20, command=button_sin, bg="#686161", fg="#FFFFFF")
button_cos = Button(root, text="cos", padx=40, pady=20, command=button_cos, bg="#686161", fg="#FFFFFF")

button_9.grid(row=1, column=0)
button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_square_root.grid(row=1, column=4)
button_sin.grid(row=1, column=5)
button_6.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_log.grid(row=2, column=4)
button_cos.grid(row=2, column=5)
button_3.grid(row=3, column=0)
button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_ln.grid(row=3, column=4)
button_power_on_10.grid(row=3, column=5)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_pow.grid(row=4, column=4)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_square.grid(row=5, column=4)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_factorial.grid(row=6, column=4)

root.config(menu=main_menu)
root.mainloop()
