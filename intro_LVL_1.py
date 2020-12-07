import pygame, sys, const, LVL_1
from clases.Sound import Sound
from clases.Music import Music
from clases.Nave import Nave
from clases.Texto import Texto

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def intro_lvl_1(cursor, controller):
    music = Music()
    music.stop()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/BG_level1.png")
    background = pygame.transform.scale(background, size)
    dialogo = pygame.image.load("assets/visual/gameplay_assets/dialogo_negro.png")
    get_ready = pygame.image.load("assets/visual/gameplay_assets/get_ready.png")
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 15)
    clock = pygame.time.Clock()
    fps = 60
    cont = 0
    cont2 = 0
    dialogue_open = False
    is_get_ready_opened = False
    secs = 30
    nombre = conseguir_nombre()
    dialogo_intro = [
        "Esos malditos, pagaran por lo que le hicieron a nuestro planeta.",
        f"Vamos {nombre}, demuestra porque aun eres capaz de manejar estos monstruos por tu cuenta.",
        "Mucho exito amigo mio."
    ]

    index = 0

    texto = Texto(
        dialogo_intro[index],
        (int(width * 0.15), int(height * 0.9)),
        font,
        screen,
        75,
        const.WHITE,
    )

    nave = Nave(
        (int(width * 0.50), int(height * 1.2)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and dialogue_open:
                    if index + 1 == len(dialogo_intro):
                        if not is_get_ready_opened and dialogue_open:
                            sound.get_ready()
                            music.lvl_1()
                            is_get_ready_opened = True
                            dialogue_open = False
                    else:
                        sound.dialogue_change()
                        index += 1
                        texto.text = dialogo_intro[index]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if index + 1 == len(dialogo_intro):
                        if not is_get_ready_opened and dialogue_open:
                            sound.get_ready()
                            music.lvl_1()
                            is_get_ready_opened = True
                            dialogue_open = False
                    else:
                        sound.dialogue_change()
                        index += 1
                        texto.text = dialogo_intro[index]

            elif event.type == pygame.JOYBUTTONDOWN:
                if index + 1 == len(dialogo_intro):
                    if not is_get_ready_opened and dialogue_open:
                        sound.get_ready()
                        music.lvl_1()
                        is_get_ready_opened = True
                        dialogue_open = False
                else:
                    sound.dialogue_change()
                    index += 1
                    texto.text = dialogo_intro[index]

        screen.blit(background, [0 , 0])
        screen.blit(nave.image, nave.rect)

        if nave.rect.y != int(height * 0.9) - 60:
            nave.rect.y -= nave.movementSpeed

        if nave.rect.y == int(height * 0.9) - 60:
            if not dialogue_open:
                cont += 1
                if cont >= secs and not is_get_ready_opened:
                    dialogue_open = True

            if dialogue_open:
                screen.blit(dialogo, [0, height - 200])
                texto.show_text()

        if is_get_ready_opened:
            cont2 += 1
            if cont2 >= secs * 2:
                LVL_1.lvl_1(cursor, controller)
            screen.blit(get_ready, [width / 2 - 150, height / 2 - 75])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
