from tkinter import *
from PIL import Image, ImageTk

#creating the window
w = Tk()
w.title("Image")
w.geometry("400x400") #window size width is 400 and height is 400

#open and identify tje image
upload = Image.open("cat.jpg")

#convert image into the tkinter copmatiable image
image_cat = ImageTk.PhotoImage(upload)

#add image to the tkinter label
image_label = Label(w, image = image_cat, height=250, width=250)
image_label.pack()
w.mainloop()