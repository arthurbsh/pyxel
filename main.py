import pygame
from pyxel import *

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

pyxs = []

pyxs.append(Pyxel(200, 200, pygame.Color('white')))
pyxs.append(Pyxel(250, 250, pygame.Color("white")))
pyxs.append(Pyxel(300, 300, pygame.Color("white")))
pyxs.append(Pyxel(350, 350, pygame.Color("white")))
pyxs.append(Pyxel(400, 400, pygame.Color("white")))




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        else:
            pass

    for pyx in pyxs:
        pygame.draw.rect(screen, pyx.color, pyx.rect, 1)

    pygame.display.flip()
