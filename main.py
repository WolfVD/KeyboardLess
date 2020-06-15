import pygame, sys
import pygame.freetype
pygame.init()

running = True

fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)

screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('KeyboardLess') 
screen.fill((255,255,255))

basicFont = pygame.font.SysFont(None, 100)

quitText = basicFont.render('QUIT', True, (0, 0, 0))
screen.blit(quitText, (900,850))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            print(mousePos)

    pygame.display.update()

pygame.quit()