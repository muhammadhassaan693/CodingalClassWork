from tkinter import *
import random 

#reset the game
def reset_game():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"

    label2.config(text="player                              ")
    label4.config(text="computer")
    label5.config(text="")

#disable the buttons
def button_disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"


#creating the window
w = Tk()
w.title("Rock, paper, scissor")
w.geometry("750x300") #window size width is 750 and height is 300

#creating widget 
label1 = Label(w, text="Rock, paper, Scissor", fg="red", bg="yellow", font="normal 20 bold")
label1.pack() #putingthe lable in the window

#creating fram
fram1 = Frame(w)
fram1.pack()

label2 = Label(fram1, text="player                               ", font=10)
label3 = Label(fram1, text="vs                              ", font=10)
label4 = Label(fram1, text="computer", font=10)

label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack()

label5 = Label(w, text="result", font=20, width=15, bg="skyblue", borderwidth=2, relief="solid")
label5.pack(pady=20)

fram2 = Frame(w)
fram2.pack()

button1 = Button(fram2, text="Rock", font=10, width=7, bg="gray")
button2 = Button(fram2, text="paper", font=10, width=7, bg="white")
button3 = Button(fram2, text="scissor", font=10, width=7, bg="red")

button1.pack(side=LEFT, padx=10)
button2.pack(side=LEFT, padx=10)
button3.pack(padx=10)

button4 = Button(w, text="Reset game", font=10, bg="green", command=reset_game)
button4.pack(pady=20)


w.mainloop()
