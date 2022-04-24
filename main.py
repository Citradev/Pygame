import pygame
import os

WIDTH, HEIGHT = 900, 500 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#Variables
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55, 40
FPS = 60
VEL = 5
BLACK = (0,0,0)
BORDER = pygame.Rect(WIDTH/2 - 5,0,10, HEIGHT)


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png')) #loading image
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png')) #loading another image

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(100, 50)), 90) #scaling it
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(100, 50)), 270) #scaling it
#Variables ends 


#Just drawing a window 
def draw_window(red, yellow):
        WIN.fill((255,255,255))
        pygame.draw.rect(WIN, BLACK, BORDER)
        WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x , yellow.y))
        WIN.blit(RED_SPACESHIP_IMAGE, (red.x , red.y))
        pygame.display.update()


#Movemnt of yellow space ship
def yellowmovement(keys_pressed, yellow):  
        if keys_pressed[pygame.K_a]: #left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: #right
            yellow.x += VEL 
        if keys_pressed[pygame.K_w]: #upwards
            yellow.y -= VEL 
        if keys_pressed[pygame.K_s]: #downwards
            yellow.y += VEL 

#Movemnt of red space ship
def redmovement(keys_pressed, red):  
        if keys_pressed[pygame.K_LEFT]: #left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: #right
            red.x += VEL 
        if keys_pressed[pygame.K_UP]: #upwards
            red.y -= VEL 
        if keys_pressed[pygame.K_DOWN]: #downwards
            red.y += VEL


#Main function of the window in the backend
def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()     
        yellowmovement(keys_pressed, yellow)
        redmovement(keys_pressed, red)

        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
