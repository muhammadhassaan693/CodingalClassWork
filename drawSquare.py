import turtle #importing turtle libirary for drawing

#creating canvas
turtle.Screen().bgcolor("blue")

sc=turtle.Screen()
sc.setup(450,350) #set the canvas size wigth 450 hight is 350 in pixelx format

turtle.title("square by hassan")

pen=turtle.Turtle() #creating the turtle object

#drawing a square
for i in range(4):
    pen.forward(150)# moving the pen to draw a single line 100 pixles
    pen.left(90) #turning the pen 90 degeres to the left