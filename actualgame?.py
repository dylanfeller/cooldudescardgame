import pygame, time, sys, random
pygame.init()

class Card(pygame.sprite.Sprite):
    """The card class that will be used to give every card an ID""" 
    cardID = 0
    cardCost = 0
    cardAttack = 0
    cardHealth = 0
    cardEffect = 0
    cardPosition=(0,0)
    highlighted = False
    def cardAlive(self):
        if cardHealth <= 0:
            return False
    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect(center=(self.cardPosition[0]+100, self.cardPosition[1]+125))
    def update(self):
        self.rect = self.image.get_rect(center=(self.cardPosition[0]+100, self.cardPosition[1]+125))

class Player:
    maxMana = 0
    currentMana = 0
    health = 30



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

card1 = Card(pygame.image.load('2mana23.png'))
card1.cardID = 1
card1.cardCost = 2
card1.cardAttack = 2
card1.cardHealth = 3

card2 = Card(pygame.image.load('2mana23.png'))
card2.cardID = 1
card2.cardCost = 2
card2.cardAttack = 2
card2.cardHealth = 3

card3 = Card(pygame.image.load('2mana23.png'))
card3.cardID = 1
card3.cardCost = 2
card3.cardAttack = 2
card3.cardHealth = 3

card4 = Card(pygame.image.load('2mana23.png'))
card4.cardID = 1
card4.cardCost = 2
card4.cardAttack = 2
card4.cardHealth = 3

card5 = Card(pygame.image.load('2mana23.png'))
card5.cardID = 1
card5.cardCost = 2
card5.cardAttack = 2
card5.cardHealth = 3

card6 = Card(pygame.image.load('2mana23.png'))
card6.cardID = 1
card6.cardCost = 2
card6.cardAttack = 2
card6.cardHealth = 3

card7 = Card(pygame.image.load('2mana23.png'))
card7.cardID = 1
card7.cardCost = 2
card7.cardAttack = 2
card7.cardHealth = 3

card8 = Card(pygame.image.load('2mana23.png'))
card8.cardID = 1
card8.cardCost = 2
card8.cardAttack = 2
card8.cardHealth = 3

card9 = Card(pygame.image.load('2mana23.png'))
card9.cardID = 1
card9.cardCost = 2
card9.cardAttack = 2
card9.cardHealth = 3

card10 = Card(pygame.image.load('2mana23.png'))
card10.cardID = 1
card10.cardCost = 2
card10.cardAttack = 2
card10.cardHealth = 3

card11 = Card(pygame.image.load('2mana23.png'))
card11.cardID = 1
card11.cardCost = 2
card11.cardAttack = 2
card11.cardHealth = 3

card12 = Card(pygame.image.load('2mana23.png'))
card12.cardID = 1
card12.cardCost = 2
card12.cardAttack = 2
card12.cardHealth = 3

card13 = Card(pygame.image.load('2mana23.png'))
card13.cardID = 1
card13.cardCost = 2
card13.cardAttack = 2
card13.cardHealth = 3

card14 = Card(pygame.image.load('2mana23.png'))
card14.cardID = 1
card14.cardCost = 2
card14.cardAttack = 2
card14.cardHealth = 3

card15 = Card(pygame.image.load('2mana23.png'))
card15.cardID = 1
card15.cardCost = 2
card15.cardAttack = 2
card15.cardHealth = 3

card16 = Card(pygame.image.load('2mana23.png'))
card16.cardID = 1
card16.cardCost = 2
card16.cardAttack = 2
card16.cardHealth = 3

card17 = Card(pygame.image.load('2mana23.png'))
card17.cardID = 1
card17.cardCost = 2
card17.cardAttack = 2
card17.cardHealth = 3

card18 = Card(pygame.image.load('2mana23.png'))
card18.cardID = 1
card18.cardCost = 2
card18.cardAttack = 2
card18.cardHealth = 3

card19 = Card(pygame.image.load('2mana23.png'))
card19.cardID = 1
card19.cardCost = 2
card19.cardAttack = 2
card19.cardHealth = 3

