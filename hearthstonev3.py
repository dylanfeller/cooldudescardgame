import pygame
import sys
import time

screen = pygame.display.set_mode((640,320))

class Deck():
    cardNumber = 0

      
class Card(pygame.sprite.Sprite):
    """The card class that will be used to give every card an ID"""
    cardHealth = 0
    cardCost = 0
    cardAttack = 0
    cardTexture = 0
    cardEffect = 0
    cardPosition = 0
    def cardAlive(self):
        if cardHealth <= 0:
            #kill self
            cardHealth = 0
    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect()      

#All the cards


card1 = Card(pygame.image.load("backofcard.jpg"))
card1.cardHealth = 1
card1.cardAttack = 1
card1.cardCost = 1
card1.cardTexture = 1
card1.cardEffect = 1
card1.cardPosition = 0

deck1 = Deck()

FieldCards = [deck1, deck2, deck3, deck4]


#turns
Turn = 0
while Turn == 0:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for d in FieldCards[]:    
            if deck1.image.get_rect().collidepoint(pygame.mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN: 
                    if deck1.cardPosition == 0:
                        print("Where do you want to place?")
                    if deck1.cardPosition == 1:
                        print("Who do you want to attack?")
                    
                    if deck1.cardPosition
        
        time.sleep(0.03)
        pygame.display.update()  
