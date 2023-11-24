import pygame
pygame.init()

#Set display
size = width, height = 800, 800
radius = 25
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Problem 3")

#Make white screen draw red circle
screen.fill((255, 255, 255))
pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), radius)

#Set coordinates of a circle
x_coor, y_coor = width // 2, height // 2

#Set clock
clock = pygame.time.Clock()
FPS = 60

#Game function. Work until the quit from the game
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                global x_coor, y_coor
                screen.fill((255, 255, 255))
                if event.key == pygame.K_UP:
                    y_coor = max(radius, y_coor - 20)
                    pygame.draw.circle(screen, (255, 0, 0), (x_coor, y_coor), 25)
                elif event.key == pygame.K_DOWN:
                    y_coor = min(height - radius, y_coor + 20)
                    pygame.draw.circle(screen, (255, 0, 0), (x_coor, y_coor), 25)
                elif event.key == pygame.K_LEFT:
                    x_coor = max(radius, x_coor - 20)
                    pygame.draw.circle(screen, (255, 0, 0), (x_coor, y_coor), 25)
                elif event.key == pygame.K_RIGHT:
                    x_coor = min(width - radius, x_coor + 20)
                    pygame.draw.circle(screen, (255, 0, 0), (x_coor, y_coor), 25)
        
        pygame.display.update()
        clock.tick(FPS)
        
game()
pygame.quit()