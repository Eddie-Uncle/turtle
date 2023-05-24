import turtle
import random
import time

# create turtle object
spiral = turtle.Turtle()

# setup the window screen
window = turtle.Screen()
window.bgcolor('black')  # change the window color to black

spiral.speed(10)  # change the speed of the turtle to 10

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'white']  # list of colors

# initialize size
size = 10

start_time = time.time()  # get the current time
run_time = 60  # run for 60 seconds

while time.time() - start_time < run_time:  # run until the specified amount of time has passed
    color = random.choice(colors)  # choose a random color
    spiral.color(color)
    spiral.forward(size)  # move the turtle forward
    spiral.right(59)  # turn the turtle to right
    size += 5  # increase the size for the next circle

turtle.done()
