from vector import *
from pygame import Color
from pygame import Rect

class Pyxel:
    def __init__(self, x, y, color=Color("white")):
        self.x = float(x)
        self.y = float(y)
        self.rect = Rect(self.x, self.y, 1, 1)
        self.targetX = 0
        self.targetY = 0
        self.speed = 3.0
        self.adjustment = .20
        self.direction = Vector(self.x, self.y, self.targetX, self.targetY, self.adjustment)
        self.color = color



    def move(self):
        self.x = self.x + (self.speed * self.direction.x)
        self.y = self.y + (self.speed * self.direction.y)
        self.rect.x, self.rect.y = int(self.x), int(self.y)

if __name__ == "__main__":
    p = Pyxel(10, 20, Color(255, 255, 255, 255))#white pyxel

    print p
