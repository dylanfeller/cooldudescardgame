import pygame, time, sys
pygame.init()

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

class Deck():
    cardNumber = 0
      
class Card(pygame.sprite.Sprite):
    """The card class that will be used to give every card an ID"""
    cardHealth = 0
    cardCost = 0
    cardAttack = 0
    cardTexture = 0
    cardEffect = 0
    cardPosition = hand1
    def cardAlive(self):
        if cardHealth <= 0:
            #kill self
            cardPosition = 2
    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect()
    def update(self):
        self.rect = self.image.get_rect(center=(self.cardPosition[0]+100, self.cardPosition[1]+125))


card1 = Card(pygame.image.load("2mana23.png"))
highlight = pygame.image.load("HIGHLIGHT.png")
card1.cardHealth = 3
card1.cardAttack = 2
card1.cardCost = 2
card1.cardTexture = 1
card1.cardEffect = 1
card1.cardPosition = hand1

FieldCards = [card1]


white = (255, 255, 255)
X = 1680
Y = 1050


display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Hearthstone Beta') 

image = pygame.image.load('board.jpg')
highlighted=False
while True :
    display_surface.fill(white) 
    display_surface.blit(image, (0, 0))
    display_surface.blit(card1.image, hand1)
    if(highlighted): 
        display_surface.blit(highlight, card1.cardPosition)
    ev = pygame.event.get()

    for event in ev:
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if card1.image.get_rect(center=(card1.cardPosition[0]+100,card1.cardPosition[1]+125)).collidepoint(pos):
                display_surface.blit(highlight, card1.cardPosition)
                highlighted=not highlighted
            # do something with the clicked sprites...


                        
    for event in ev : 
 
        if event.type == pygame.QUIT : 
            pygame.quit()        
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:                
                pygame.quit()
                sys.exit()                

    card1.update()
    pygame.display.update()    