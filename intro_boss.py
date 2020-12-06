import pygame, sys, const, boss_fight
from clases.Sound import Sound
from clases.Music import Music
from clases.Nave import Nave
from clases.Boss import Boss
from clases.Texto import Texto

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def intro_boss():
    music = Music()
    music.game_over()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/boss_background.png")
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
        "Pe pe pe pero ¡¿¡¿que es eso?!?!",
        "Nunca en nuestra vida habiamos visto un alienigena asi de gigante, hay que tener mucho cuidado con este tipo.",
        "Parece ser que su nucleo se encuentra en el centro de su cuerpo, procura que tus disparos vayan para alla y puedas herirlo.",
        f"escuchame {nombre}, destruye las partes que se encuentran al lado del nucleo, parecen ser que mantienen seguro su punto debil mientras esten activas",
        f"Ten mucho cuidado {nombre}, este monstruo no parece ser ninguna broma como en tus aventuras anteriores, un golpe puede resultarte letal.",
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

    #int(height * 0.9)
    nave = Nave(
        (int(width * 0.50), int(height * 1.2)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    boss = Boss(
        (int(width * 0.50), int(height * 0.35)),
        size,
        screen
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
                            is_get_ready_opened = True
                            dialogue_open = False
                    else:
                        sound.dialogue_change()
                        index += 1
                        texto.text = dialogo_intro[index]

        screen.blit(background, [0 , 0])
        boss.update()
        screen.blit(boss.image,boss.rect)
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
                boss_fight.boss_fight()
            screen.blit(get_ready, [width / 2 - 150, height / 2 - 75])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
