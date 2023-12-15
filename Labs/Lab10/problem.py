#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMIES_SPEED = 5
COINS_SPEED = 5
ENEMIES_SCORE = 0
COINS_SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
#Load background
background = pygame.image.load("assets/images/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
#Creating Enemies
class Enemy(pygame.sprite.Sprite):
    #Initializating objects
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    #Moving of enemies
    def move(self):
        global ENEMIES_SCORE
        self.rect.move_ip(0, ENEMIES_SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            ENEMIES_SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Creating Player 
class Player(pygame.sprite.Sprite):
    #Initializing object
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    #Moving player
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #Checking borders of the screen 
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]: self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]: self.rect.move_ip(5, 0)
                  
#Creating Coins                  
class Coin(pygame.sprite.Sprite):
    #Initializing 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/Coin.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    #Moving coins
    def move(self):
        global COINS_SCORE
        self.rect.move_ip(0, COINS_SPEED)
        if (pygame.sprite.spritecollideany(P1, coins)):
            COINS_SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        elif (pygame.sprite.spritecollideany(E1, coins)):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        elif (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Load backgorund music           
def play_background_music(timestamp):
    pygame.mixer_music.load('assets/audios/background.wav')
    pygame.mixer_music.play(start = timestamp)
        
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Parametrs for background music
is_playing = False
background_music_len = 16

#Game Loop
while True:    
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              ENEMIES_SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #Set on background music             
    if not is_playing:
        is_playing = True
        start_ticks = pygame.time.get_ticks()
        play_background_music(0)
     
    #Calucate time passed    
    if is_playing: time_stamp = (pygame.time.get_ticks() - start_ticks) / 1000
    
    if time_stamp > background_music_len: is_playing = False
 
    #Draw background
    DISPLAYSURF.blit(background, (0,0))
    
    #Draw enemies scores
    enemies_scores = font_small.render(str(ENEMIES_SCORE), True, BLACK)
    DISPLAYSURF.blit(enemies_scores, (10,10))
    
    #Draw coins scores
    coins_scores = font_small.render(str(COINS_SCORE), True, BLACK)
    DISPLAYSURF.blit(coins_scores, (SCREEN_WIDTH - 35, 10))
    
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        #Post game screen
        play_background_music(background_music_len)
        pygame.mixer.Sound('assets/audios/crash.wav').play()
        time.sleep(0.5)
                
        #Draw game over screen        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        #Deleting sprites
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()       
         
    pygame.display.update()
    FramePerSec.tick(FPS)