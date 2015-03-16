import pygame
from pyxel import *
import random

def mathModule(x):
    if(x< 0):
        return -x
    return x

def getClosestColor(color, colorList):
    deltas = []
    for gpyx in colorList:
        c = gpyx.color
        deltaR = mathModule(c.r - color.r)
        deltaG = mathModule(c.g - color.g)
        deltaB = mathModule(c.b - color.b)
        deltas.append(deltaR + deltaG + deltaB)

    return deltas.index(min(deltas))


width = 1280
height = 720

clock = pygame.time.Clock()

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pyxs = []
gpyxs = []

#create points to be followed
gpyxs.append(Pyxel(237, 512, pygame.Color(255, 0, 0, 255)))
gpyxs.append(Pyxel(535, 578, pygame.Color(0, 255, 0, 255)))
gpyxs.append(Pyxel(1000, 250, pygame.Color(0, 0, 255, 255)))
gpyxs.append(Pyxel(400, 200, pygame.Color(255, 255, 255, 255)))

#create all moving points
for i in range(width/10):
    for j in range(height/10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = 255
        x = i*10
        y = j*10
    #x = random.randint(0, width)
    #y = random.randint(0, height)

        color = pygame.Color(r, g, b, a)

        gpyx = gpyxs[getClosestColor(color, gpyxs)]

        pyxs.append(Pyxel(x, y, color, gpyx.x, gpyx.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    tx, ty = pygame.mouse.get_pos()

    for pyx in pyxs:
        if pygame.mouse.get_pressed()[0]:#movement based on mouse position
            pyx.direction.adjustToPoint(pyx.x, pyx.y, tx, ty)
            pyx.move()
        elif pygame.key.get_pressed()[pygame.K_SPACE]:#movement based initial position
            #adjust positon to default point(the color changer parameter)
            pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.iX, pyx.iY)
            #pyx.direction.headTo(pyx.x, pyx.y, pyx.iX, pyx.iY)
            pyx.safeMove(pyx.iX, pyx.iY)
        else:#movement based shit on screen
            pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.dX, pyx.dY)
            pyx.move()

        pygame.draw.rect(screen, pyx.color, pyx.rect, 1)


    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(20)
    #print clock.get_fps()
    #print pygame.mouse.get_pressed()
