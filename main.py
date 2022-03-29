import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Type or DIE")
pygame.display.set_icon(pygame.image.load("C:/Users/silas/OneDrive/Billeder/typing.gif"))

resolution = (1280,720)
white = (255,255,255)

screen = pygame.display.set_mode(resolution)

while True:
    screen.fill(white)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()