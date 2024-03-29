import pygame, time, sys, random, socket
pygame.init()

class Card(pygame.sprite.Sprite):
    """The card class that will be used to give every card an ID""" 
    cardID = 0
    cardCost = 0
    cardAttack = 0
    cardHealth = 0
    cardEffect = 0
    handPosition=0
    cardPosition=(0,0)
    highlighted = False
    cardUsed = 0
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
card2.cardID = 2
card2.cardCost = 2
card2.cardAttack = 2
card2.cardHealth = 3

card3 = Card(pygame.image.load('2mana23.png'))
card3.cardID = 3
card3.cardCost = 2
card3.cardAttack = 2
card3.cardHealth = 3

card4 = Card(pygame.image.load('2mana23.png'))
card4.cardID = 4
card4.cardCost = 2
card4.cardAttack = 2
card4.cardHealth = 3

card5 = Card(pygame.image.load('2mana23.png'))
card5.cardID = 5
card5.cardCost = 2
card5.cardAttack = 2
card5.cardHealth = 3

card6 = Card(pygame.image.load('2mana23.png'))
card6.cardID = 6
card6.cardCost = 2
card6.cardAttack = 2
card6.cardHealth = 3

card7 = Card(pygame.image.load('2mana23.png'))
card7.cardID = 7
card7.cardCost = 2
card7.cardAttack = 2
card7.cardHealth = 3

card8 = Card(pygame.image.load('2mana23.png'))
card8.cardID = 8
card8.cardCost = 2
card8.cardAttack = 2
card8.cardHealth = 3

card9 = Card(pygame.image.load('2mana23.png'))
card9.cardID = 9
card9.cardCost = 2
card9.cardAttack = 2
card9.cardHealth = 3

card10 = Card(pygame.image.load('2mana23.png'))
card10.cardID = 10
card10.cardCost = 2
card10.cardAttack = 2
card10.cardHealth = 3

card11 = Card(pygame.image.load('2mana23.png'))
card11.cardID = 11
card11.cardCost = 2
card11.cardAttack = 2
card11.cardHealth = 3

card12 = Card(pygame.image.load('2mana23.png'))
card12.cardID = 12
card12.cardCost = 2
card12.cardAttack = 2
card12.cardHealth = 3

card13 = Card(pygame.image.load('2mana23.png'))
card13.cardID = 13
card13.cardCost = 2
card13.cardAttack = 2
card13.cardHealth = 3

card14 = Card(pygame.image.load('2mana23.png'))
card14.cardID = 14
card14.cardCost = 2
card14.cardAttack = 2
card14.cardHealth = 3

card15 = Card(pygame.image.load('2mana23.png'))
card15.cardID = 15
card15.cardCost = 2
card15.cardAttack = 2
card15.cardHealth = 3

card16 = Card(pygame.image.load('2mana23.png'))
card16.cardID = 16
card16.cardCost = 2
card16.cardAttack = 2
card16.cardHealth = 3

card17 = Card(pygame.image.load('2mana23.png'))
card17.cardID = 17
card17.cardCost = 2
card17.cardAttack = 2
card17.cardHealth = 3

card18 = Card(pygame.image.load('2mana23.png'))
card18.cardID = 18
card18.cardCost = 2
card18.cardAttack = 2
card18.cardHealth = 3

card19 = Card(pygame.image.load('2mana23.png'))
card19.cardID = 19
card19.cardCost = 2
card19.cardAttack = 2
card19.cardHealth = 3

card20 = Card(pygame.image.load('2mana23.png'))
card20.cardID = 20
card20.cardCost = 2
card20.cardAttack = 2
card20.cardHealth = 3

ecard1 = Card(pygame.image.load('2mana23.png'))
ecard1.cardID = 1
ecard1.cardCost = 2
ecard1.cardAttack = 2
ecard1.cardHealth = 3

ecard2 = Card(pygame.image.load('2mana23.png'))
ecard2.cardID = 2
ecard2.cardCost = 2
ecard2.cardAttack = 2
ecard2.cardHealth = 3

ecard3 = Card(pygame.image.load('2mana23.png'))
ecard3.cardID = 3
ecard3.cardCost = 2
ecard3.cardAttack = 2
ecard3.cardHealth = 3

ecard4 = Card(pygame.image.load('2mana23.png'))
ecard4.cardID = 4
ecard4.cardCost = 2
ecard4.cardAttack = 2
ecard4.cardHealth = 3

ecard5 = Card(pygame.image.load('2mana23.png'))
ecard5.cardID = 5
ecard5.cardCost = 2
ecard5.cardAttack = 2
ecard5.cardHealth = 3

