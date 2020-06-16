import pygame, sys
import pygame.freetype
pygame.init()

running = True
menuSetup = True
menu = True
typing = False

screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption('KeyboardLess') 

Fboldsmall = pygame.font.Font("Raleway-Bold.ttf", 100)
Fboldbig = pygame.font.Font("Raleway-Bold.ttf", 180)

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

#region typing_text


#endregion typing_text

words = open("words.txt", "r")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if quitRect.collidepoint(mousePos) and menu == True:
                running = False
            if startRect.collidepoint(mousePos) and menu == True:
                typing = True

    if typing == True:
        screen.fill((0,0,0))
        pygame.display.update()

    if menuSetup == True:
        screen.fill((0,0,0))
        screen.blit(quitText, (quitX-(quitRect.width/2),quitY-(quitRect.height/2)))
        screen.blit(startText, (startX-(startRect.width/2),startY-(startRect.height/2)))

        menuSetup = False
        menu = True

        pygame.display.update()


pygame.quit()