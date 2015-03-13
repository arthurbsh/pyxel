import math

#Defines an  unitary vector for given coordinatess
class Vector:

    def __init__(self, initX, initY, tarX, tarY, adjustment=0.3):

        vectx = tarX - initX
        vecty = tarY - initY

        module = math.sqrt(vectx*vectx + vecty*vecty)

        #what to do when source is the same as target
        if module == 0:
            module = 1

        self.x = vectx/module
        self.y = vecty/module

    def adjust(self):
        return None

    def adjustToPoint(self, x, y):
        deltaX = self.x - x
        deltaY = self.y - y

        self.x = self.x - deltaX
        self.y = self.y - deltaY

        return None

if __name__ == "__main__":
    #testing for vector

    v1 = Vector(0, 0, .1, 0)

    print v1.x
    print v1.y
