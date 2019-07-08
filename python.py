import pygame
import sys

screen = pygame.display.set_mode((640,320))



#turns
Turn = 0

while Turn == 0:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if Card.get_rect().collidepoint(pygame.mouse.get_pos()):
            if e.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((255,255,255))     
          
    time.sleep(0.03)
    pygame.display.update()  
