import turtle as t
import random
tim = t.Turtle()
tim.pensize(20)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spiro(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(500)
        tim.setheading(tim.heading()+ size)

draw_spiro(5)
screen = t.Screen()
screen.exitonclick()