ecard6 = Card(pygame.image.load('2mana23.png'))
ecard6.cardID = 6
ecard6.cardCost = 2
ecard6.cardAttack = 2
ecard6.cardHealth = 3

ecard7 = Card(pygame.image.load('2mana23.png'))
ecard7.cardID = 7
ecard7.cardCost = 2
ecard7.cardAttack = 2
ecard7.cardHealth = 3

ecard8 = Card(pygame.image.load('2mana23.png'))
ecard8.cardID = 8
ecard8.cardCost = 2
ecard8.cardAttack = 2
ecard8.cardHealth = 3

ecard9 = Card(pygame.image.load('2mana23.png'))
ecard9.cardID = 9
ecard9.cardCost = 2
ecard9.cardAttack = 2
ecard9.cardHealth = 3

ecard10 = Card(pygame.image.load('2mana23.png'))
ecard10.cardID = 10
ecard10.cardCost = 2
ecard10.cardAttack = 2
ecard10.cardHealth = 3

ecard11 = Card(pygame.image.load('2mana23.png'))
ecard11.cardID = 11
ecard11.cardCost = 2
ecard11.cardAttack = 2
ecard11.cardHealth = 3

ecard12 = Card(pygame.image.load('2mana23.png'))
ecard12.cardID = 12
ecard12.cardCost = 2
ecard12.cardAttack = 2
ecard12.cardHealth = 3

ecard13 = Card(pygame.image.load('2mana23.png'))
ecard13.cardID = 13
ecard13.cardCost = 2
ecard13.cardAttack = 2
ecard13.cardHealth = 3

ecard14 = Card(pygame.image.load('2mana23.png'))
ecard14.cardID = 14
ecard14.cardCost = 2
ecard14.cardAttack = 2
ecard14.cardHealth = 3

ecard15 = Card(pygame.image.load('2mana23.png'))
ecard15.cardID = 15
ecard15.cardCost = 2
ecard15.cardAttack = 2
ecard15.cardHealth = 3

ecard16 = Card(pygame.image.load('2mana23.png'))
ecard16.cardID = 16
ecard16.cardCost = 2
ecard16.cardAttack = 2
ecard16.cardHealth = 3

ecard17 = Card(pygame.image.load('2mana23.png'))
ecard17.cardID = 17
ecard17.cardCost = 2
ecard17.cardAttack = 2
ecard17.cardHealth = 3

ecard18 = Card(pygame.image.load('2mana23.png'))
ecard18.cardID = 18
ecard18.cardCost = 2
ecard18.cardAttack = 2
ecard18.cardHealth = 3

ecard19 = Card(pygame.image.load('2mana23.png'))
ecard19.cardID = 19
ecard19.cardCost = 2
ecard19.cardAttack = 2
ecard19.cardHealth = 3

ecard20 = Card(pygame.image.load('2mana23.png'))
ecard20.cardID = 20
ecard20.cardCost = 2
ecard20.cardAttack = 2
ecard20.cardHealth = 3

#start of code

nullcard = Card(pygame.image.load('2mana23.png'))
selected = nullcard 
highlight = pygame.image.load("HIGHLIGHT.png")
highlighted = nullcard
FieldCards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20]
gameBoard = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
white = (255, 255, 255)
X = 1680
Y = 1050
display_surface = pygame.display.set_mode((X, Y ), pygame.FULLSCREEN)
pygame.display.set_caption('Hearthstone Beta')
board = pygame.image.load('board.jpg')
player1 = Player()
player2 = Player()
deck = FieldCards.copy()
random.shuffle(deck)

def render_gameboard():
    # base game board works :)
    display_surface.fill(white)
    display_surface.blit(board, (0, 0))

    # render cards already existing
    p=0
    while p<14:
        if p==1:
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
        p+=1
    while p<21:
        if p==1:
            display_surface.blit(ecard1.image, ecard1.cardPosition)
        elif p==2:
            display_surface.blit(ecard2.image, ecard2.cardPosition)
        elif p==3:
            display_surface.blit(ecard3.image, ecard3.cardPosition)
        elif p==4:
            display_surface.blit(ecard4.image, ecard4.cardPosition)
        elif p==5:
            display_surface.blit(ecard5.image, ecard5.cardPosition)
        elif p==6:
            display_surface.blit(ecard6.image, ecard6.cardPosition)
        elif p==7:
            display_surface.blit(ecard7.image, ecard7.cardPosition)
        elif p==8:
            display_surface.blit(ecard8.image, ecard8.cardPosition)
        elif p==9:
            display_surface.blit(ecard9.image, ecard9.cardPosition)
        elif p==10:
            display_surface.blit(ecard10.image, ecard10.cardPosition)
        elif p==11:
            display_surface.blit(ecard11.image, ecard11.cardPosition)
        elif p==12:
            display_surface.blit(ecard12.image, ecard12.cardPosition)
        elif p==13:
            display_surface.blit(ecard13.image, ecard13.cardPosition)
        elif p==14:
            display_surface.blit(ecard14.image, ecard14.cardPosition)
        elif p==15:
            display_surface.blit(ecard15.image, ecard15.cardPosition)
        elif p==16:
            display_surface.blit(ecard16.image, ecard16.cardPosition)
        elif p==17:
            display_surface.blit(ecard17.image, ecard17.cardPosition)
        elif p==18:
            display_surface.blit(ecard18.image, ecard18.cardPosition)
        elif p==19:
            display_surface.blit(ecard19.image, ecard19.cardPosition)
        elif p==20:
            display_surface.blit(ecard20.image, ecard20.cardPosition)

    
    for c in FieldCards:
        if(c.highlighted): 
                display_surface.blit(highlight, c.cardPosition)

