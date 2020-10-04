# Rock Paper Scissors Game

import pygame,sys
from pygame.locals import *
import time
import random

pygame.init()

# Mokhtasat safhe namayesh
display_width = 700
display_height = 550

# farakhani safhe namayesh
gameDisplay = pygame.display.set_mode((display_width,display_height))

# tarif moteghayere rang
Black = (0,0,0)
White = (255,255,255)
Red = (200,0,0)
Bright_red = (255,0,0)
Green = (0,200,0)
Bright_green = (0,255,0)
Bright_Pink = (255, 192, 203)
Pink = (255, 51, 153)
Yellow = (255, 255, 0)


# gozashtan sartitr va nam baraye bazi
pygame.display.set_caption('Rock Paper Scissors')
pygame.mixer.music.load("Piano.wav")
pygame.mixer.music.play(-1)

def Intro():
    Intro = False
    while not Intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Intro = True
            gameDisplay.fill(White)
            myfont = pygame.font.Font('freesansbold.ttf', 60)
            myfont1 = pygame.font.Font('freesansbold.ttf', 20)
            text1 = myfont.render('Rock Paper Scissors', True, Black)
            gameDisplay.blit(text1, (50,10))
            startpic = pygame.image.load('pic.png').convert_alpha()
            gameDisplay.blit(startpic,(-50,80))
            text2 = myfont.render('Strat Game',True,Black)
            gameDisplay.blit(text2, (180,350))               
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 1 + 200 > mouse[0] > 1 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_green,(1,450,200,50))                
            else:
                pygame.draw.rect(gameDisplay,Green,(1,450,200,50))
            if 1 + 200 > mouse[0] > 1 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    Computer()
            text2 = myfont1.render('OnePlayer',True,Black)
            gameDisplay.blit(text2, (50,465))
            if 250 + 200 > mouse[0] > 250 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_Pink,(250,450,200,50))                
            else:
                pygame.draw.rect(gameDisplay,Pink,(250,450,200,50))
            if 250 + 200 > mouse[0] > 250 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    TwoPlayer()
            text2 = myfont1.render('TwoPlayer',True,Black)
            gameDisplay.blit(text2, (300,465))
            if 500 + 200 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_red,(500,450,200,50))
            else:
                pygame.draw.rect(gameDisplay,Red,(500,450,200,50))
            if 500 + 200 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    pygame.quit()
                    quit()                        
            text2 = myfont1.render('Quit',True,Black)
            gameDisplay.blit(text2, (580,465))
            pygame.display.update()


