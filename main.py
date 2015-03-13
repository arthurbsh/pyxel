import pygame
from pyxel import *
import random

width = 1280
height = 720

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

pyxs = []

for i in range(100):
    pass

pyxs.append(Pyxel(200, 200, pygame.Color('white')))
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
    clock.tick(60)
    print clock.get_fps()
