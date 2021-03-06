import pygame, const, sys, main_menu
from clases.Button import Button
from clases.Music import Music
from clases.Cursor import Cursor

mouse_on_movement = False
mouse_x, mouse_y = 0, 0

def game_over(cursor, controller):
    global mouse_on_movement, mouse_x, mouse_y

    #Pygame values
    music = Music()
    music.game_over()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)
    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/game_over_screen.png")
    background = pygame.transform.scale(background, size)
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 40)
    #My values
    rectSize = (275, 100)
    button = Button(
        screen,
        (int(width / 2 - rectSize[0] / 2),
        int(height * 0.70 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.RED,
        const.DARK_RED,
        "Regresar al menú",
        font,
        const.WHITE
    )

    mouse_on_movement = False
    mouse_x, mouse_y = cursor.x, cursor.y

    def event_manager(cursor, controller):
        global mouse_on_movement, mouse_x, mouse_y

        for event in pygame.event.get():
            if controller != None:
                if controller.get_left_stick() == (0 , 0):
                    mouse_on_movement = True
                    if pygame.mouse.get_pos() != (mouse_x, mouse_y):
                        cursor.mouse_movement(mouse_x, mouse_y)
            else:
                mouse_on_movement = True
                if pygame.mouse.get_pos() != (mouse_x, mouse_y):
                    cursor.mouse_movement(mouse_x, mouse_y)

            if event.type == pygame.QUIT:
                sys.exit()

            #Compruebo la posicion del cursos para validar el hover del botón
            button.is_hovered(cursor.x, cursor.y)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if button.is_pressed(event, x, y):
                    main_menu.main_menu(cursor.x, cursor.y, controller)

            if event.type == pygame.JOYBUTTONDOWN:
                if button.is_pressed(event, cursor.x, cursor.y):
                    main_menu.main_menu(cursor.x, cursor.y, controller)

        if mouse_on_movement:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if controller != None:
            x_controller, y_controller = controller.get_left_stick()
            cursor.movement(x_controller, y_controller)

            if (x_controller, y_controller) != (0, 0):
                mouse_on_movement = False

    while True:
        event_manager(cursor, controller)

        screen.blit(background, [0, 0])
        button.init_button()

        cursor.update()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
