import pygame, sys, const, credits, xbox360_controller
from clases.Escena import Escena
from clases.Music import Music
from clases.Cursor import Cursor

index = 0
mouse_on_movement = False
mouse_x, mouse_y = 0, 0

def endgame_history(cursor_x, cursor_y, controller):
    global mouse_on_movement, mouse_x, mouse_y

    music = Music()
    music.endgame()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 25)
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 10000)
    escena = Escena(
        const.ESCENAS_ENDGAME[index],
        const.ENDGAME_STORY[index],
        const.WHITE,
        font,
        screen,
        size,
        (size[0], size[1]),
        100,
        35
    )

    cursor = Cursor(
        (cursor_x, cursor_y),
        screen
    )

    mouse_on_movement = False
    mouse_x, mouse_y = cursor_x, cursor_y

    def change_scene():
        escena.load_new_image(
            const.ESCENAS_ENDGAME[index],
            const.ENDGAME_STORY[index],
        )

    def event_manager(cursor, controller):
        global index, mouse_on_movement, mouse_x, mouse_y

        for event in pygame.event.get():
            if controller.get_left_stick() == (0 , 0):
                mouse_on_movement = True
                if pygame.mouse.get_pos() != (mouse_x, mouse_y):
                    cursor.mouse_movement(mouse_x, mouse_y)

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and escena.is_last_scene:
                    credits.credits(cursor, controller)

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.joy == controller.get_id():
                    if event.button == xbox360_controller.A and escena.is_last_scene:
                        credits.credits(cursor, controller)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if escena.next_pressed(x, y):
                    if index < len(const.ESCENAS_ENDGAME) - 1:
                        index += 1
                        pygame.time.set_timer(timer_event, 0)
                        pygame.time.set_timer(timer_event, 10000)
                        if index == len(const.ESCENAS_ENDGAME) - 1:
                            escena.last_scene()
                        change_scene()
                    elif index >= len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                        credits.credits(cursor, controller)
                if escena.skip_pressed(x, y):
                    credits.credits(cursor, controller)

            elif event.type == pygame.JOYBUTTONDOWN:
                if escena.next_pressed(cursor.x, cursor.y):
                    if index < len(const.ESCENAS_ENDGAME) - 1:
                        index += 1
                        pygame.time.set_timer(timer_event, 0)
                        pygame.time.set_timer(timer_event, 10000)
                        if index == len(const.ESCENAS_ENDGAME) - 1:
                            escena.last_scene()
                        change_scene()
                    elif index >= len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                        credits.credits(cursor, controller)
                if escena.skip_pressed(cursor.x, cursor.y):
                    credits.credits(cursor, controller)

            elif event.type == timer_event:
                if index < len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                    index += 1
                    if index == len(const.ESCENAS_ENDGAME) - 1:
                        escena.last_scene()
                    change_scene()
                elif index >= len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                    credits.credits(cursor, controller)

        if mouse_on_movement:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if controller != None:
            x_controller, y_controller = controller.get_left_stick()
            cursor.movement(x_controller, y_controller)

            if (x_controller, y_controller) != (0, 0):
                mouse_on_movement = False

    while True:
        event_manager(cursor, controller)

        escena.show_scene()

        cursor.update()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
