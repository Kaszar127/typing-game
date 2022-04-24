import pygame as pg
from pygame import gfxdraw
import math
import random
import os.path
import time

resolution = [1000,1000]
white = pg.Color(255,255,255)
red = pg.Color(255,0,0)
black = pg.Color(0,0,0)
user_text = ""
my_path = os.path.abspath(os.path.dirname(__file__))
score = 0
fontSize = 22
userRadius = 15
enemyList = []

# deltaTime
prev_time = time.time()
deltaTime = 0
timer = 0
enemyTimer = 0

class Enemy:
    def __init__(self, surface, words,):
        self.surface = surface
        self.randomVar = random.randint(0,360)
        self.spawnRad = int(self.surface.get_width()/2)
        self.position = pg.Vector2(int(self.surface.get_width()/2 + self.spawnRad * math.cos(self.randomVar * math.pi / 180)), int(self.surface.get_height()/2 + self.spawnRad * math.sin(self.randomVar * math.pi / 180)))
        self.radius = 15
        self.word = random.choice(words)
        self.speed = 1
        
    def draw(self):
        #gfxdraw.filled_circle(self.surface, int(self.position.x), int(self.position.y), self.radius, red)
        #gfxdraw.aacircle(self.surface, int(self.position.x), int(self.position.y), self.radius, red)
        
        screen.blit(font.render(self.word, True, black),(self.position.x - self.radius/2 - (fontSize*len(self.word)/5), self.position.y - (userRadius*3) - (fontSize/2)))

        if(self.position.x >= self.surface.get_width()/2):
            screen.blit(slimeSpriteFlipped,(self.position.x - screen.get_width()/30, self.position.y - screen.get_height()/30))
        else:
            screen.blit(slimeSprite,(self.position.x - screen.get_width()/30, self.position.y - screen.get_height()/30))


    def elim(self, user_text):
        if(self.word == user_text):
            # Still need fix
            #limAni = font.render(str(len(self.word*10)), True, black)
            #screen.blit(elimAni,(self.position.x, self.position.y))
            
            return True, 
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

screen = pg.display.set_mode(resolution)

font = pg.font.Font(os.path.join(my_path,"Assets/Roboto-Black.ttf"),fontSize)

# Image load
wizardLoad = pg.image.load(os.path.join(my_path,"Assets/wizard.png"))
slimeLoad = pg.image.load(os.path.join(my_path,"Assets/slime.png"))
grassLoad = pg.image.load(os.path.join(my_path,"Assets/grass.jpg"))

# Image transform
wizardSprite = pg.transform.scale(wizardLoad, (screen.get_width()/10,screen.get_height()/10))
slimeSprite = pg.transform.scale(slimeLoad, (screen.get_width()/15, screen.get_height()/15))
slimeSpriteFlipped = pg.transform.flip(slimeSprite.copy(),True, False)
grassSprite = pg.transform.scale(grassLoad, (screen.get_width(),screen.get_height()))

pg.display.set_caption("Word Wizard")
pg.display.set_icon(pg.image.load(os.path.join(my_path,"Assets/wizard.png")))

while True:
    # deltaTime
    nowTime = time.time()
    deltaTime = nowTime - prev_time
    prev_time = nowTime
    timer += deltaTime
    enemyTimer += deltaTime

    # Image display
    screen.blit(grassSprite,(0, 0))
    screen.blit(wizardSprite,(screen.get_width()/2-screen.get_width()/20, screen.get_height()/2-screen.get_height()/20))
    
    # Calls enemy draw method
    list(map(lambda x: x.draw(), enemyList))

    # Calls enemy move method based on deltatime
    if(timer >= 0.01):
        list(map(lambda x: x.move(),enemyList))
        timer = 0

    # Generates enemy based on deltatime
    if(enemyTimer >= 2):
        enemyList.append(Enemy(screen, wordlist))
        enemyTimer = 0

    # For visulisation will remove
    #gfxdraw.aacircle(screen,int(screen.get_width()/2),int(screen.get_height()/2),int(resolution[0]/2),black)
    #gfxdraw.aacircle(screen,int(screen.get_width()/2),int(screen.get_height()/2),userRadius,black)

    screen.blit(font.render("Score: " + str(score), True, black),(screen.get_width()/2 - (fontSize*(len("Score: ")+len(str(score)))/5), fontSize))
    screen.blit(font.render(user_text, True, black),(screen.get_width()/2 - (userRadius/2) - (fontSize*len(user_text)/5), screen.get_height()/2 - (userRadius*5) - (fontSize/2)))
    
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
                        score += len(user_text)*10
                for j in range(len(indexList)):
                    enemyList.pop(indexList[j])
                
                user_text = ""
        if(event.type == pg.QUIT):
            pg.quit()

#    for char in range(len(user_text)):
#       if user_text[char] == enemy.word:
#          print(user_text[char])