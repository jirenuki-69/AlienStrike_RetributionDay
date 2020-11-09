import pygame, sys
from pygame import mixer
from clases.Escena import Escena
import const, title_screen

index = 0

def history():
    global index

    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    pygame.mixer.music.load("assets/music/Alien Soldier - Sidelimits.mp3")
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1)
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    # background = pygame.image.load("assets/menu.png")
    # background = pygame.transform.scale(background, size)
    # settings = pygame.image.load("assets/settings.png")
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 30)
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 10000)
    escena = Escena(
        const.ESCENAS[index],
        const.ESCENAS_TEXTO[index],
        const.WHITE,
        font,
        screen,
        size,
        (int(size[0] * 0.8), int(size[1] * 0.7))
    )

    def change_scene():
        escena.load_new_image(
            const.ESCENAS[index],
            const.ESCENAS_TEXTO[index],
        )

    def event_manager():
        global index

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == timer_event:
                if index < len(const.ESCENAS) - 1:
                    index += 1
                    change_scene()
                else:
                    title_screen.title_screen()
    while True:
        event_manager()

        screen.fill(const.BLACK)

        escena.show_scene()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
