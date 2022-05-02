import pygame as pg
import math
import random
import time
import os.path

# Enemy class
class Enemy:
    def __init__(self, surface, words, speed):
        self.surface = surface
        self.spawnRad = int(self.surface.get_width()/2)
        self.randomVar = random.randint(0,360)
        self.position = pg.Vector2(int(self.surface.get_width()/2 + self.spawnRad * math.cos(self.randomVar * math.pi / 180)), int(self.surface.get_height()/2 + self.spawnRad * math.sin(self.randomVar * math.pi / 180)))
        self.radius = 15
        self.fontSize = 22
        # Will eventually self-destruct because of index range
        self.word = words.pop(words.index(random.choice(words)))
        self.enemySpeed = speed
        
    def draw(self):
        # Displays enemy word
        screen.blit(font1.render(self.word, True, pg.Color(255,0,0)),(self.position.x - self.radius/2 - (self.fontSize*len(self.word)/5), self.position.y - (userRadius*3) - (self.fontSize/2)))

        # Displays enemy sprite depending on left-right direction
        if(self.position.x >= self.surface.get_width()/2):
            screen.blit(slimeSpriteFlipped,(self.position.x - screen.get_width()/30, self.position.y - screen.get_height()/30))
        else:
            screen.blit(slimeSprite,(self.position.x - screen.get_width()/30, self.position.y - screen.get_height()/30))

    def move(self):
        # Creates direction vector from enemy position to the center
        self.target = (pg.Vector2(self.surface.get_size())/2 - self.position).normalize()
        
        # Moves the enemy with direction vector and speed
        self.velocity = pg.Vector2(self.target.x * self.enemySpeed, self.target.y * self.enemySpeed)
        self.position += self.velocity
    
    def isColliding(self):
        # Checks if enemy and wizard is colliding
        length = (pg.Vector2(self.surface.get_size())/2 - self.position).length()
        
        # Returns true or false
        return (length <= float(self.radius))
    
    def elim(self, user_text):
        # Checks if enemy word is the same as input
        if(self.word == user_text):
            return True, 
        return False

# Various variables
resolution = [1000, 1000]
user_text = ""
my_path = os.path.abspath(os.path.dirname(__file__))
score = 0
userRadius = 15
speed = 1
enemyList = []
playing = True

# deltaTime
prev_time = time.time()
deltaTime = 0
timer = 0
enemyTimer = 0

# Makes wordlist.txt into an actual list
wordfile = open(os.path.join(my_path,"Assets/wordlist.txt"), "r")
worddata = wordfile.read()
wordlist = worddata.split("\n")
wordfile.close()

# Initializes pygame and sets display size and fonts
pg.init()
screen = pg.display.set_mode(resolution, pg.RESIZABLE)
font1 = pg.font.Font(os.path.join(my_path,"Assets/Roboto-Black.ttf"),22)
font2 = pg.font.Font(os.path.join(my_path,"Assets/Roboto-Black.ttf"),36)
font3 = pg.font.Font(os.path.join(my_path,"Assets/Roboto-Black.ttf"),96)

# Image load
wizardLoad = pg.image.load(os.path.join(my_path,"Assets/wizard.png"))
slimeLoad = pg.image.load(os.path.join(my_path,"Assets/slime.png"))
grassLoad = pg.image.load(os.path.join(my_path,"Assets/grass.jpg"))

# Image transform
wizardSprite = pg.transform.scale(wizardLoad, (screen.get_width()/10,screen.get_height()/10))
slimeSprite = pg.transform.scale(slimeLoad, (screen.get_width()/15, screen.get_height()/15))
slimeSpriteFlipped = pg.transform.flip(slimeSprite.copy(),True, False)
grassSprite = pg.transform.scale(grassLoad, (screen.get_width(),screen.get_height()))

# Sets caption and img of display
pg.display.set_caption("Word Wizard")
pg.display.set_icon(pg.image.load(os.path.join(my_path,"Assets/wizard.png")))

