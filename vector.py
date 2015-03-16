import math

#Defines an  unitary vector for given coordinatess
class Vector:

    def __init__(self, initX, initY, tarX, tarY, adjustment=0.3):

        vectx = float(tarX - initX)
        vecty = float(tarY - initY)

        module = math.sqrt(vectx*vectx + vecty*vecty)

        #what to do when source is the same as target
        if module != 0:
            self.x = vectx/module
            self.y = vecty/module
        else:
            self.x = vectx
            self.y = vecty

        self.adjustment = adjustment

    def makeUnit(self):
        vectx = self.x
        vecty = self.y

        module = math.sqrt(vectx*vectx + vecty*vecty)

        #what to do when source is the same as target
        if module == 0:
            module = 1

        self.x = vectx/module
        self.y = vecty/module

    def adjust(self):
        return None

    def headTo(self, sx, sy, tx, ty):
        newx =  tx - sx
        newy = ty - sy

        newmodule = math.sqrt(newx*newx + newy*newy)


        if(newmodule != 0):
            newy = (newy/newmodule)
            newx = (newx/newmodule)

        self.x = newx
        self.y = newy

        self.makeUnit()

    def adjustToPoint(self, sx, sy, tx, ty, modulate=1):
        newx =  tx - sx
        newy = ty - sy

        newmodule = math.sqrt(newx*newx + newy*newy)


        if(newmodule != 0):
            newy = (newy/newmodule)*self.adjustment
            newx = (newx/newmodule)*self.adjustment

        self.x = self.x + newx
        self.y = self.y + newy

        if(modulate):
            self.makeUnit()

if __name__ == "__main__":
    #testing for vector

    v1 = Vector(0, 0, .1, 0)

    print v1.x
    print v1.y
