import pygame
import sys, title_screen
from pygame import mixer
from clases.Music import Music

def credits(cursor, controller):
    music = Music()
    music.credits()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/credits_screen.png")

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    title_screen.title_screen(cursor.x, cursor.y, controller)

            if event.type == pygame.JOYBUTTONDOWN:
                title_screen.title_screen(cursor.x, cursor.y, controller)

        screen.blit(background, [0 , 0])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
