import pygame as pg

from pygame import gfxdraw

class Ball:
    def __init__(self, xPos, yPos, xVel = 1, yVel = 1, rad = 15):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
    def draw(self, surface):
        gfxdraw.filled_circle(surface, int(self.x), int(self.y), self.radius, black)
        gfxdraw.aacircle(surface, int(self.x), int(self.y), self.radius, black)

# Makes wordlist.txt into an actual list
wordfile = open("wordlist.txt", "r")
worddata = wordfile.read()
wordlist = worddata.split("\n")
print(wordlist)
wordfile.close()

pg.init()

pg.display.set_caption("Type or DIE")
#pg.display.set_icon(pg.image.load("C:/Users/silas/OneDrive/Billeder/typing.gif"))

resolution = (700,400)
white = pg.Color(255,255,255)
black = pg.Color(0,0,0)

screen = pg.display.set_mode(resolution,pg.RESIZABLE)

ball = Ball(resolution[0]/2, resolution[1]/2)

while True:
    screen.fill(white)

    ball.draw(screen)
    
    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()