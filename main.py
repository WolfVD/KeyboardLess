import pygame, sys, random
pygame.init()

#region variable_setup
running = True
menuSetup = True
menu = True
typingSetup = False
typing = False
timer = False

currentText = None
currentX = None
currentY = None
currentRect = None
letterText = None
letterX = None
letterY = None
letterRect = None
currentAcc = None

letter = "A"
currentString = ""
counter = 1
word = ""
start_ticks = 0
accuracy = 100
#endregion variable_setup

screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption('KeyboardLess') 

#region font_setup
Fboldsmall = pygame.font.Font("Raleway-Bold.ttf", 100)
Fboldbig = pygame.font.Font("Raleway-Bold.ttf", 180)
Fregsmall = pygame.font.Font("Raleway-Regular.ttf", 40)
Fregmedium = pygame.font.Font("Raleway-Regular.ttf", 60)
Fregbig = pygame.font.Font("Raleway-Regular.ttf", 80)
#endregion font_setup

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT):
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if quitRect.collidepoint(mousePos) and menu == True:
                    running = False
                if startRect.collidepoint(mousePos) and menu == True:
                    typingSetup = True
                    menu = False
            elif event.button == 2:
                currentString = currentString[:counter-1] + letter + currentString[counter:]
                counter+=1

                currentText.fill((0,0,0))
                screen.blit(currentText, (currentX-(currentRect.width/2),currentY-(currentRect.height/2)))
                currentText = Fboldsmall.render(currentString, True, (255,255,255))
                currentX = 960
                currentY = 850
                currentRect = currentText.get_rect()
                currentRect.x = currentX-(currentRect.width/2)
                currentRect.y = currentY-(currentRect.height/2)
                screen.blit(currentText, (currentX-(currentRect.width/2),currentY-(currentRect.height/2)))

                intended = word[counter-2].lower()
                actual = letter.lower()
                tempAcc = 100-(abs(ord(intended)-ord(actual))*25)
                if tempAcc < 0:
                    tempAcc = 0

                accuracy = accuracy + ((tempAcc-accuracy)/(counter-1))

                currentAcc.fill((0,0,0))
                screen.blit(currentAcc, (20,70))
                currentAcc = Fregsmall.render("Accuracy: " + str(round(accuracy,2)) + "%", True, (255,255,255))
                screen.blit(currentAcc, (20,70))

                if counter == len(word):
                    exit()

            elif event.button == 4 and typing == True:
                if timer == True:
                    start_ticks=pygame.time.get_ticks()
                    timer = False
                num = (ord(letter)-63)
                if num == 27:
                    num = 1
                letter = chr(num+64)

                letterText.fill((0,0,0))
                screen.blit(letterText, (letterX-(letterRect.width/2),letterY-(letterRect.height/2)))
                letterText = Fboldbig.render(letter, True, (255, 255, 255))
                letterX = 960
                letterY = 540
                letterRect = letterText.get_rect()
                letterRect.x = letterX-(letterRect.width/2)
                letterRect.y = letterY-(letterRect.height/2)
                screen.blit(letterText, (letterX-(letterRect.width/2),letterY-(letterRect.height/2)))

            elif event.button == 5 and typing == True:
                if timer == True:
                    start_ticks=pygame.time.get_ticks()
                    timer = False
                num = (ord(letter)-64)
                if num == 1:
                    num = 27
                letter = chr(num+63)

                letterText.fill((0,0,0))
                screen.blit(letterText, (letterX-(letterRect.width/2),letterY-(letterRect.height/2)))
                letterText = Fboldbig.render(letter, True, (255, 255, 255))
                letterX = 960
                letterY = 540
                letterRect = letterText.get_rect()
                letterRect.x = letterX-(letterRect.width/2)
                letterRect.y = letterY-(letterRect.height/2)
                screen.blit(letterText, (letterX-(letterRect.width/2),letterY-(letterRect.height/2)))


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

            letterText = Fboldbig.render(letter, True, (255, 255, 255))
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
        timer = True

    if menuSetup == True:
        screen.fill((0,0,0))
        screen.blit(quitText, (quitX-(quitRect.width/2),quitY-(quitRect.height/2)))
        screen.blit(startText, (startX-(startRect.width/2),startY-(startRect.height/2)))

        menuSetup = False
        menu = True

        pygame.display.update()
    
    if typing == True:
        if timer == False:
            seconds = (pygame.time.get_ticks()-start_ticks)/1000
            currentTime.fill((0,0,0))
            screen.blit(currentTime, (20,20))
            currentTime = Fregsmall.render("Time: " + str(seconds), True, (255,255,255))
            screen.blit(currentTime, (20,20))

        pygame.display.update()


pygame.quit()