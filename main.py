import pygame as pg
from pygame.locals import *

pg.init()

pg.display.set_caption("Type or DIE")
pg.display.set_icon(pg.image.load("C:/Users/silas/OneDrive/Billeder/typing.gif"))

resolution = (700,400)
white = (255,255,255)

screen = pg.display.set_mode(resolution,pg.RESIZABLE)

while True:
    screen.fill(white)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()