import turtle
import random

# create turtle object
spiral = turtle.Turtle()

# setup the window screen
window = turtle.Screen()
window.bgcolor('black')  # change the window color to black

spiral.speed(10)  # change the speed of the turtle to 10

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'white']  # list of colors

# initialize size
size = 10

while True:  # start infinite loop
    color = random.choice(colors)  # choose a random color
    spiral.color(color)
    spiral.forward(size)  # move the turtle forward
    spiral.right(59)  # turn the turtle to right
    size += 5  # increase the size for the next circle

turtle.done()
