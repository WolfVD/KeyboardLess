import pygame, sys, random
pygame.init()

running = True
menuSetup = True
menu = True
typingSetup = False
typing = False

screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption('KeyboardLess') 

Fboldsmall = pygame.font.Font("Raleway-Bold.ttf", 100)
Fboldbig = pygame.font.Font("Raleway-Bold.ttf", 180)
Fregsmall = pygame.font.Font("Raleway-Regular.ttf", 40)
Fregmedium = pygame.font.Font("Raleway-Regular.ttf", 60)
Fregbig = pygame.font.Font("Raleway-Regular.ttf", 80)

#region menu_text
quitText = Fboldsmall.render('QUIT', True, (255, 255, 255))
quitX = 960
quitY = 900
quitRect = quitText.get_rect()
quitRect.x = quitX-(quitRect.width/2)
quitRect.y = quitY-(quitRect.height/2)

startText = Fboldbig.render('START', True, (255, 255, 255))
startX = 960
startY = 540
startRect = startText.get_rect()
startRect.x = startX-(startRect.width/2)
startRect.y = startY-(startRect.height/2)
#endregion menu_text

f = open("words.txt", "r")
words=f.readlines()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if quitRect.collidepoint(mousePos) and menu == True:
                running = False
            if startRect.collidepoint(mousePos) and menu == True:
                typingSetup = True
                menu = False

    if typingSetup == True:
        for i in range(5):
            screen.fill((0,0,0))

            line = random.randint(0,990)
            word = words[line]

            currentString = "_"*(len(word)-1)

            goalText=Fregbig.render("Goal: " + word, True, (255,255,255))
            goalX = 960
            goalY = 100
            goalRect = goalText.get_rect()
            goalRect.x = goalX-(goalRect.width/2)
            goalRect.y = goalY-(goalRect.height/2)
            screen.blit(goalText, (goalX-(goalRect.width/2),goalY-(goalRect.height/2)))

            timeText=Fregmedium.render("<30 Seconds", True, (255,255,255))
            timeX = 960
            timeY = 200
            timeRect = timeText.get_rect()
            timeRect.x = timeX-(timeRect.width/2)
            timeRect.y = timeY-(timeRect.height/2)
            screen.blit(timeText, (timeX-(timeRect.width/2),timeY-(timeRect.height/2)))

            accText = Fregmedium.render("75% Accuracy", True, (255,255,255))
            accX = 960
            accY = 275
            accRect = accText.get_rect()
            accRect.x = accX-(accRect.width/2)
            accRect.y = accY-(accRect.height/2)
            screen.blit(accText, (accX-(accRect.width/2),accY-(accRect.height/2)))

            letterText = Fboldbig.render('A', True, (255, 255, 255))
            letterX = 960
            letterY = 540
            letterRect = letterText.get_rect()
            letterRect.x = letterX-(letterRect.width/2)
            letterRect.y = letterY-(letterRect.height/2)
            screen.blit(letterText, (letterX-(letterRect.width/2),letterY-(letterRect.height/2)))

            currentText = Fboldsmall.render(currentString, True, (255,255,255))
            currentX = 960
            currentY = 850
            currentRect = currentText.get_rect()
            currentRect.x = currentX-(currentRect.width/2)
            currentRect.y = currentY-(currentRect.height/2)
            screen.blit(currentText, (currentX-(currentRect.width/2),currentY-(currentRect.height/2)))

            currentTime = Fregsmall.render("Time: ", True, (255,255,255))
            screen.blit(currentTime, (20,20))
            currentAcc = Fregsmall.render("Accuracy: ", True, (255,255,255))
            screen.blit(currentAcc, (20,70))

            pygame.display.update()

            pygame.time.wait(50-(i*10))

        typingSetup = False
        typing = True

    if menuSetup == True:
        screen.fill((0,0,0))
        screen.blit(quitText, (quitX-(quitRect.width/2),quitY-(quitRect.height/2)))
        screen.blit(startText, (startX-(startRect.width/2),startY-(startRect.height/2)))

        menuSetup = False
        menu = True

        pygame.display.update()


pygame.quit()