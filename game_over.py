import pygame, const, sys, main_menu
from clases.Button import Button
from clases.Music import Music

def game_over():
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

    def event_manager():
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            #Compruebo la posicion del cursos para validar el hover del botón
            button.is_hovered(mouse_x, mouse_y)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if button.is_pressed(event, x, y):
                    main_menu.main_menu()

    while True:
        event_manager()

        screen.blit(background, [0, 0])
        button.init_button()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
