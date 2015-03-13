import pygame
from pyxel import *
import random

width = 1280
height = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

pyxs = []

for i in range(10000):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = 255
    x = random.randint(0, 1280)
    y = random.randint(0, 720)

    pyxs.append(Pyxel(x, y, pygame.Color(r, g, b, a)))
#pyxs.append(Pyxel(250, 250, pygame.Color("white")))
#pyxs.append(Pyxel(300, 300, pygame.Color("white")))
#pyxs.append(Pyxel(350, 350, pygame.Color("white")))
#pyxs.append(Pyxel(400, 400, pygame.Color("white")))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    tx, ty = pygame.mouse.get_pos()

    for pyx in pyxs:
        pyx.direction.adjustToPoint(pyx.x, pyx.y, tx, ty)
        pyx.move()
        pygame.draw.rect(screen, pyx.color, pyx.rect, 1)


    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick()
    print clock.get_fps()
