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
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 

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
    if pressed[pygame.K_1]:
    	display_surface.blit(testcard, hand1)
    if pressed[pygame.K_2]:
    	display_surface.blit(testcard, hand2)
    if pressed[pygame.K_3]:
    	display_surface.blit(testcard, hand3)
    if pressed[pygame.K_4]:
    	display_surface.blit(testcard, hand4)
    if pressed[pygame.K_5]:
    	display_surface.blit(testcard, hand5)
    if pressed[pygame.K_6]:
    	display_surface.blit(testcard, hand6)
    if pressed[pygame.K_7]:
    	display_surface.blit(testcard, hand7)
  
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
  
        # Draws the surface object to the screen.   
        pygame.display.update()  

