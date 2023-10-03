from turtle import Turtle, Screen
import math

g = 10

inputs = ['initial velocity(m/s)', 'throwing angle(degree)', 'abssisa of initial position', 'ordinate of initial position']  #string list for input prompt
turtle = Turtle()                                                                    # crate a turtle object
screen = Screen()                                                                    # create a screen object
input_variables = []                                                       # declaring an empty list for input variables
# prompting user for input them and saving them in the list.
for text in inputs:
    initials = int(screen.textinput(title='input', prompt=f'Enter {text}'))
    input_variables.append(initials)
# extracting inputs from the list and saving them into different variables
V = input_variables[0]
theta = input_variables[1]
Xo = input_variables[2]
Yo = input_variables[3]

Vx = V * math.cos(math.radians(theta))  # calculating x component of initial velocity
Vy = V * math.sin(math.radians(theta))  # calculating Y component of final velocity

# setting up the screen and drawing axes
screen.setup(width=1000, height=600)
turtle.color("red")
turtle.hideturtle()
turtle.penup()
turtle.goto(-500, 0)
turtle.pendown()
turtle.goto(500, 0)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.goto(0, 300)
turtle.goto(Xo, Yo)

T = (2 * Vy) / g  # calculating time of flight
R = Vx * T        # calculating total horizontal distance covered
H = Yo + (Vy ** 2) / (2 * g)  # calculating maximum height

# Drawing the trajectory of projectile
t = 0
skip_first = True
while True:
    x = Xo + Vx * t
    y = Yo + (Vy*t) - ((g*t**2)/2)
    turtle.color('green')
    turtle.shape("circle")
    turtle.shapesize(1)
    turtle.showturtle()
    turtle.goto(x, y)
    t = t + 0.1
    if skip_first:
        skip_first = False
    else:
        if y <= 0:
            break


screen.exitonclick()
# printing the calculated outputs.
print(f"Maximum height: {round(H, 2)} meter")
print(f"Horizontal distance: {round(R, 2)} meter")
print(f"Time of flight: {round(T, 2)} sec")

