from tkinter import *

###main()
window = Tk()
window.title("Calculator")
window.configure()
operator=""
text_input=StringVar()

#Entry

num = Entry(window, font="arial 20 normal",width=20, borderwidth=5, textvariable=text_input, bd=30, insertwidth=3, bg="powderblue")
num.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Definie button
#==================================================================================================================================================#
def button_click(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def button_clear():
    global operator
    operator=""
    text_input.set("")

def button_equals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

#==================================================================================================================================
#buttons

button_1 = Button(window, bg="powderblue", bd=8, font="15", text="1", padx=45, pady=20,  command=lambda:button_click(1))
button_2 = Button(window, bg="powderblue", bd=8,font="15",text="2", padx=45, pady=20,  command=lambda:button_click(2))
button_3 = Button(window, bg="powderblue", bd=8,font="15",text="3", padx=45, pady=20,  command=lambda:button_click(3))
button_4 = Button(window, bg="powderblue", bd=8,font="15",text="4", padx=45, pady=20,  command=lambda:button_click(4))
button_5 = Button(window, bg="powderblue", bd=8,font="15",text="5", padx=45, pady=20,  command=lambda:button_click(5))
button_6 = Button(window, bg="powderblue", bd=8,font="15",text="6", padx=45, pady=20,  command=lambda:button_click(6))
button_7 = Button(window, bg="powderblue", bd=8,font="15",text="7", padx=45, pady=20,  command=lambda:button_click(7))
button_8 = Button(window, bg="powderblue", bd=8,font="15",text="8", padx=45, pady=20,  command=lambda:button_click(8))
button_9 = Button(window, bg="powderblue", bd=8,font="15",text="9", padx=45, pady=20,  command=lambda:button_click(9))
button_0 = Button(window, bg="powderblue", bd=8,font="15",text="0", padx=45, pady=20,  command=lambda:button_click(0))
button_add = Button(window, bg="powderblue", bd=8,font="15",text="+", padx=45, pady=20,  command=lambda:button_click("+"))
button_equal = Button(window, bg="powderblue", bd=8,font="15",text="=", padx=174, pady=20,  command=button_equals)
button_clear = Button(window, bg="powderblue", bd=8,font="15",text="C", padx=45, pady=20,  command=button_clear)
button_sub = Button(window, bg="powderblue", bd=8,font="15",text="-", padx=45, pady=20,  command=lambda:button_click("-"))
button_multi = Button(window, bg="powderblue", bd=8,font="15",text="x", padx=45, pady=20,  command=lambda:button_click("*"))
button_div = Button(window, bg="powderblue", bd=8,font="15",text="÷", padx=45, pady=20,  command=lambda:button_click("/"
                                                                                                                     ""))


#grids

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_sub.grid(row=5, column=0)
button_multi.grid(row=5, column=1)
button_div.grid(row=5, column=2)


button_0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=4, column=2)


##loops
window.mainloop()
