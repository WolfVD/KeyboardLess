import pygame, sys
import pygame.freetype
pygame.init()

running = True

screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption('KeyboardLess') 
screen.fill((255,255,255))

basicFont = pygame.font.SysFont(None, 100)

quitText = basicFont.render('QUIT', True, (0, 0, 0))

quitX = 875
quitY = 850
screen.blit(quitText, (quitX,quitY))
quitRect = quitText.get_rect()
quitRect.x = quitX
quitRect.y = quitY


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if quitRect.collidepoint(mousePos):
                running = False

    pygame.display.update()

pygame.quit()