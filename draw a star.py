import turtle #importing turtle libirary for drawing

#creating canvas
turtle.Screen().bgcolor("white")

sc=turtle.Screen()
sc.setup(450,350) #set the canvas size wigth 450 hight is 350 in pixelx format

turtle.title("star by hassan")

pen=turtle.Turtle() #creating the turtle object

#first triangle for the star
pen.pendown()

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.penup() #moving the pen without drawing
