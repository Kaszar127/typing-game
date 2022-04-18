import pygame as pg
from pygame import gfxdraw
import math
import random
import os.path

resolution = [700,700]
white = pg.Color(255,255,255)
black = pg.Color(0,0,0)
user_text = ""
my_path = os.path.abspath(os.path.dirname(__file__))

class Enemy:
    def __init__(self, xPos, yPos, words, rad = 15):
        self.randomVar = random.randint(0,360)
        self.spawnRad = int(resolution[0]/2)
        self.x = int(resolution[0]/2 + self.spawnRad * math.cos(self.randomVar * math.pi / 180))
        self.y = int(resolution[1]/2 + self.spawnRad * math.sin(self.randomVar * math.pi / 180))
        self.radius = rad
        self.word = random.choice(words)

    def draw(self, surface):
        gfxdraw.filled_circle(surface, self.x, self.y, self.radius, black)
        gfxdraw.aacircle(surface, self.x, self.y, self.radius, black)
        text = font.render(self.word, True, black)
        screen.blit(text,(self.x, self.y - resolution[1]/10))

    def elim(self, user_text):
        if(self.word == user_text):
           return True
        return False

# Makes wordlist.txt into an actual list
wordfile = open(os.path.join(my_path,"Assets/wordlist.txt"), "r")
worddata = wordfile.read()
wordlist = worddata.split("\n")
wordfile.close()

pg.init()

font = pg.font.Font(os.path.join(my_path,"Assets/Roboto-Black.ttf"),18)

pg.display.set_caption("Word Wizard")
pg.display.set_icon(pg.image.load(os.path.join(my_path,"Assets/typing.jpg")))

screen = pg.display.set_mode(resolution)

enemyList = [Enemy(resolution[0]/2, resolution[1]/2, wordlist), Enemy(resolution[0]/3, resolution[1]/3, wordlist)]

while True:
    screen.fill(white)
    list(map(lambda x: x.draw(screen), enemyList))

    # For visulisation will remove
    gfxdraw.aacircle(screen,int(resolution[0]/2),int(resolution[1]/2),int(resolution[0]/2), black)

    pg.display.flip()
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            user_text += event.unicode
            if event.key == pg.K_BACKSPACE:
                user_text = user_text[:-2]
            if event.key == pg.K_SPACE:
                user_text = user_text[:-1]
                print((user_text))
                
                # Created to avoide overunning enemyList while reffering to the last element
                indexList = []
                for i in range(len(enemyList)):
                    if(enemyList[i].elim(user_text)):
                        indexList.append(i)
                for j in range(len(indexList)):
                    enemyList.pop(indexList[j])

                user_text = ""

                # Kept for future refference
                # list(map(lambda x: x.elim(user_text), enemyList))

        if event.type == pg.QUIT:
            pg.quit()

#    for char in range(len(user_text)):
#       if user_text[char] == enemy.word:
#          print(user_text[char])