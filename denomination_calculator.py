from tkinter import *

#creating the window
w = Tk()
w.title("Denomination calculator")
w.geometry("600x500") #window size width is 600 and height is 500
w.config(bg="light blue")

#creating widget
lable1 = Label(text="enter total number", fg="green", bg="yellow")
text_input = Entry(width=45)

Button1= Button(text="calculate")

lable2 = Label(text="here are numbers of notes for each denomination", fg="red" , bg="yellow")

lable3 = Label(text="2000")
lable4 = Label(text="1000")
lable5 = Label(text="500")
lable6 = Label(text="100")

t1 = Entry(width=30)
t2 = Entry(width=30)
t3 = Entry(width=30)
t4 = Entry(width=30)

#placing the widget on the window
lable1.place(x=230, y=50)
text_input.place(x=200, y=80)
Button1.place(x=240, y=120)
lable2.place(x=140, y=170)

lable3.place(x=180, y=200)
t1.place(x=270, y=200)

lable4.place(x= 180, y=230)
t2.place(x=270, y=230)

lable5.place(x=180, y=260)
t3.place(x=270, y=260)

lable6.place(x=180, y=290)
t4.place(x=270, y=290)


w.mainloop()