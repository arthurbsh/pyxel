import pygame
from pyxel import *
import random
from PIL import Image
im = Image.open("./images/image.jpg") #Can be many different formats.
cam = Image.open("./images/webcam.jpg")
pix = im.load()
webcam = pygame.image.load("./images/webcam.jpg")
ima = pygame.image.load("./images/image.jpg")

camw = webcam.get_width()
camh = webcam.get_height()

width = 1280
height = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

def mathModule(x):
    if(x< 0):
        return -x
    return x


def isGray(c):
    colors = [c.r, c.g, c.b]

    limit = 30

    return (max(colors) - min(colors)) < limit

def isNeighbor(r1, r2):
    x = r1.centerx - r2.centerx
    y = r1.centery - r2.centery

    x *= x
    y *= y

    return (x + y) < 200

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




#detects all colored pixels
detected = []
for i in range(camw/10):
    for j in range(camh/10):
        x = i*10
        y = j*10

        c = pygame.transform.average_color(webcam, Rect(x, y, 10, 10))
        color = pygame.Color(c[0], c[1],c[2], c[3])

        #gpyx = gpyxs[getClosestColor(color, gpyxs)]
        if not isGray(color):
            detected.append(Pyxel(x, y, color, x, y))


#group near pixels
groups = []
while len(detected) > 0:
    group = [detected.pop(0)]
    added = True
    i = 0
    while i < len(detected):
        for g in group:
            if not i < len(detected):
                break
            if isNeighbor(detected[i].rect, g.rect):
                group.append(detected.pop(i))
                #print "add new guy to group"
                i = 0
                continue
        i += 1

    #print "adding new group with", len(group), "elements"
    groups.append(group)

#create color point for each chuck of pixels
gpyxs = []
for group in groups:
    size = len(group)
    sumx = 0
    sumy = 0
    sumr = 0
    sumg = 0
    sumb = 0
    for g in group:
        sumx += g.x
        sumy += g.y
        sumr += g.color.r
        sumg += g.color.g
        sumb += g.color.b

    avgx = int(sumx/size)
    avgy = int(sumy/size)

    cpx = (width/camw)*avgx
    cpy = (height/camh)*avgy

    #print "gpyx added"
    gpyxs.append(Pyxel(cpx, cpy, pygame.Color(sumr/size, sumg/size, sumb/size, 255)))

#create all moving points
pyxs = []
for i in range(width/10):
    for j in range(height/10):
        r, g, b = pix[i,j]
        #r = random.randint(0, 255)
        #g = random.randint(0, 255)
        #b = random.randint(0, 255)
        a = 255
        x = i*10
        y = j*10
        r, g, b = pix[x,y]

        c = pygame.transform.average_color(ima, Rect(x, y, 10, 10))
        color = pygame.Color(c[0], c[1],c[2], c[3])
        #color = pygame.Color(r, g, b, a)

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
            #pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.iX, pyx.iY)
            pyx.direction.headTo(pyx.x, pyx.y, pyx.iX, pyx.iY)
            pyx.safeMove(pyx.iX, pyx.iY)
        else:#movement based shit on screen
            pyx.direction.adjustToPoint(pyx.x, pyx.y, pyx.dX, pyx.dY)
            pyx.move()

        #pygame.draw.rect(screen, pyx.color, pyx.rect, 1)#draws empty squares



        if((pyx.x, pyx.y)==(pyx.iX, pyx.iY)):
            #pass
            screen.blit(ima, (pyx.rect.x, pyx.rect.y), (pyx.rect.x, pyx.rect.y, pyx.rect.width, pyx.rect.height))
        else:
            #pass
            pygame.draw.circle(screen, pyx.color, (pyx.rect.x, pyx.rect.y), pyx.rect.width/2)#draws filled circles

    #screen.blit(ima, pygame.Rect(20, 20, 50, 50))


    for d in gpyxs:
        #pygame.draw.rect(screen, d.color, d.rect, 1)
        pass
    for group in groups:
        for d in group:
            pass
            #pygame.draw.rect(screen, d.color, d.rect, 1)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick()
    print clock.get_fps()
    #print pygame.mouse.get_pressed()
