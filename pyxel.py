from vector import *
from pygame import Color
from pygame import Rect

class Pyxel:
    def __init__(self, x, y, color=Color("white")):
        self.x = x
        self.y = y
        self.rect = Rect(x, y, 1, 1)
        self.targetX = 0
        self.targetY = 0
        self.speed = 3.0
        self.adjustment = .30
        self.vector = Vector(self.x, self.y, self.targetX, self.targetY, self.adjustment)
        self.color = color



    def move(self):
        return None

if __name__ == "__main__":
    p = Pyxel(10, 20, Color(255, 255, 255, 255))#white pyxel

    print p
