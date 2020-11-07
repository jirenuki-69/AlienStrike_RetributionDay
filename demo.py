import pygame
import sys
from pygame import mixer
from clases.Nave import Nave

def demo():
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    pygame.mixer.music.load("assets/music/Alien Soldier - Runner AD2025.mp3")
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
    font = pygame.font.Font("Fonts\\Thewitcher-jnOj.ttf", 30)

    nave = Nave(
        (int(width * 0.10), int(height * 0.85)),
        5,
        size,
        "assets/gameplay_images/main_ship.png"
    )

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

        response = nave.event_manager()

    while True:
        event_manager()

        screen.fill(BLACK)
        screen.blit(nave.image, nave.rect)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
