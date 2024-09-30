import turtle

vel = [1, 0]
pos = [-500, -500]
graphPos = [0, 0]

turtle.penup()
turtle.setpos(pos)
turtle.pendown()

while True:
    vel[1] += 0.005
    pos = [pos[0] + vel[0], pos[1] + vel[1]]

    turtle.setpos(pos)

turtle.done()
