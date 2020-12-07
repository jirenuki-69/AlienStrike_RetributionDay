import pygame, sys, const, endgame_history
from clases.Nave import Nave
from clases.Music import Music
from clases.Sound import Sound
from clases.Texto import Texto

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def boss_end_scene(nave_pos, cursor, controller):
    nave_pos = (nave_pos[0] + 90, nave_pos[1] + 60)
    music = Music()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    nombre = conseguir_nombre()
    index = 0
    DIALOGO_FINAL = [
        "Increible... nunca me pude imaginar que existia semejante monstruo.",
        f"{nombre}, llenas de orgullo al mundo, definitivamente eres el heroe de esta historia.",
        "No esperemos mucho mas, es hora de regresar a casa y tomarnos un buen descanso. bien hecho campeon"
    ]

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/boss_background.png")
    background = pygame.transform.scale(background, size)
    dialogo = pygame.image.load("assets/visual/gameplay_assets/dialogo_negro.png")
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 15)

    texto = Texto(
        DIALOGO_FINAL[index],
        (int(width * 0.15), int(height * 0.9)),
        font,
        screen,
        70,
        const.WHITE,
    )

    nave = Nave(
        nave_pos,
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    dialogue_open = False
    rotated = False
    finalizado = False
    grados = 0
    loop = 1
    cont = 0

    def subir_nave(nave):
        nave.rect.y -= nave.movementSpeed

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and dialogue_open:
                    if index + 1 == len(DIALOGO_FINAL):
                        print("Final")
                        rotated = True

                    else:
                        sound.dialogue_change()
                        index += 1
                        texto.text = DIALOGO_FINAL[index]
                        print("Si pasa")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and dialogue_open:
                    if index + 1 == len(DIALOGO_FINAL):
                        print("Final")
                        rotated = True

                    else:
                        sound.dialogue_change()
                        index += 1
                        texto.text = DIALOGO_FINAL[index]
                        print("Si pasa")

            if event.type == pygame.JOYBUTTONDOWN:
                if index + 1 == len(DIALOGO_FINAL):
                    print("Final")
                    rotated = True

                else:
                    sound.dialogue_change()
                    index += 1
                    texto.text = DIALOGO_FINAL[index]
                    print("Si pasa")

        if rotated and not finalizado:
            grados += 3

        if grados == 180:
            finalizado = True
            nave.rect.y += (nave.movementSpeed * loop) / 2
            loop += 0.5
            nave.image = img_copy

        screen.blit(background, [0, 0])

        if nave.rect.y > height:
            cont += 1
            if cont >= 60:
                endgame_history.endgame_history(cursor.x, cursor.y, controller)

        if not rotated:
            screen.blit(nave.image, nave.rect)

        elif rotated and not finalizado:
            img_copy = pygame.transform.rotate(nave.image, grados)
            screen.blit(img_copy, (nave.rect.x - int(img_copy.get_width() / 2) + 90, nave.rect.y - int(img_copy.get_height() / 2) + 60))

        elif rotated and finalizado:
            screen.blit(nave.image, nave.rect)

        if nave.rect.y > height / 2 - nave.rect.height / 2:
            subir_nave(nave)

        if nave.rect.y == height / 2 - nave.rect.height / 2:
            dialogue_open = True
            screen.blit(dialogo, [0, height - 200])
            texto.show_text()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
