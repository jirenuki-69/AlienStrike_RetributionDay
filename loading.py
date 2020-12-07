import pygame, sys, const
import intro_LVL_1, intro_LVL_2, intro_LVL_3, intro_boss
from clases.Shield import Escudo
from clases.Texto import Texto
from clases.Sound import Sound
from clases.Cursor import Cursor

def loading(next_level, cursor, controller, difficulty = "easy", shields = [], vidas = 5):
    pygame.init()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/loading.jpg")
    background = pygame.transform.scale(background, size)
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 18)
    clock = pygame.time.Clock()
    fps = 60
    cont = 0

    texto = Texto(
        "Cargando",
        (535, 650),
        font,
        screen,
        75,
        const.WHITE,
    )

    def loading_bar(screen, cont):
        largo = 300
        ancho = 30
        calculo_barra = int((cont/90 * largo))
        borde = pygame.Rect(450, 700, largo, ancho)
        rectangulo = pygame.Rect(450, 700, calculo_barra, ancho)
        pygame.draw.rect(screen, const.WHITE, borde, 3)
        pygame.draw.rect(screen, const.WHITE, rectangulo)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background, [0 , 0])
        texto.show_text()

        cont += 1

        loading_bar(screen, cont)

        if cont == 30:
            texto.text = "Cargando."

        if cont == 55:
            texto.text = "Cargando.."

        if cont == 80:
            texto.text = "Cargando..."

        if cont >= 90:
            if next_level == "1":
                intro_LVL_1.intro_lvl_1(cursor, controller)
            elif next_level == "2":
                intro_LVL_2.intro_lvl_2(cursor, controller, difficulty, shields, vidas)
            elif next_level == "3":
                intro_LVL_3.intro_lvl_3(cursor, controller, difficulty, shields, vidas)
            elif next_level == "boss":
                intro_boss.intro_boss(cursor, controller, difficulty, shields, vidas)


        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
