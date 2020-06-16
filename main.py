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
results = False

letter = "A"
currentString = ""
word = ""
counter = 1
start_ticks = 0
accuracy = 100
maxTime = 20
minAcc = 75
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
words = f.readlines()

def DisplayResults():
    screen.fill((0,0,0))

    if accuracy > minAcc and (pygame.time.get_ticks()-start_ticks)/1000<maxTime:
        resultText = Fboldbig.render("YOU WIN!", True, (33,204,78))
    else:
        resultText = Fboldbig.render("YOU LOSE :(", True, (224,22,22))
    resultX = 960
    resultY = 300
    resultRect = resultText.get_rect()
    resultRect.x = resultX-(resultRect.width/2)
    resultRect.y = resultY-(resultRect.height/2)
    screen.blit(resultText, (resultX-(resultRect.width/2),resultY-(resultRect.height/2)))

    resultAccText = Fregmedium.render("Accuracy  |  Required: " + str(minAcc) + "%    Actual: " + str(round(accuracy,2)) + "%", True, (255,255,255))
    resultAccX = 960
    resultAccY = 550
    resultAccRect = resultAccText.get_rect()
    resultAccRect.x = resultAccX-(resultAccRect.width/2)
    resultAccRect.y = resultAccY-(resultAccRect.height/2)
    screen.blit(resultAccText, (resultAccX-(resultAccRect.width/2),resultAccY-(resultAccRect.height/2)))

    resultTimeText = Fregmedium.render("Time  |  Required: " + str(maxTime) + "s    Actual: " + str(round((pygame.time.get_ticks()-start_ticks)/1000,3)) + "s", True, (255,255,255))
    resultTimeX = 960
    resultTimeY = 700
    resultTimeRect = resultTimeText.get_rect()
    resultTimeRect.x = resultTimeX-(resultTimeRect.width/2)
    resultTimeRect.y = resultTimeY-(resultTimeRect.height/2)
    screen.blit(resultTimeText, (resultTimeX-(resultTimeRect.width/2),resultTimeY-(resultTimeRect.height/2)))

    continueText = Fregsmall.render("Click anywhere to continue", True, (255,255,255))
    continueX = 960
    continueY = 900
    continueRect = continueText.get_rect()
    continueRect.x = continueX-(continueRect.width/2)
    continueRect.y = continueY-(continueRect.height/2)
    screen.blit(continueText, (continueX-(continueRect.width/2),continueY-(continueRect.height/2)))

    pygame.display.update()

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
                if results == True:
                    results = False
                    menuSetup = True
            elif event.button == 2 and typing == True:
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
                pygame.display.update()

                if counter == len(word):
                    typing = False
                    results = True
                    DisplayResults()

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

            timeText=Fregmedium.render("<" + str(maxTime) + " Seconds", True, (255,255,255))
            timeX = 960
            timeY = 200
            timeRect = timeText.get_rect()
            timeRect.x = timeX-(timeRect.width/2)
            timeRect.y = timeY-(timeRect.height/2)
            screen.blit(timeText, (timeX-(timeRect.width/2),timeY-(timeRect.height/2)))

            accText = Fregmedium.render(str(minAcc) + "% Accuracy", True, (255,255,255))
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
        counter = 1
        start_ticks = 0
        accuracy = 100

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