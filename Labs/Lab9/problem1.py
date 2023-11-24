import pygame
from datetime import datetime
pygame.init()

#Set display
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Problem 1")

#Load pictures
main_clock = pygame.image.load('clock_images/main-clock.png')
main_clock = pygame.transform.scale(main_clock, (600, 600))
rect_main_clock = main_clock.get_rect()
rect_main_clock.center = (width // 2, height // 2)

left_hand = pygame.image.load('clock_images/left-hand.png')
left_hand = pygame.transform.scale(left_hand, (360, 90))
rect_left_hand = left_hand.get_rect()
rect_left_hand.center = (width // 2, height // 2)

right_hand = pygame.image.load('clock_images/right-hand.png')
right_hand = pygame.transform.scale(right_hand, (320, 80))
rect_right_hand = right_hand.get_rect()
rect_right_hand.center = (width // 2, height // 2)

#Set clock
clock = pygame.time.Clock()
FPS = 60

#Find current angle of left hand 
def left_hand_angle():
    return (90 -6 * datetime.now().second) % 360

#Find current angle for right hand
def right_hand_angle():
    return (90 -6 * datetime.now().minute) % 360

#Game function. Work until the quit from the game
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((255, 255, 255))
        
        #Rotate left hand
        rotated_left_hand = pygame.transform.rotate(left_hand, left_hand_angle())
        rect_rotated_left_hand = rotated_left_hand.get_rect()
        rect_rotated_left_hand.center = rect_left_hand.center    
        
        #Rotate right hand
        rotated_right_hand = pygame.transform.rotate(right_hand, right_hand_angle())
        rect_rotated_right_hand = rotated_right_hand.get_rect()
        rect_rotated_right_hand.center = rect_right_hand.center
        
        #Make all pictures visible on the display
        screen.blit(main_clock, rect_main_clock)
        screen.blit(rotated_left_hand, rect_rotated_left_hand)
        screen.blit(rotated_right_hand, rect_rotated_right_hand)
        
        pygame.display.update()
        clock.tick(FPS)
        
game()
pygame.quit()