card20 = Card(pygame.image.load('2mana23.png'))
card20.cardID = 1
card20.cardCost = 2
card20.cardAttack = 2
card20.cardHealth = 3


nullcard = Card(pygame.image.load('2mana23.png'))
selected = nullcard 
highlight = pygame.image.load("HIGHLIGHT.png")
highlighted = nullcard
FieldCards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20]
gameBoard = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
white = (255, 255, 255)
X = 1680
Y = 1050
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Hearthstone Beta')
board = pygame.image.load('board.jpg')
player1 = Player()
player2 = Player()
deck = FieldCards
random.shuffle(deck)

def render_gameboard():
    # base game board
    display_surface.fill(white)
    display_surface.blit(board, (0, 0))

    # render cards already existing
    for p in gameBoard:
        if p==0:
            break
        elif p==1:
            display_surface.blit(card1.image, card1.cardPosition)
        elif p==2:
            display_surface.blit(card2.image, card2.cardPosition)
        elif p==3:
            display_surface.blit(card3.image, card3.cardPosition)
        elif p==4:
            display_surface.blit(card4.image, card4.cardPosition)
        elif p==5:
            display_surface.blit(card5.image, card5.cardPosition)
        elif p==6:
            display_surface.blit(card6.image, card6.cardPosition)
        elif p==7:
            display_surface.blit(card7.image, card7.cardPosition)
        elif p==8:
            display_surface.blit(card8.image, card8.cardPosition)
        elif p==9:
            display_surface.blit(card9.image, card9.cardPosition)
        elif p==10:
            display_surface.blit(card10.image, card10.cardPosition)
        elif p==11:
            display_surface.blit(card11.image, card11.cardPosition)
        elif p==12:
            display_surface.blit(card12.image, card12.cardPosition)
        elif p==13:
            display_surface.blit(card13.image, card13.cardPosition)
        elif p==14:
            display_surface.blit(card14.image, card14.cardPosition)
        elif p==15:
            display_surface.blit(card15.image, card15.cardPosition)
        elif p==16:
            display_surface.blit(card16.image, card16.cardPosition)
        elif p==17:
            display_surface.blit(card17.image, card17.cardPosition)
        elif p==18:
            display_surface.blit(card18.image, card18.cardPosition)
        elif p==19:
            display_surface.blit(card19.image, card19.cardPosition)
        elif p==20:
            display_surface.blit(card20.image, card20.cardPosition)

    # player turn
    # draw
    if gameBoard[0] == 0 :
        gameBoard[0] = deck.pop().cardID
    elif gameBoard[1] == 0 :
        gameBoard[1] = deck.pop().cardID
    elif gameBoard[2] == 0 :
        gameBoard[2] = deck.pop().cardID
    elif gameBoard[3] == 0 :
        gameBoard[3] = deck.pop().cardID
    elif gameBoard[4] == 0 :
        gameBoard[4] = deck.pop().cardID
    elif gameBoard[5] == 0 :
        gameBoard[5] = deck.pop().cardID
    elif gameBoard[6] == 0 :
        gameBoard[6] = deck.pop().cardID


while True :
    ev = pygame.event.get()
    render_gameboard()

    playerTurn=True
    if player1.maxMana<10:
        player1.maxMana+=1
    player1.currentMana=player1.maxMana
    while playerTurn:
        render_gameboard()
        # check for player input
        for event in ev:
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    playerTurn = False
                    selected = nullcard
            if event.type == pygame.MOUSEBUTTONUP:
                for c in FieldCards:
                    pos = pygame.mouse.get_pos()
                    if c.image.get_rect(center=(c.cardPosition[0]+100,c.cardPosition[1]+125)).collidepoint(pos):
                        display_surface.blit(highlight, c.cardPosition)
                        selected.highlighted = False
                        c.highlighted=not c.highlighted
                        selected = c
            pygame.display.update()
            for event in ev : 
                if event.type == pygame.QUIT : 
                    pygame.quit()        
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:                
                        pygame.quit()
                        sys.exit()