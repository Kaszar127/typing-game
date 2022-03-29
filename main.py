import pygame as pg
from pygame.locals import *

class Ball:
    def __init__(self, xPos, yPos, xVel = 1, yVel = 1, rad = 15):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
    def draw(self, surface):
        pg.draw.circle(surface, black, (self.x, self.y), self.radius)

pg.init()

pg.display.set_caption("Type or DIE")
#pg.display.set_icon(pg.image.load("C:/Users/silas/OneDrive/Billeder/typing.gif"))

resolution = (700,400)
white = (255,255,255)
black = (0,0,0)

screen = pg.display.set_mode(resolution,pg.RESIZABLE)

ball = Ball(resolution[0]/2, resolution[1]/2)

while True:
    screen.fill(white)

    ball.draw(screen)
    
    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()