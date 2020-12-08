import pygame
import sys
from pygame import mixer
from clases.Button import Button
from clases.Music import Music
from clases.Cursor import Cursor
import main_menu, const, option_screen, demo, xbox360_controller

def title_screen(cursor_x, cursor_y, controller):
    music = Music()
    music.title_screen()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    logo = pygame.image.load("assets/visual/gameplay_assets/logo.png")
    logo = pygame.transform.scale(logo, (1000, 600))
    settings = pygame.image.load("assets/visual/settings.png")

    settings = pygame.transform.scale(settings, (80, 80))
    settingsRect = settings.get_rect()
    settingsRect[0], settingsRect[1] = 20, int(height * 0.85)

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

    cont = 0
    index = 0
    secs = 10
    first_loop = True
    second_loop = False

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

    cursor = Cursor(
        (cursor_x, cursor_y),
        screen
    )

    def event_manager(cursor, controller):

        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            #Compruebo la posicion del cursos para validar el hover del botón
            menu_button.is_hovered(mouse_x, mouse_y)
            if controller != None:
                menu_button.is_hovered(cursor.x, cursor.y)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if menu_button.is_pressed(event, x, y):
                    main_menu.main_menu(cursor.x, cursor.y, controller)
                if settingsRect.collidepoint(x, y):
                    option_screen.option_screen(controller, cursor.x, cursor.y)

            elif event.type == pygame.JOYBUTTONDOWN:
                if menu_button.is_pressed(event, cursor.x, cursor.y):
                    main_menu.main_menu(cursor.x, cursor.y, controller)
                if settingsRect.collidepoint(cursor.x, cursor.y):
                    option_screen.option_screen(controller, cursor.x, cursor.y)

    while True:
        event_manager(cursor, controller)
        background = pygame.image.load(const.CITY_PULSING_LIGHTS[index])
        background = pygame.transform.scale(background, size)

        screen.blit(background, [0, 0])
        screen.blit(logo, (int(width * 0.1), int(height * 0.05)))
        screen.blit(settings, [settingsRect[0], settingsRect[1]])
        menu_button.init_button()

        cursor.update()

        if controller != None:
            x_controller, y_controller = controller.get_left_stick()
            cursor.movement(x_controller, y_controller)

        cont += 1

        if first_loop and cont % 3 * secs == 0:
            index += 1

        if second_loop and cont % 3 * secs == 0:
            index -= 1

        if cont >= 12 * secs:
            first_loop = not first_loop
            second_loop = not second_loop
            if first_loop:
                index += 1
            if second_loop:
                index -= 1
            cont = 0

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
