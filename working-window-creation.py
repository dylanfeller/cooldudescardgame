import pygame
pygame.init() 
  
# define the RGB value 
# for white colour 
white = (255, 255, 255) 
  
# assigning values to X and Y variable 
X = 1680
Y = 1050

# positions
hand1 = (50, 745)
hand2 = (266, 746)
hand3 = (482, 746)
hand4 = (696, 746)
hand5 = (909, 746)
hand6 = (1123, 747)
hand7 = (1336, 746)
board1 = (50, 389 ) 
board2 = (266, 390)
board3 = (482, 390)
board4 = (696, 390)
board5 = (909, 390)
board6 = (1123, 391)
board7 = (1336, 390)
board8 = (50, 128)
board9 = (266, 129)
board10 = (482, 129)
board11 = (696, 129)
board12 = (909, 129)
board13 = (1123, 130)
board14 = (1336, 129) 

  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y ), pygame.FULLSCREEN) 

# set the pygame window name 
pygame.display.set_caption('Hearthstone Beta') 
  
# create a surface object, image is drawn on it. 
image = pygame.image.load('board.jpg')
testcard = pygame.image.load('2mana23.png')
  
# infinite loop 
while True : 
  
    # fill surface object with white
    display_surface.fill(white) 
  
    # copying image to (0, 0)
    display_surface.blit(image, (0, 0))
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
    	display_surface.blit(testcard, hand1)
    if pressed[pygame.K_x]:
    	display_surface.blit(testcard, hand2)
    if pressed[pygame.K_c]:
    	display_surface.blit(testcard, hand3)
    if pressed[pygame.K_v]:
    	display_surface.blit(testcard, hand4)
    if pressed[pygame.K_b]:
    	display_surface.blit(testcard, hand5)
    if pressed[pygame.K_n]:
    	display_surface.blit(testcard, hand6)
    if pressed[pygame.K_m]:
    	display_surface.blit(testcard, hand7)
    if pressed[pygame.K_a]:
        display_surface.blit(testcard, board1)
    if pressed[pygame.K_s]:
        display_surface.blit(testcard, board2)
    if pressed[pygame.K_d]:
        display_surface.blit(testcard, board3)
    if pressed[pygame.K_f]:
        display_surface.blit(testcard, board4)
    if pressed[pygame.K_g]:
        display_surface.blit(testcard, board5)
    if pressed[pygame.K_h]:
        display_surface.blit(testcard, board6)
    if pressed[pygame.K_j]:
        display_surface.blit(testcard, board7)
    if pressed[pygame.K_q]:
        display_surface.blit(testcard, board8)
    if pressed[pygame.K_w]:
        display_surface.blit(testcard, board9)
    if pressed[pygame.K_e]:
        display_surface.blit(testcard, board10)
    if pressed[pygame.K_r]:
        display_surface.blit(testcard, board11)
    if pressed[pygame.K_t]:
        display_surface.blit(testcard, board12)
    if pressed[pygame.K_y]:
        display_surface.blit(testcard, board13)
    if pressed[pygame.K_u]:
        display_surface.blit(testcard, board14)
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit() 
            # quit the program. 
            quit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # deactivates the pygame library 
                pygame.quit() 
                # quit the program. 
                quit()
  
        # Draws the surface object to the screen.   
        pygame.display.update()  

