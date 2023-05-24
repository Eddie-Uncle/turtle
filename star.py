import turtle

# create turtle object
star = turtle.Turtle()

# setup the window screen
window = turtle.Screen()
window.bgcolor('black')  # change the window color to black

star.speed(10)  # change the speed of the turtle to 10

colors = ['red', 'green', 'blue', 'yellow', 'purple']  # list of colors

while True:  # start infinite loop
    for i in range(5):
        star.color(colors[i % 5])  # change the turtle color
        star.forward(200 + i * 10)  # move the turtle forward by 200+10*i units
        star.right(144)  # turn the turtle to right by 144 degrees
    star.right(15)  # add a slight turn to change the starting position for the next star
