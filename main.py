import math


class Color():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def diff(self, c):
        return math.sqrt((self.red - c.red) ** 2 + \
                         (self.green - c.green) ** 2 + \
                         (self.blue - c.blue) ** 2)


print("Enter your colour values below.")
red = int(input("Red (a value from 0 to 255): "))
green = int(input("Green (a value from 0 to 255): "))
blue = int(input("Blue (a value from 0 to 255): "))
you = Color(red, green, blue)
common = {
    "red": Color(255, 0, 0),
    "green": Color(0, 255, 0),
    "blue": Color(0, 0, 255),
    "yellow": Color(255, 255, 0),
    "cyan": Color(0, 255, 255),
    "magenta": Color(255, 0, 255),
    "white": Color(255, 255, 255),
    "black": Color(0, 0, 0)
}
closest = ""
minimum = -1
for m in common.keys():
    d = you.diff(common[m])
    if minimum < 0 or minimum > d:
        closest = m
        minimum = d
print("The closest colour to your colour is", closest)
