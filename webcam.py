import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera(0)
cam.start()

print pygame.camera.list_cameras()
