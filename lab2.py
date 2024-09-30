# Name: AHMED, Faiz Saadat
# Student ID: 21088108
# Email: fsahmed@connect.ust.hk
import random
import turtle

t = turtle.Turtle()
t.fillcolor('white')  # default shape fill color
t.speed(50)  # increase speed of turtle, since it's painfully slow
explosionColors = ["aquamarine", "DarkGoldenrod", "green", "LightPink"]


# teleports the pen to destPos
def warp(destPos):
    t.penup()
    t.setpos(destPos)
    t.pendown()


# teleports the pen relative to its current position
def offsetPos(offset):
    penPos = t.pos()
    origPos = t.pos()
    warp([penPos[0] + offset[0], penPos[1] + offset[1]])
    return origPos


# draws a rectangle at the turtle
def drawRect(xy):
    t.begin_fill()
    for i in range(4):
        t.forward(xy[i % 2])
        t.left(90)
    t.end_fill()


# draws a circle at the pen
# function has only one line in convention with drawRect
def drawCircle(rad):
    t.begin_fill()
    t.circle(rad)
    t.end_fill()


def drawLine(startPos, endPos):
    warp(startPos)
    t.setpos(endPos)


def drawTriangle(edgeSize):
    for s in range(3):
        t.forward(edgeSize)
        t.right(120)


def drawHex(edgeSize):
    for i in range(6):
        drawTriangle(edgeSize)
        t.right(60)


def drawExplosion(diam):
    circleSpace = int(diam / 32)
    outerRad = circleSpace * 16
    origPos = offsetPos([0, -outerRad])
    colIdx = -1
    for c in range(15):
        colSuffix = c % 4
        if colSuffix == 0:
            colIdx += 1
        t.fillcolor(f"{explosionColors[colIdx]}{colSuffix + 1}")
        drawCircle(outerRad - circleSpace * c)
        offsetPos([0, circleSpace])
    t.fillcolor("white")
    warp(origPos)


# uses a matrix to draw the letters of my surname "Ahmed"
def drawWord(pointRad, word):
    word = word.upper()
    wOrigPos = t.pos()
    for c in word:
        ranColor = (random.random(), random.random(), random.random())
        t.fillcolor(ranColor)
        t.pencolor(ranColor)
        cOrigPos = offsetPos([0, -pointRad])
        for p in MATRIX_LETTERS[c]:
            warp([cOrigPos[0] + p[0] * (pointRad + 2) * 2, cOrigPos[1] + p[1] * (pointRad + 2) * 2])
            drawCircle(pointRad)
        warp(cOrigPos)
        offsetPos([(pointRad + 2) * 11, 0])
    warp(wOrigPos)
    t.pencolor("black")
    t.fillcolor("white")


USER_ACTIONS = [
    "'t': Spins the pen counterclockwise.",
    "'r': Draws a rectangle at the pen's position.",
    "'c': Draws a circle at the pen's position.",
    "'p': Changes the color of the pen",
    "'l': Draws a line to a given point from the current location of the pen",
    "'f': Changes the fill color of shapes to be drawn",
    "'g': Makes a flower of triangles given a petal size",
    "'e': Makes an explosion of circles given a diameter",
    "'a': Draws my last name 'Ahmed' at the pen's position",
]

MATRIX_LETTERS = {
    'A': ((0, 0), (0, 1), (0, 2), (0, 3), (4, 0), (4, 1), (4, 2), (4, 3), (1, 4), (2, 4), (3, 4), (1, 2), (2, 2), (3, 2)),
    'H': ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (1, 2), (2, 2), (3, 2)),
    'M': ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (1, 4), (3, 4), (2, 3), (2, 2), (2, 1)),
    'E': ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (1, 2), (2, 2), (3, 2), (1, 0), (2, 0), (3, 0), (4, 0)),
    'D': ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (1, 0), (2, 0), (3, 0), (4, 1), (4, 2), (4, 3)),
}

while True:
    for u in USER_ACTIONS:
        print(u)

    userDecision = input("What would you like to do? ")

    # A
    if userDecision == 't':
        counterAngleRot = int(input("Enter angle of counterclockwise rotation: "))
        t.left(counterAngleRot)

    # B
    elif userDecision == 'r':
        rectDim = [int(input("Enter width of rectangle: ")), int(input("Enter height of rectangle: "))]
        drawRect(rectDim)

    # C
    elif userDecision == 'c':
        drawCircle(int(input("Enter radius of circle: ")))

    # D
    elif userDecision == 'p':
        penColor = input("Enter color of pen (e.g. 'red'): ")
        t.pencolor(penColor)

    elif userDecision == 'l':
        lineXY = [int(input("Enter x-coordinate of line: ")), int(input("Enter y-coordinate of line: "))]
        drawLine(t.pos(), lineXY)

    # E
    elif userDecision == 'f':
        fillCol = input("Enter a fill color (e.g. 'red'; default value is 'white'): ")
        t.fillcolor(fillCol)

    # F
    elif userDecision == 'g':
        petalSize = int(input("Enter size of each petal: "))
        drawHex(petalSize)
        t.right(30)
        drawHex(petalSize)
        t.left(30)

    # G
    elif userDecision == 'e':
        explosionDiameter = int(input("Enter size of explosion: "))
        drawExplosion(explosionDiameter)

    # H
    elif userDecision == 'a':
        print("Drawing my surname...")
        drawWord(5, "Ahmed")
        print("Done!")

    userDecision = ''
    print('')