def draw():
    if gameBoard[0] == 0 :
        gameBoard[0] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[0] == x.cardID:
                x.cardPosition = hand1
                x.handPosition = 0
                break
    elif gameBoard[1] == 0 :
        gameBoard[1] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[1] == x.cardID:
                x.cardPosition = hand2
                x.handPosition = 1
                break
    elif gameBoard[2] == 0 :
        gameBoard[2] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[2] == x.cardID:
                x.cardPosition = hand3
                x.handPosition = 2
                break
    elif gameBoard[3] == 0 :
        gameBoard[3] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[3] == x.cardID:
                x.cardPosition = hand4
                x.handPosition = 3
                break
    elif gameBoard[4] == 0 :
        gameBoard[4] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[4] == x.cardID:
                x.cardPosition = hand5
                x.handPosition = 4
                break
    elif gameBoard[5] == 0 :
        gameBoard[5] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[5] == x.cardID:
                x.cardPosition = hand6
                x.handPosition = 5
                break
    elif gameBoard[6] == 0 :
        gameBoard[6] = deck.pop().cardID
        for x in FieldCards:
            if gameBoard[6] == x.cardID:
                x.cardPosition = hand7
                x.handPosition = 6
                break    


while True :
    render_gameboard()
    draw()

    playerTurn=True
    if player1.maxMana<10:
        player1.maxMana+=1
    for c in FieldCards:
        c.cardUsed = 0
    player1.currentMana=player1.maxMana
    #player1 turn
    while playerTurn:
        render_gameboard()
        # check for player input
        for event in pygame.event.get():
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    playerTurn = False
                    selected = nullcard
                    for x in FieldCards:
                        x.highlighted=False
                elif event.key == pygame.K_ESCAPE:                
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                for c in FieldCards:
                    pos = pygame.mouse.get_pos()
                    if c.image.get_rect(center=(c.cardPosition[0]+100,c.cardPosition[1]+125)).collidepoint(pos):
                        if c.cardPosition != (0,0):
                            display_surface.blit(highlight, c.cardPosition)
                            selected.highlighted = False 
                            c.highlighted= True
                            selected = c
                if selected != nullcard:
                    if player1.currentMana >= selected.cardCost:       
                        if gameBoard[7] == 0:
                            if pos[0] > 50 and pos[0] < 250 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board1 
                                gameBoard[7] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[8] == 0:
                            if pos[0] > 266 and pos[0] < 466 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board2 
                                gameBoard[8] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[9] == 0:
                            if pos[0] > 482 and pos[0] < 682 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board3 
                                gameBoard[9] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[10] == 0:
                            if pos[0] > 696 and pos[0] < 896 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board4 
                                gameBoard[10] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[11] == 0:
                            if pos[0] > 909 and pos[0] < 1109 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board5 
                                gameBoard[11] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[12] == 0:
                            if pos[0] > 1123 and pos[0] < 1323 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board6 
                                gameBoard[12] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                        if gameBoard[13] == 0:
                            if pos[0] > 1336 and pos[0] < 1536 and pos[1] > 389 and pos[1] < 639:            
                                gameBoard[selected.handPosition] = 0
                                selected.cardPosition = board7 
                                gameBoard[13] = selected.cardID
                                player1.currentMana -= selected.cardCost
                                cardUsed = 1
                                selected = nullcard
                                for x in FieldCards:
                                    x.highlighted=False
                    if selected.cardUsed == 0:
                        if gameBoard[14] != 0:
                            if pos[0] > 50 and pos[0] < 250 and pos[1] > 128 and pos[1] < 378:
                                #selected.cardHealth-= opponent.cardAttack
                                #opponent.cardhealth-= selected.cardHealth
                                break

            if event.type == pygame.QUIT : 
                pygame.quit()        
                sys.exit()
                
        pygame.display.update()
    pygame.display.update()