import pygame
import sys
from pygame import mixer
from clases.Button import Button
import main_menu, const, my_settings, demo

def title_screen():
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    pygame.mixer.music.load("assets/music/Alien Soldier - Title Theme(sugiero como musica del titulo).mp3")
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1)
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/menu.png")
    background = pygame.transform.scale(background, size)
    settings = pygame.image.load("assets/visual/settings.png")

    settings = pygame.transform.scale(settings, (80, 80))
    settingsRect = settings.get_rect()
    settingsRect[0], settingsRect[1] = 20, int(height * 0.85)

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

    #My values
    rectSize = (275, 100)
    menu_button = Button(
        screen,
        (int(width / 2 - rectSize[0] / 2),
        int(height * 0.75 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.RED,
        const.DARK_RED,
        "Jugar",
        font,
        const.WHITE
    )

    def event_manager():
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            #Compruebo la posicion del cursos para validar el hover del botón
            menu_button.is_hovered(mouse_x, mouse_y)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if menu_button.is_pressed(event, x, y):
                    main_menu.main_menu()
                if settingsRect.collidepoint(x, y):
                    my_settings.settings()

    while True:
        event_manager()

        screen.blit(background, [0, 0])
        screen.blit(settings, [settingsRect[0], settingsRect[1]])
        menu_button.init_button()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
