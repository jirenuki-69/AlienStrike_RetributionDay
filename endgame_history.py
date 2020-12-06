import pygame, sys, const, credits
from clases.Escena import Escena
from clases.Music import Music

index = 0

def endgame_history():
    global index

    music = Music()
    music.endgame()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 30
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

    def change_scene():
        escena.load_new_image(
            const.ESCENAS_ENDGAME[index],
            const.ENDGAME_STORY[index],
        )

    def event_manager():
        global index

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and escena.is_last_scene:
                    credits.credits()

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
                        credits.credits()
                if escena.skip_pressed(x, y):
                    credits.credits()

            elif event.type == timer_event:
                if index < len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                    index += 1
                    if index == len(const.ESCENAS_ENDGAME) - 1:
                        escena.last_scene()
                    change_scene()
                elif index >= len(const.ESCENAS_ENDGAME) - 1 and not escena.is_last_scene:
                    credits.credits()

    while True:
        event_manager()

        escena.show_scene()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
