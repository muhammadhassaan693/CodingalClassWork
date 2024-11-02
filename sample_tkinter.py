from tkinter import *

#creating the window
w = Tk()
w.title("sample window")
w.geometry("400x300") #window size width is 400 and height is 300

#adding some widgets or components
greeting_label = Label(text="Hello I am Hassan", fg="red", bg="yellow")
greeting_label.pack() #putingthe lable in the window

text_input = Entry(width=30)
text_input.pack()







w.mainloop()