import math
import turtle
import colorsys

turtle.bgcolor("purple")
turtle.shape("turtle")
turtle.speed(0)

turtle.goto(0, -40)
turtle.pendown()
h=0
phi = 137.508 * (math.pi/180.0)
for i in range(16):
    for j in range(18):
        turtle.color("yellow")
        h+= 0.005
        turtle.rt(90)
        turtle.circle(150 - j*6, 90)
        turtle.lt(90)
        turtle.circle(150 - j*6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)

turtle.penup()
turtle.goto(0,0)
turtle.color("black")
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()

turtle.penup()
turtle.goto(0, 300)
turtle.color("white")
turtle.write("Te Quiero Mucho", align="center", font=("Arial", 24, "bold"))
# write("De mi, para mi tesoro", align="center", font=("Arial", 24, "bold"))

turtle.done()

# bgcolor("purple")
# shape("turtle")
# speed(0)

# goto(0, -40)
# pendown()
# h=0
# phi = 137.508 * (math.pi/180.0)
# for i in range(16):
#     for j in range(18):
#         color("yellow")
#         h+= 0.005
#         rt(90)
#         circle(150 - j*6, 90)
#         lt(90)
#         circle(150 - j*6, 90)
#         rt(180)
#     circle(40, 24)

# penup()
# goto(0,0)
# color("black")
# fillcolor("brown")
# begin_fill()
# circle(0)
# end_fill()

# phi = 137.508 * (math.pi / 180.0)
# for i in range(160 + 40):
#     r = 4 * math.sqrt(i)
#     theta = i * phi
#     x = r * math.cos(theta)
#     y = r * math.sin(theta)
#     penup()
#     goto(x, y)
#     setheading(i * 137.508)
#     pendown()
#     if i < 160:
#         stamp()

# penup()
# goto(0, 300)
# color("white")
# write("Te Quiero Mucho", align="center", font=("Arial", 24, "bold"))
# # write("De mi, para mi tesoro", align="center", font=("Arial", 24, "bold"))

# done()