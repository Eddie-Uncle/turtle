import turtle

print("Running turtle - after installing sudo apt-get install python3-tk")

T = turtle.Turtle()
T.speed(0)

def square(length, angle):
    for i in range(4):
        T.forward(length)
        T.right(angle)

for x in range(10000):
    square(100, 90)
    T.right(11)
	 