# Main game loop
while True:
    # Sub game loop
    while playing:
        # deltaTime
        nowTime = time.time()
        deltaTime = nowTime - prev_time
        prev_time = nowTime
        timer += deltaTime
        enemyTimer += deltaTime

        # Image display
        screen.blit(grassSprite,(0, 0))
        screen.blit(wizardSprite,(screen.get_width()/2-screen.get_width()/20, screen.get_height()/2-screen.get_height()/20))
    
        # Calls enemy draw function
        list(map(lambda x: x.draw(), enemyList))

        # Calls enemy move function and isColliding function based on deltatime
        if(timer >= 0.01):
            for i in range(len(enemyList)):
                enemyList[i].move()
                if(enemyList[i].isColliding()):
                    playing = False
            timer = 0

        # Generates enemy based on deltatime and changes enemy speed
        if(enemyTimer >= 2):
            enemyList.append(Enemy(screen, wordlist, speed))
            speed += 0.02
            enemyTimer = 0

        # Displays score and user input
        screen.blit(font2.render("Score: " + str(score), True, pg.Color(0,0,0)),(screen.get_width()/2 - (36*(len("Score: ")+len(str(score)))/5), 36))
        screen.blit(font1.render(user_text, True, pg.Color(0,0,0)),(screen.get_width()/2 - (userRadius/2) - (22*len(user_text)/5), screen.get_height()/2 - (userRadius*5) - (22/2)))
    
        # Refreshes display
        pg.display.flip()

        # Main event loop
        for event in pg.event.get():
            if(event.type == pg.KEYDOWN):
                # Puts the clicked button in a string
                user_text += event.unicode
                if(event.key == pg.K_BACKSPACE):
                    # Removes the backspace unicode character and the previous typed character
                    user_text = user_text[:-2]
                if(event.key == pg.K_SPACE or event.key == pg.K_RETURN):
                    # Removes space or enter unicode
                    user_text = user_text[:-1]
    
                    # Created to avoid overunning enemyList while reffering to the last element
                    indexList = []
                    for i in range(len(enemyList)):
                        if(enemyList[i].elim(user_text)):
                            indexList.append(i)
                            score += len(user_text)*10
                    for j in range(len(indexList)):
                        enemyList.pop(indexList[j])

                    # Resets user input
                    user_text = ""
            if(event.type == pg.QUIT):
                pg.quit()
    
    # Game over loop
    while not playing:
        # Game over screen background
        screen.fill(pg.Color(0, 0, 0))

        # Game over screen text
        screen.blit(font3.render("Game Over", True, pg.Color(255, 0, 0)), (screen.get_width()/2 - (96*(len("Game Over")/4)), screen.get_height()/4))
        screen.blit(font2.render("A Tragic End", True, pg.Color(255, 255, 255)), (screen.get_width()/2 - (36*(len("A Tragic End")/4.3)), screen.get_height()/2-(36*1.5)))
        screen.blit(font1.render("The casting speed of the wizard could not keep up with the appearance of slimes.", True, pg.Color(255, 255, 255)), (screen.get_width()/2 - (22*(len("The casting speed of the wizard could not keep up with the appearance of slimes.")/4.3)), screen.get_height()/2))
        screen.blit(font1.render("Still, The wizard put up a valiant front before succumbing to the unending horde of slimes.", True, pg.Color(255, 255, 255)), (screen.get_width()/2 - (22*(len("Still, The wizard put up a valiant front before succumbing to the unending horde of slimes.")/4.3)), screen.get_height()/2+(22*1.5)))
        screen.blit(font1.render("Thereby, achieving a score of " + str(score) + " for future wizards to beat.", True, pg.Color(255, 255, 255)), (screen.get_width()/2 - (22*((len("Thereby, achieving a score of ")+len(str(score))+len(" for future wizards to beat."))/4.3)), screen.get_height()/2+(22*1.5*2)))
        screen.blit(font2.render("Press ENTER for a subsequent attempt. . .", True, pg.Color(255, 255, 255)), (screen.get_width()/2 - (36*(len("Press ENTER for a subsequent attempt. . .")/4.3)), screen.get_height()/1.5))
        
        # Game over screen refresh
        pg.display.flip()

        # Game over screen event loop
        for event in pg.event.get():
            if(event.type == pg.KEYDOWN):
                if(event.key == pg.K_RETURN):
                    # Resets game variables 
                    score = 0
                    enemyList = []
                    user_text = ""
                    speed = 1
                    playing = True
            if(event.type == pg.QUIT):
                pg.quit()