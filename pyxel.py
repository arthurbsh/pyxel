from vector import *
from pygame import Color
from pygame import Rect

def mathModule(x):
    if(x < 0):
        return -x
    return x

class Pyxel:
    def __init__(self, x, y, color=Color("white"), defaultX=0, defaultY=0):
        self.iX = x
        self.iY = y
        self.dX = defaultX
        self.dY = defaultY
        #print "defaults set to:", self.dX, self.dY
        self.x = float(x)
        self.y = float(y)
        self.rect = Rect(self.x, self.y, 10, 10)
        self.targetX = -1
        self.targetY = -1
        self.speed = 20.0
        self.adjustment = .20
        self.direction = Vector(self.x, self.y, self.targetX, self.targetY, self.adjustment)
        self.color = color



    def move(self):
        self.x = self.x + (self.speed * self.direction.x)
        self.y = self.y + (self.speed * self.direction.y)
        self.rect.x, self.rect.y = int(self.x), int(self.y)

    def safeMove(self, x, y):
        deltaX = mathModule(self.x - x) - 1
        deltaY = mathModule(self.y - y) - 1

        if(deltaX < self.speed):
            self.x = x
            self.rect.x = x
        else:
            self.x = self.x + (self.speed * self.direction.x)
            self.rect.x= int(self.x)

        if(deltaY < self.speed):
            self.y = y
            self.rect.y = y
        else:
            self.y = self.y + (self.speed * self.direction.y)
            self.rect.y = int(self.y)

if __name__ == "__main__":
    p = Pyxel(10, 20, Color(255, 255, 255, 255))#white pyxel

    print p
