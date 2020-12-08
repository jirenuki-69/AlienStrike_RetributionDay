import pygame, sys, const, main_menu, loading
from pygame import mixer
from clases.Music import Music
from clases.Sound import Sound
from clases.Cursor import Cursor

def practice_splash_screen(cursor_x, cursor_y, controller):
    music = Music()
    music.splash_screen()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/splash/splash_screen_practice.png")
    background = pygame.transform.scale(background, (800, 500))
    logo = pygame.image.load("assets/visual/gameplay_assets/logo.png")
    logo = pygame.transform.scale(logo, (1000, 600))
    clock = pygame.time.Clock()
    fps = 60
    cont = 0
    sound_started = False
    in_position = False
    y = height

    cursor = Cursor(
        (cursor_x, cursor_y),
        screen
    )

    def event_manager(cursor, controller):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                loading.loading("practice", cursor, controller)
            if event.type == pygame.JOYBUTTONDOWN:
                loading.loading("practice", cursor, controller)

    while True:
        event_manager(cursor, controller)

        if not in_position:
            y -= 20

        if y == int(height / 2 - 100): in_position = True

        if in_position and not sound_started:
            sound.practice_mode()
            sound_started = True

        if in_position: cont += 1

        if cont >= 90: cont = 0


        screen.fill(const.BLACK)
        screen.blit(logo, (int(width * 0.1), int(height * 0.01)))
        if cont <= 60:
            screen.blit(background, [width / 2 - 400, y])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
