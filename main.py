import pygame as pg
from pygame import gfxdraw
import math
import random
import os.path
import time

resolution = [700,700]
white = pg.Color(255,255,255)
red = pg.Color(255,0,0)
black = pg.Color(0,0,0)
user_text = ""
my_path = os.path.abspath(os.path.dirname(__file__))

# deltaTime
prev_time = time.time()
deltaTime = 0
timer = 0
enemyTimer = 0

class Enemy:
    def __init__(self, surface, words, rad = 15):
        self.surface = surface
        self.randomVar = random.randint(0,360)
        self.spawnRad = int(self.surface.get_width()/2)
        self.position = pg.Vector2(int(self.surface.get_width()/2 + self.spawnRad * math.cos(self.randomVar * math.pi / 180)), int(self.surface.get_height()/2 + self.spawnRad * math.sin(self.randomVar * math.pi / 180)))
        self.radius = rad
        self.word = random.choice(words)
        self.speed = 5
        
    def draw(self):
        gfxdraw.filled_circle(self.surface, int(self.position.x), int(self.position.y), self.radius, red)
        gfxdraw.aacircle(self.surface, int(self.position.x), int(self.position.y), self.radius, red)
        text = font.render(self.word, True, black)
        screen.blit(text,(self.position.x, self.position.y - self.surface.get_height()/10))

    def elim(self, user_text):
        if(self.word == user_text):
           return True
        return False

    def move(self):

        try:
            self.target = (pg.Vector2(self.surface.get_size())/2 - self.position).normalize()
        except:
            pass

        self.velocity = pg.Vector2(self.target.x * self.speed, self.target.y * self.speed)
        self.position += self.velocity


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

enemyList = []

while True:
    # deltaTime
    nowTime = time.time()
    deltaTime = nowTime - prev_time
    prev_time = nowTime
    timer += deltaTime
    enemyTimer += deltaTime

    screen.fill(white)
    list(map(lambda x: x.draw(), enemyList))

    if(timer >= 0.01):
        list(map(lambda x: x.move(),enemyList))
        timer = 0

    if(enemyTimer >= 2):
        enemyList.append(Enemy(screen, wordlist))
        enemyTimer = 0

    # For visulisation will remove
    gfxdraw.aacircle(screen,int(screen.get_width()/2),int(screen.get_height()/2),int(resolution[0]/2), black)
    gfxdraw.aacircle(screen,int(screen.get_width()/2),int(screen.get_height()/2),15, black)
    
    pg.display.flip()

    for event in pg.event.get():
        if(event.type == pg.KEYDOWN):
            user_text += event.unicode
            if(event.key == pg.K_BACKSPACE):
                user_text = user_text[:-2]
            if(event.key == pg.K_SPACE):
                user_text = user_text[:-1]
                print((user_text))
                
                # Created to avoid overunning enemyList while reffering to the last element
                indexList = []
                for i in range(len(enemyList)):
                    if(enemyList[i].elim(user_text)):
                        indexList.append(i)
                for j in range(len(indexList)):
                    enemyList.pop(indexList[j])
                
                user_text = ""
        if(event.type == pg.QUIT):
            pg.quit()

#    for char in range(len(user_text)):
#       if user_text[char] == enemy.word:
#          print(user_text[char])