def Computer():    
    pic1 = pygame.image.load('rockwin1.png').convert_alpha()
    pic2 = pygame.image.load('paperwin2.png').convert_alpha()
    pic3 = pygame.image.load('rockrock.png').convert_alpha()
    rocklist = [pic1 , pic2 , pic3]
    pic4 = pygame.image.load('paperwin1.png').convert_alpha()
    pic5 = pygame.image.load('scissorswin2.png').convert_alpha()
    pic6 = pygame.image.load('paperpaper.png').convert_alpha()
    paperlist = [pic4 , pic5 , pic6]
    pic7 = pygame.image.load('scissorswin1.png').convert_alpha()
    pic8 = pygame.image.load('rockwin2.png').convert_alpha()
    pic9 = pygame.image.load('scissorsscissors.png').convert_alpha()
    scissorslist = [pic7 , pic8 , pic9]
    score1 = 0
    score2= 0
    
    clock = pygame.time.Clock()
    gameDisplay.fill(Black)
    while True:        
        gameDisplay.fill(Black , (75,65 ,50,20))
        gameDisplay.fill(Black , (635,65 ,50,20))  
        myfont = pygame.font.Font('freesansbold.ttf', 50)
        text1 = myfont.render('Player1',True,Red)
        gameDisplay.blit(text1,(0,10))        
        text1 = myfont.render('Computer',True,Red)
        gameDisplay.blit(text1,(440,10))
        mouse = pygame.mouse.get_pos()    
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(gameDisplay,Bright_green,(1,100,100,50))
        pygame.draw.rect(gameDisplay,Yellow,(1,155,100,50))
        pygame.draw.rect(gameDisplay,Pink,(1,210,100,50))
        pygame.draw.rect(gameDisplay,White,(105,155,150,50))
        myfont1 = pygame.font.Font('freesansbold.ttf', 20)
        text1 = myfont1.render('Rock',True,Black)
        gameDisplay.blit(text1,(28,115))        
        text1 = myfont1.render('Paper',True,Black)
        gameDisplay.blit(text1,(23,170))        
        text1 = myfont1.render('Scissors',True,Black)
        gameDisplay.blit(text1,(10,226))        
        text1 = myfont1.render('End Menu',True,Yellow)
        gameDisplay.blit(text1,(130,170))
        myfont2 = pygame.font.Font(None, 25)
        text1 = myfont1.render('Score',True,White)
        gameDisplay.blit(text1,(1,65))      
        text1 = myfont1.render('Score',True,White)
        gameDisplay.blit(text1,(560,65)) 
        text1 = myfont1.render(':',True,White)
        gameDisplay.blit(text1,(60,65))      
        text1 = myfont1.render(':',True,White)
        gameDisplay.blit(text1,(620,65))
        text1 = myfont2.render(f'{score1}',True,Pink)
        gameDisplay.blit(text1,(80,67))
        text1 = myfont2.render(f'{score2}',True,Pink)
        gameDisplay.blit(text1,(640,67))   
        img1 = random.choice(rocklist)
        img2 = random.choice(paperlist)
        img3 = random.choice(scissorslist)            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
            if 1 + 100 > mouse[0] > 1 and 100 + 50 > mouse[1] > 100:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img1 == pic1:
                            gameDisplay.blit(pic1 , (80 , 287))
                            score1 += 1
                            score2 += 0
            if 1 + 100 > mouse[0] > 1 and 100 + 50 > mouse[1] > 100:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img1 == pic2:
                            gameDisplay.blit(pic2 , (80 , 287))
                            score2 += 1
                            score1 += 0
            if 1 + 100 > mouse[0] > 1 and 100 + 50 > mouse[1] > 100:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:                                        
                        if img1 == pic3:
                            gameDisplay.blit(pic3 , (80 , 287))
                            score1 += 0
                            score2 += 0
            if 1 + 100 > mouse[0] > 1 and 155 + 50 > mouse[1] > 155:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img2 == pic4:
                            gameDisplay.blit(pic4 , (80 , 287))
                            score1 += 1
                            score2 += 0
            if 1 + 100 > mouse[0] > 1 and 155 + 50 > mouse[1] > 155:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img2 == pic5:
                            gameDisplay.blit(pic5 , (80 , 287))
                            score2 += 1
                            score1 += 0
            if 1 + 100 > mouse[0] > 1 and 155 + 50 > mouse[1] > 155:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img2 == pic6:
                            gameDisplay.blit(pic6 , (80 , 287))
                            score1 += 0
                            score2 += 0
            if 1 + 100 > mouse[0] > 1 and 210 + 50 > mouse[1] > 210:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img3 == pic7:
                            gameDisplay.blit(pic7 , (80 , 287))
                            score1 += 1
                            score2 += 0
            if 1 + 100 > mouse[0] > 1 and 210 + 50 > mouse[1] > 210:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img3 == pic8:
                            gameDisplay.blit(pic8 , (80 , 287))
                            score2 += 1
                            score1 += 0
            if 1 + 100 > mouse[0] > 1 and 210 + 50 > mouse[1] > 210:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if img3 == pic9:
                            gameDisplay.blit(pic9 , (80 , 287))
                            score1 += 0
                            score2 += 0
        if 105 + 150 > mouse[0] > 105 and 155 + 50 > mouse[1] > 155:
            if click[0] == 1:
                    GameExit()            
        pygame.display.update()            
        clock.tick(30)
