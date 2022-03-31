import pygame as pg
from pygame import gfxdraw
import random

class Enemy:
    def __init__(self, xPos, yPos, words, rad = 15):
        self.x = int(xPos)
        self.y = int(yPos)
        self.radius = rad
        self.type = "ball"
        self.word = random.choice(words)

    def draw(self, surface):
        gfxdraw.filled_circle(surface, self.x, self.y, self.radius, black)
        gfxdraw.aacircle(surface, self.x, self.y, self.radius, black)
        
        text = font.render(self.word, True, black)
        screen.blit(text,(self.x, self.y - 100))

# Makes wordlist.txt into an actual list
wordfile = open("Assets/wordlist.txt", "r")
worddata = wordfile.read()
wordlist = worddata.split("\n")
wordfile.close()

pg.init()

font = pg.font.Font('Assets/Roboto-Black.ttf',18)

pg.display.set_caption("Type or DIE")
pg.display.set_icon(pg.image.load("Assets/typing.jpg"))

resolution = (700,400)
white = pg.Color(255,255,255)
black = pg.Color(0,0,0)

screen = pg.display.set_mode(resolution)

Enemy = Enemy(resolution[0]/2, resolution[1]/2, wordlist)

while True:
    screen.fill(white)

    Enemy.draw(screen)
    
    
    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()