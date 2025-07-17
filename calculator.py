from tkinter import*

# Making the Button Click functionality for numbers
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# Making the Button Click functionality for clear button
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

# Making the Button Click functionality for the (=) button
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""
   
   

cal = Tk()
cal.title("Calculator") #Title of the program
operator = ""
text_Input = StringVar()

texDisplay = Entry(cal, font=('Calisto MT', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right').grid(columnspan=4)

#All the Buttons functionality
btn7 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="7",bg="black", command=lambda:btnClick(7)).grid(row=1,column=0)

btn8 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="8",bg="black", command=lambda:btnClick(8)).grid(row=1,column=1)

btn9 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="9",bg="black", command=lambda:btnClick(9)).grid(row=1,column=2)

Division = Button(cal, padx=16,pady=16, bd=10, fg="black", font=('Calisto MT', 20, 'bold'),
              text="/",bg="white", command=lambda:btnClick("/")).grid(row=4,column=3)

#==========================================================================================

btn4 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="4",bg="black", command=lambda:btnClick(4)).grid(row=2,column=0)

btn5 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="5",bg="black", command=lambda:btnClick(5)).grid(row=2,column=1)

btn6 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="6",bg="black", command=lambda:btnClick(6)).grid(row=2,column=2)

Multiply = Button(cal, padx=16,pady=16, bd=10, fg="black", font=('Calisto MT', 20, 'bold'),
              text="x",bg="white", command=lambda:btnClick("*")).grid(row=3,column=3)

#==========================================================================================

btn1 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="1",bg="black", command=lambda:btnClick(1)).grid(row=3,column=0)

btn2 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="2",bg="black", command=lambda:btnClick(2)).grid(row=3,column=1)

btn3 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="3",bg="black", command=lambda:btnClick(3)).grid(row=3,column=2)

Subtraction = Button(cal, padx=16,pady=16, bd=10, fg="black", font=('Calisto MT', 20, 'bold'),
              text="-",bg="white", command=lambda:btnClick("-")).grid(row=2,column=3)

#==========================================================================================

btnClear = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="C",bg="Orange", command=btnClearDisplay).grid(row=4,column=0)

btn0 = Button(cal, padx=16,pady=16, bd=10, fg="white", font=('Calisto MT', 20, 'bold'),
              text="0",bg="black", command=lambda:btnClick(0)).grid(row=4,column=1)

btnEquals = Button(cal, padx=16,pady=16, bd=10, fg="black", font=('Calisto MT', 20, 'bold'),
              text="=",bg="white", command=btnEqualsInput).grid(row=4,column=2)

Addition = Button(cal, padx=16,pady=16, bd=10, fg="black", font=('Calisto MT', 20, 'bold'),
              text="+",bg="white", command=lambda:btnClick("+")).grid(row=1,column=3)

#==========================================================================================
cal.mainloop()