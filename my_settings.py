import pygame, sys

def settings():
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
    background = pygame.image.load("assets/menu.png")
    background = pygame.transform.scale(background, size)
    settings = pygame.image.load("assets/settings.png")

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

    #Colores
    GREEN = (0, 255, 0)
    RED = (217, 31, 11)
    DARK_GREEN = (51, 97, 28)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)

    #My values
    rectSize = (275, 100)

    def event_manager():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    while True:
        event_manager()

        screen.fill(BLACK)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
