import pygame, Buttons, os, screen, random

from pygame.locals import *

#Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1000,750),0,32)

#pictures
background_1_filename = "1.png"
background_2_filename = '2.png'
background_3_filename = '3.png'
background_4_filename = '4.png'
background_5_filename = '5.png'
background_6_filename = '6.png'



class Button_Example:
    def __init__(self):
        self.main()
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((725,750),0,32)
        pygame.display.set_caption("Kendall's Battle Dice")




    #Update the game display and show the button
    def game_display(self, dice1, dice2, playerap, aiap, playermultiplier, aimultiplier, invalidmove, playerhp, aihp, playerattack, aiattack, playerblock, aiblock, playerwin, aiwin):
        self.screen.fill((255,255,255))
        font1 = pygame.font.Font(os.path.join("Times_New_Roman_Normal.ttf"),24)
        choosemove = font1.render("Choose Your Move:",True,(0,0,0))
        instructions = font1.render("Instructions:",True,(0,0,0))
        multiplierdesc = font1.render("Multiplier doubles when you block, and resets when you do nothing.",True,(0,0,0))
        apdesc = font1.render("AP is your action points you gain AP everytime the dice rolls.",True,(0,0,0))
        hpdesc = font1.render("HP is your health points, if it hits zero you lose.",True,(0,0,0))
        attackdesc = font1.render("Deal 5 damage, negates opponents attack, and can be blocked.",True,(0,0,0))
        blockdesc = font1.render("Blocks any attacks, doubles multiplier",True,(0,0,0))

        invalidmove1 = font1.render("Invalid Move!",True,(255,0,0))
        playerwin1 = font1.render("Player Won!",True,(255,0,0))
        aiwin1 = font1.render("You Lose!",True,(255,0,0))

        if playerwin == True:
            screen.blit(playerwin1, (25, 345))
        if aiwin == True:
            screen.blit(aiwin1, (25, 345))

        multiplier1 = font1.render("Multiplier:",True,(0,0,0))
        multiplier2 = font1.render("%d" %playermultiplier,True,(0,0,0))
        aimultiplier1 = font1.render("AI Multiplier:",True,(0,0,0))
        aimultiplier2 = font1.render("%d" %aimultiplier,True,(0,0,0))
        playerap1 = font1.render("Player AP:",True,(0,0,0))
        playerap2 = font1.render("%d" %playerap,True,(0,0,0))
        aiap1 = font1.render("AI AP:",True,(0,0,0)) 
        aiap2 = font1.render("%d" %aiap,True,(0,0,0)) 

        playerhp1 = font1.render("HP:",True,(0,0,0)) 
        playerhp2 = font1.render("%d" %playerhp,True,(0,0,0)) 

        aihp1 = font1.render("AI HP:",True,(0,0,0)) 
        aihp2 = font1.render("%d" %aihp,True,(0,0,0)) 

        one = pygame.image.load(background_1_filename).convert_alpha()
        two = pygame.image.load(background_2_filename).convert_alpha()
        three = pygame.image.load(background_3_filename).convert_alpha()
        four = pygame.image.load(background_4_filename).convert_alpha()
        five = pygame.image.load(background_5_filename).convert_alpha()
        six = pygame.image.load(background_6_filename).convert_alpha()

        #Parameters:               surface,      color,  x,   y, length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (0,0,0), 200, 405, 150,    100,    0,        "Do Nothing, 0 AP", (255,255,255))
        self.Button2.create_button(self.screen, (0,0,0), 360, 405, 150,    100,    0,        "Block, %d AP" %playermultiplier, (255,255,255))
        self.Button3.create_button(self.screen, (0,0,0), 40, 405, 150,    100,    0,        "Attack, 5 AP", (255,255,255))
        self.Button4.create_button(self.screen, (0,0,0), 520, 405, 150,    100,    0,        "Quit", (255,255,255))
        screen.blit(choosemove, (25, 365))
        
        if invalidmove == True:
            screen.blit(invalidmove1, (25, 345))

        screen.blit(instructions, (15, 0))
        screen.blit(multiplierdesc, (15, 25))
        screen.blit(apdesc, (15, 55))  
        screen.blit(hpdesc, (15, 85))    
        screen.blit(attackdesc, (15, 115))          
        screen.blit(blockdesc, (15, 145))          


        screen.blit(aimultiplier1, (500, 525))
        screen.blit(aimultiplier2, (675, 525))

        screen.blit(multiplier1, (25, 525))
        screen.blit(multiplier2, (150, 525))


        screen.blit(playerap1, (25, 555))
        screen.blit(playerap2, (150, 555))

        screen.blit(aiap1, (500, 555))       
        screen.blit(aiap2, (675, 555))

        screen.blit(playerhp1, (25, 585))
        screen.blit(playerhp2, (150, 585))
        screen.blit(aihp1, (500, 585)) 
        screen.blit(aihp2, (675, 585))


        if dice1 == 1:
            screen.blit(one, (200,200))
        elif dice1 == 2:
            screen.blit(two, (200,200))   
        elif dice1 == 3:
            screen.blit(three, (200,200))
        elif dice1 == 4:
            screen.blit(four, (200,200))   
        elif dice1 == 5:
            screen.blit(five, (200,200))
        elif dice1 == 6:
            screen.blit(six, (200,200))
        if dice2 == 1:    
            screen.blit(one, (400,200))
        elif dice2 == 2:
            screen.blit(two, (400,200))   
        elif dice2 == 3:
            screen.blit(three, (400,200))
        elif dice2 == 4:
            screen.blit(four, (400,200))   
        elif dice2 == 5:
            screen.blit(five, (400,200))
        elif dice2 == 6:
            screen.blit(six, (400,200))

        pygame.display.flip()




    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.Button3 = Buttons.Button()
        self.Button4 = Buttons.Button()
        #variables
        aihp = 20
        playerhp = 20
        aiap = 0
        playerap = 0
        aimultiplier = 1
        playermultiplier = 1
        dice1 = 1 
        dice2 = 1
        invalidmove = False
        playerattack = 0
        aiattack = 0
        playerblock = False
        aiblock = False
        playerwin = False
        aiwin = False
        #initialize dice
        dice1 = random.randint(1,6) 
        dice2 = random.randint(1,6)
        playerap += dice1
        aiap += dice2 

        self.display()
        while True:
            self.game_display(dice1, dice2, playerap, aiap, playermultiplier, aimultiplier, invalidmove, playerhp, aihp, playerattack, aiattack, playerblock, aiblock, playerwin, aiwin)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    #reset wins
                    if playerwin == True:
                        playerwin = False
                    if aiwin == True:    
                        aiwin = False
                    #Do nothing Button
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        playermultiplier = 1
                        invalidmove = False

                    #Block Button
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        if playermultiplier < playerap:
                            invalidmove = False
                            playerap -= playermultiplier
                            playermultiplier = playermultiplier * 2
                            playerblock = True
                        elif playermultiplier > playerap:
                            invalidmove = True
                            print "invalid move!"
                        
                    #attack button
                    if self.Button3.pressed(pygame.mouse.get_pos()):
                        print "attack!"
                        if playerap > 5:
                            playerattack = 5
                            playerap -= 5
                            invalidmove = False
                        elif playerap < 5:
                            invalidmove = True

                    #quit button
                    if self.Button4.pressed(pygame.mouse.get_pos()):
                        pygame.quit()

                    #roll dice if any button but quit is pushed, also AI moves
                    if (self.Button1.pressed(pygame.mouse.get_pos()) or self.Button2.pressed(pygame.mouse.get_pos()) or self.Button3.pressed(pygame.mouse.get_pos())) and invalidmove == False:
                        #ai moves
                        #if ai has enough ap to attack
                        if aiap > 5:
                            aimove = random.randint(1,10)
                            # 50% chance to attack
                            if aimove > 5:
                                aiattack = 5
                                aiap -= 5
                            #30% chance to block    
                            elif playerap > 5 and (aiap > aimultiplier) and aimove > 2:
                                aiap -= aimultiplier
                                aimultiplier = aimultiplier * 2
                                aiblock = True
                            #20% chance to reset multiplier    
                            else:
                                aimultiplier = 1
                            


                        #damage calculations
                        if playerattack == 5 and aiattack == 5:
                            print "attacks cancel eachother!"
                        elif playerattack == 5 and aiattack == 0 and aiblock == False:
                            aihp -= 5
                        elif aiattack == 5 and playerattack == 0 and playerblock == False:
                            playerhp -= 5

                        #check for winner
                        if playerhp <= 0:
                            aiwin = True
                            #reset variables for next game
                            aihp = 20
                            playerhp = 20
                            aiap = 0
                            playerap = 0
                            aimultiplier = 1
                            playermultiplier = 1
                            dice1 = 1 
                            dice2 = 1
                            invalidmove = False
                            playerattack = 0
                            aiattack = 0
                            playerblock = False
                            aiblock = False

                        if aihp <= 0:
                            playerwin = True                             
                            #reset variables for next game
                            aihp = 20
                            playerhp = 20
                            aiap = 0
                            playerap = 0
                            aimultiplier = 1
                            playermultiplier = 1
                            dice1 = 1 
                            dice2 = 1
                            invalidmove = False
                            playerattack = 0
                            aiattack = 0
                            playerblock = False
                            aiblock = False


                        #reset values after calculation   
                        playerblock = False
                        aiblock = False
                        aiattack = 0
                        playerattack = 0
                        aiattack = 0

                        #roll next move
                        dice1 = random.randint(1,6) 
                        dice2 = random.randint(1,6)
                        playerap += dice1
                        aiap += dice2
                        #update screen    
                        self.game_display(dice1, dice2, playerap, aiap, playermultiplier, aimultiplier, invalidmove, playerhp, aihp, playerattack, aiattack, playerblock, aiblock, playerwin, aiwin)
                             




if __name__ == '__main__':
    obj = Button_Example()
