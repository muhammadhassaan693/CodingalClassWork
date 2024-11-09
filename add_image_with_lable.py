from tkinter import *
from PIL import Image, ImageTk

#creating the window
w = Tk()
w.title("Image")
w.geometry("1000x1000") #window size width is 1000 and height is 1000

#open and identify tje image
upload = Image.open("cat2.png")

#convert image into the tkinter copmatiable image
image_cat = ImageTk.PhotoImage(upload)

#add image to the tkinter label
image_label = Label(w, image = image_cat, height=750, width=750)
image_label.pack()
w.mainloop()