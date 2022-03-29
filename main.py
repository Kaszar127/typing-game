import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Type or DIE")

resolution = (700,400)
white = (255,255,255)

screen = pygame.display.set_mode(resolution)

while True:
    screen.fill(white)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()