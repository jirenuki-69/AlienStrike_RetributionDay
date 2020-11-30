import pygame
import sys
from pygame import mixer
from clases.Nave import Nave
import const

step = 1
response = 0
def tutorial():
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    #pygame.mixer.music.load("assets/music/Alien Soldier - Runner AD2025.mp3")
    #pygame.mixer.music.set_volume(.1)
    #pygame.mixer.music.play(-1)
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/gencity.png")
    ackground = pygame.transform.scale(background, size)
    # settings = pygame.image.load("assets/settings.png")

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)
    ban = False
    cont = 0
    mag = False

    nave = Nave(
        (int(width * 0.10), int(height * 0.85)),
        5,
        size,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    #My values
    rectSize = (275, 100)

    def text(data, x, y, color, size, screen):
        font = pygame.font.Font(const.FONT, size)
        texto_marcador = font.render(data, True, color)
        texto_marcador_rect = texto_marcador.get_rect()
        screen_rec = screen.get_rect()

        texto_marcador_rect.center = screen_rec.center

        if x == -1:
            x = texto_marcador_rect[0]
        if y == -1:
            y = texto_marcador_rect[1]

        screen.blit(texto_marcador, [x, y, texto_marcador_rect[2],  texto_marcador_rect[3]])

    def fire(character):
        screen.blit(character.misilimage, character.misilrect)
        character.misilrect.y -= 10
        #for x in objarrg:
        #    if character.misilrect.colliderect(x.rect):
        #        objarrg.remove(x)
        #        character.misilrect.x = pantalla_x + 10
        #        puntos += 5

    def event_manager():
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    step += 1



        response = nave.event_manager()

    while True:
        event_manager()
        screen.blit(background, [0, 0])
        if ban:
            if cont < fps * 2:
                cont += 1
            fire(nave)
        screen.blit(nave.image, nave.rect)
        text(const.TUTORIAL[0], 0, 750, const.WHITE, 50, screen)
        if response != 0:
            nave.misilrect.center = response.center
            ban = True
        text(const.TUTORIAL[step], 0, 0, const.WHITE, 50, screen)
        print(cont)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
