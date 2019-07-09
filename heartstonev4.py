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
            cardPosition = 2
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
deck1 = card1
deck2 = card1
#deck2 = Deck()
#deck3 = Deck()
#deck4 = Deck()

FieldCards = [deck1, deck2]

#turns
Turn = 0
while Turn == 0:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        for d in FieldCards:    
            if d.image.get_rect().collidepoint(pygame.mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN: 
                    if d.cardPosition == 0:
                        print ("1")
                    if d.cardPosition == 1:
                        print ("2")
                        
                    
                    
        
        time.sleep(0.03)
        pygame.display.update()  