def TwoPlayer():  
    score1 = 0
    score2= 0      
    pic1 = pygame.image.load('n1.png').convert_alpha()
    pic2 = pygame.image.load('n2.png').convert_alpha()
    pic3 = pygame.image.load('n3.png').convert_alpha()
    list1 = [pic1 , pic2 , pic3]    
    clock = pygame.time.Clock()
    gameDisplay.fill(Black)
    while True:         
        gameDisplay.fill(Black , (110,65 ,50,20))
        gameDisplay.fill(Black , (635,65 ,50,20))
        img1 = random.choice(list1)
        img2 = random.choice(list1)
        myfont = pygame.font.Font('freesansbold.ttf', 50)
        text1 = myfont.render('Player1',True,Pink)
        gameDisplay.blit(text1,(0,10))    
        text1 = myfont.render('Player2',True,Yellow)
        gameDisplay.blit(text1,(505,10))
        myfont1 = pygame.font.Font('freesansbold.ttf', 20)
        pygame.draw.rect(gameDisplay,Yellow,(1,100,150,50))
        pygame.draw.rect(gameDisplay,Pink,(545,100,150,50))
        pygame.draw.rect(gameDisplay,White,(60,68,15,15))
        pygame.draw.rect(gameDisplay,White,(77,68,15,15))
        pygame.draw.rect(gameDisplay,White,(589,68,15,15))
        pygame.draw.rect(gameDisplay,White,(606,68,15,15))
        pygame.draw.rect(gameDisplay,Bright_Pink,(280,200,150,50))
        text1 = myfont1.render('Choice 1',True,Black)
        gameDisplay.blit(text1,(30,115))    
        text1 = myfont1.render('Choice 2',True,Black)
        gameDisplay.blit(text1,(580,115))
        text1 = myfont1.render('End Menu',True,Black)
        gameDisplay.blit(text1,(308,215))        
        myfont2 = pygame.font.Font(None, 25)
        text1 = myfont1.render('Score',True,White)
        gameDisplay.blit(text1,(1,65))      
        text1 = myfont1.render('Score',True,White)
        gameDisplay.blit(text1,(530,65)) 
        text1 = myfont1.render(':',True,White)
        gameDisplay.blit(text1,(95,65))      
        text1 = myfont1.render(':',True,White)
        gameDisplay.blit(text1,(624,65))
        text1 = myfont1.render('+',True,Pink)
        gameDisplay.blit(text1,(79,64))      
        text1 = myfont1.render('-',True,Yellow)
        gameDisplay.blit(text1,(64,65))  
        text1 = myfont1.render('+',True,Pink)
        gameDisplay.blit(text1,(608,64))      
        text1 = myfont1.render('-',True,Yellow)
        gameDisplay.blit(text1,(593,65))
        text1 = myfont2.render(f'{score1}',True,Pink)
        gameDisplay.blit(text1,(110,67))
        text1 = myfont2.render(f'{score2}',True,Pink)
        gameDisplay.blit(text1,(640,67))
        mouse = pygame.mouse.get_pos()    
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if 1 + 150 > mouse[0] > 1 and 100 + 50 > mouse[1] > 100:            
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:                        
                        gameDisplay.blit(img1 , (0 , 275))                            
            if 545 + 150 > mouse[0] > 545 and 100 + 50 > mouse[1] > 100:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:                        
                        gameDisplay.blit(img2 , (430 , 275))

            
            if 60 + 15 > mouse[0] > 60 and 68 + 15 > mouse[1] > 68:            
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score1 -= 1
            if 77 + 15 > mouse[0] > 77 and 68 + 15 > mouse[1] > 68:            
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score1 += 1     

            if 589 + 15 > mouse[0] > 589 and 68 + 15 > mouse[1] > 68:            
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score2 -= 1
            if 606 + 15 > mouse[0] > 606 and 68 + 15 > mouse[1] > 68:            
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        score2 += 1   
            

        if 280 + 150 > mouse[0] > 280 and 200 + 50 > mouse[1] > 200:
            if click[0] == 1:
                    GameExit()
        pygame.display.update()
        clock.tick(60)
    
      


def GameExit():
    GameExit = False
    while not GameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True
            gameDisplay.fill(White)
            myfont = pygame.font.Font('freesansbold.ttf', 50)
            myfont1 = pygame.font.Font('freesansbold.ttf', 20)        
            endpic = pygame.image.load('endpic.png').convert_alpha()
            gameDisplay.blit(endpic,(230,60))
            text2 = myfont.render('Thanks For Using!',True,Black)
            gameDisplay.blit(text2, (120,300))               
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 1 + 200 > mouse[0] > 1 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_green,(1,450,200,50))                
            else:
                pygame.draw.rect(gameDisplay,Green,(1,450,200,50))
            if 1 + 200 > mouse[0] > 1 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    Computer()
            text2 = myfont1.render('OnePlayer',True,Black)
            gameDisplay.blit(text2, (50,465))
            if 250 + 200 > mouse[0] > 250 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_Pink,(250,450,200,50))                
            else:
                pygame.draw.rect(gameDisplay,Pink,(250,450,200,50))
            if 250 + 200 > mouse[0] > 250 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    TwoPlayer()
            text2 = myfont1.render('TwoPlayer',True,Black)
            gameDisplay.blit(text2, (300,465))
            if 500 + 200 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(gameDisplay,Bright_red,(500,450,200,50))
            else:
                pygame.draw.rect(gameDisplay,Red,(500,450,200,50))
            if 500 + 200 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    pygame.quit()
                    quit()                        
            text2 = myfont1.render('Quit',True,Black)
            gameDisplay.blit(text2, (580,465))
            pygame.display.update()
   
Intro()




