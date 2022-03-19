from os import close
from tkinter import *
import math



root=Tk()
root.geometry("400x450")
root.title("My Calculator")
root.configure(bg="CadetBlue1")
equation=StringVar()
expression = ""


# Function to update expression
# in the text entry box
def press(num):
       
                
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")

def clearone():
        global expression
        entry_1.delete(entry_1.index("end") - 1)
        expression=str(entry_1.get())
        #equation.set("")
def square_root():
        global expression
        k=int(eval(expression))
        if k>=0:
         #equation.set(" error " )
         expression=math.sqrt(k)
        #print(math.sqrt(k))
         equation.set(str(expression))
         expression=str(entry_1.get())
        else:
           equation.set(" error ")     
        
   
        
        

equation=StringVar()

entry_1=Entry(root,justify="right",textvariable=equation,font=22)
entry_1.place(x=10,y=5,height=50,width=380)

button_1=Button(root,text="C",fg="white",bg="darksalmon",font=("Helvetica",15),command=clear)
button_1.place(x=30,y=60,height=50,width=80)

button_2=Button(root,text="(",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("("))
button_2.place(x=110,y=60,height=50,width=80)

button_3=Button(root,text=")",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(")"))
button_3.place(x=190,y=60,height=50,width=80)

button_4=Button(root,text="<",fg="white",bg="darksalmon",font=("Helvetica",15),command=clearone)
button_4.place(x=270,y=60,heigh=50,width=80)

button_5=Button(root,text="7",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(7))
button_5.place(x=30,y=120,height=50,width=80)

button_6=Button(root,text="8",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(8))
button_6.place(x=110,y=120,height=50,width=80)

button_7=Button(root,text="9",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(9))
button_7.place(x=190,y=120,height=50,width=80)

button_8=Button(root,text="x",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("*"))
button_8.place(x=270,y=120,height=50,width=80)

button_9=Button(root,text="4",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(4))
button_9.place(x=30,y=180,height=50,width=80)

button_10=Button(root,text="5",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(5))
button_10.place(x=110,y=180,height=50,width=80)

button_11=Button(root,text="6",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(6))
button_11.place(x=190,y=180,height=50,width=80)

button_12=Button(root,text="-",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("-"))
button_12.place(x=270,y=180,height=50,width=80)

button_13=Button(root,text="1",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(1))
button_13.place(x=30,y=240,height=50,width=80)

button_14=Button(root,text="2",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(2))
button_14.place(x=110,y=240,height=50,width=80)

button_15=Button(root,text="3",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(3))
button_15.place(x=190,y=240,height=50,width=80)

button_16=Button(root,text="+",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("+"))
button_16.place(x=270,y=240,height=50,width=80)

button_17=Button(root,text=".",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("."))
button_17.place(x=30,y=300,height=50,width=80)

button_18=Button(root,text="0",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(0))
button_18.place(x=110,y=300,height=50,width=80)

button_19=Button(root,text="=",fg="white",bg="darksalmon",font=("Helvetica",15),command=equalpress)
button_19.place(x=190,y=300,height=50,width=80)

button_20=Button(root,text="/",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("/"))
button_20.place(x=270,y=300,height=50,width=80)

button_21=Button(root,text="",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press(None))
button_21.place(x=30,y=360,height=50,width=80)

button_22=Button(root,text="√",fg="white",bg="darksalmon",font=("Helvetica",15),command=square_root)
button_22.place(x=110,y=360,height=50,width=80)

button_23=Button(root,text="^",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("^"))
button_23.place(x=190,y=360,height=50,width=80)

button_24=Button(root,text="//",fg="white",bg="darksalmon",font=("Helvetica",15),command=lambda: press("//"))
button_24.place(x=270,y=360,height=50,width=80)

root.mainloop()
