import pygame
from pyxel import *
import random
from PIL import Image
im = Image.open("./images/webcam.jpg") #Can be many different formats.
webcam = pygame.image.load("./images/webcam.jpg")
pix = im.load()


#print im.size #Get the width and hight of the image for iterating over




def mathModule(x):
    if(x< 0):
        return -x
    return x

def isGray(c):
    colors = [c.r, c.g, c.b]

    limit = 30

    return (max(colors) - min(colors)) < limit

def getClosestColor(color, colorList):
    deltas = []
    for gpyx in colorList:
        c = gpyx.color
        deltaR = mathModule(c.r - color.r)
        deltaR *= deltaR
        deltaG = mathModule(c.g - color.g)
        deltaG *= deltaG
        deltaB = mathModule(c.b - color.b)
        deltaB *= deltaB
        #print deltaR, deltaG, deltaB
        deltas.append(deltaR + deltaG + deltaB)

    return deltas.index(min(deltas))


width = 1280
height = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pyxs = []
gpyxs = []

#create points to be followed
gpyxs.append(Pyxel(200, 120, pygame.Color(255, 0, 0, 255)))
gpyxs.append(Pyxel(400, 240, pygame.Color(0, 255, 0, 255)))
gpyxs.append(Pyxel(600, 360, pygame.Color(0, 0, 255, 255)))
gpyxs.append(Pyxel(800, 480, pygame.Color(255, 255, 255, 255)))
gpyxs.append(Pyxel(1000, 600, pygame.Color(255, 255, 0, 255)))

#create all moving points
for i in range(640/10):
    for j in range(480/10):
        r, g, b = pix[i,j]
        #r = random.randint(0, 255)
        #g = random.randint(0, 255)
        #b = random.randint(0, 255)
        a = 255
        x = i*10
        y = j*10
        r, g, b = pix[x,y]

        c = pygame.transform.average_color(webcam, Rect(x, y, 10, 10))
        #print c

        color = pygame.Color(c[0], c[1],c[2], c[3])



        gpyx = gpyxs[getClosestColor(color, gpyxs)]
        if not isGray(color):
            pyxs.append(Pyxel(x, y, color, gpyx.x, gpyx.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    tx, ty = pygame.mouse.get_pos()

    #print pyxs[tx/10 + (ty/10)*128].color

    for pyx in pyxs:
        if pygame.mouse.get_pressed()[0]:#movement based on mouse position
            pyx.direction.adjustToPoint(pyx.x, pyx.y, tx, ty)
            #pyx.move()
        elif pygame.key.get_pressed()[pygame.K_SPACE]:#movement based initial position
            #adjust positon to default point(the color changer parameter)
            #pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.iX, pyx.iY)
            pyx.direction.headTo(pyx.x, pyx.y, pyx.iX, pyx.iY)
            #pyx.safeMove(pyx.iX, pyx.iY)
        else:#movement based shit on screen
            pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.dX, pyx.dY)
            #pyx.move()

        pygame.draw.rect(screen, pyx.color, pyx.rect, 1)#draws empty squares
        #pygame.draw.circle(screen, pyx.color, (pyx.rect.x, pyx.rect.y), pyx.rect.width/2)#draws filled circles


    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(20)
    #print clock.get_fps()
    #print pygame.mouse.get_pressed()
