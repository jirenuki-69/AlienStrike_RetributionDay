import pygame, sys, const, title_screen
from clases.Texto import Texto
from clases.Button import Button
from clases.Music import Music
from clases.Sound import Sound

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def editar_nombre(nombre):
    my_file = open("nombre.txt", "w")
    my_file.writelines(str(nombre))

    my_file.close()

def conseguir_dificultad():
    with open ("difficulty.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def cambiar_dificultad(dificultad):
    my_file = open("difficulty.txt", "w")
    my_file.writelines(str(dificultad))

    my_file.close()

def option_screen():
    music = Music()
    music.options()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/option_screen.png")
    background = pygame.transform.scale(background, size)
    main_character_img = pygame.image.load("assets/visual/main_character_img/main_character_day.gif")
    main_character_img = pygame.transform.scale(main_character_img, (320, 200))

    diffuculty_shields = pygame.image.load("assets/visual/difficulty/example.png")
    diffuculty_no_shields = pygame.image.load("assets/visual/difficulty/example2.png")
    diffuculty_shields = pygame.transform.scale(diffuculty_shields, (500, 200))
    diffuculty_no_shields = pygame.transform.scale(diffuculty_no_shields, (500, 200))

    back_arrow = pygame.image.load("assets/visual/difficulty/back.png")
    next_arrow = pygame.image.load("assets/visual/difficulty/next.png")
    back_arrow_rect = back_arrow.get_rect()
    next_arrow_rect = next_arrow.get_rect()

    back_arrow_rect.x, back_arrow_rect.y = (int(width * 0.4), int(height * 0.257))
    next_arrow_rect.x, next_arrow_rect.y = (int(width * 0.61), int(height * 0.257))

    plus = pygame.image.load("assets/visual/options/plus.png")
    plus_rect = plus.get_rect()
    small_plus = pygame.transform.scale(plus, (15, 15))
    small_plus_rect = small_plus.get_rect()

    minus = pygame.image.load("assets/visual/options/minus.png")
    minus_rect = minus.get_rect()
    small_minus = pygame.transform.scale(minus, (15, 15))
    small_minus_rect = small_minus.get_rect()

    sound_plus = pygame.image.load("assets/visual/options/plus.png")
    sound_plus_rect = plus.get_rect()
    sound_small_plus = pygame.transform.scale(plus, (15, 15))
    sound_small_plus_rect = small_plus.get_rect()

    sound_minus = pygame.image.load("assets/visual/options/minus.png")
    sound_minus_rect = minus.get_rect()
    sound_small_minus = pygame.transform.scale(minus, (15, 15))
    sound_small_minus_rect = small_minus.get_rect()

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)
    font2 = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 30)
    font3 = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 20)
    description_font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 20)
    rectSize = (210, 30)

    display = [True, False, False, False]

    texto_descripcion = Texto(
        const.SETTINGS_DESCRIPTION,
        (width * 0.13, height * 0.79),
        description_font,
        screen,
        60,
        const.WHITE
    )

    volume_button = Button(
        screen,
        (int(width * 0.812),
        int(height * 0.258 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.TRANSPARENT,
        const.TRANSPARENT,
        "",
        font,
        const.WHITE
    )

    name_button = Button(
        screen,
        (int(width * 0.812),
        int(height * 0.308 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.TRANSPARENT,
        const.TRANSPARENT,
        "",
        font,
        const.WHITE
    )

    dificulty_button = Button(
        screen,
        (int(width * 0.812),
        int(height * 0.358 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.TRANSPARENT,
        const.TRANSPARENT,
        "",
        font,
        const.WHITE
    )

    exit_button = Button(
        screen,
        (int(width * 0.812),
        int(height * 0.408 - rectSize[1])),
        rectSize[0],
        rectSize[1],
        const.TRANSPARENT,
        const.TRANSPARENT,
        "",
        font,
        const.WHITE
    )

    texto_musica = Texto(
        "Música del juego",
        (width * 0.05, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_sonido = Texto(
        "SFX del juego",
        (width * 0.05, height * 0.35),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_new_volume = Texto(
        str(music.get_volume()),
        (width * 0.5, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_new_SFX = Texto(
        str(sound.get_SFX_volume()),
        (width * 0.5, height * 0.35),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_nombre = Texto(
        "Nombre del heroe",
        (width * 0.05, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_new_name = Texto(
        conseguir_nombre(),
        (width * 0.4, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_guion = Texto(
        "__________________",
        (width * 0.4, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_press_enter = Texto(
        "Presione ENTER para guardar los cambios. Con un nombre vacío no verá ningún cambio",
        (width * 0.05, height * 0.32),
        font3,
        screen,
        70,
        const.WHITE
    )

    texto_titulo = Texto(
        f"Ex piloto estrella de la armada 15 - {conseguir_nombre()}",
        (int(width * 0.22), int(height * 0.67)),
        font2,
        screen,
        45,
        const.WHITE
    )

    texto_dificultad = Texto(
        "Dificultad del juego",
        (width * 0.05, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_dificultad_placeholder = Texto(
        conseguir_dificultad(),
        (width * 0.48, height * 0.25),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_facil = Texto(
        const.EASY_DESCRIPTION,
        (width * 0.05, height * 0.32),
        font3,
        screen,
        70,
        const.WHITE
    )

    texto_dificil = Texto(
        const.HARD_DESCRIPTION,
        (width * 0.05, height * 0.32),
        font3,
        screen,
        70,
        const.WHITE
    )

    #Del volumen del juego
    minus_rect.x, minus_rect.y = (int(width * 0.4), int(height * 0.257))
    small_minus_rect.x, small_minus_rect.y = (int(width * 0.45), int(height * 0.266))
    plus_rect.x, plus_rect.y = (int(width * 0.61), int(height * 0.257))
    small_plus_rect.x, small_plus_rect.y = (int(width * 0.58), int(height * 0.266))

    #Del SFX del juego
    sound_minus_rect.x, sound_minus_rect.y = (int(width * 0.4), int(height * 0.357))
    sound_small_minus_rect.x, sound_small_minus_rect.y = (int(width * 0.45), int(height * 0.366))
    sound_plus_rect.x, sound_plus_rect.y = (int(width * 0.61), int(height * 0.357))
    sound_small_plus_rect.x, sound_small_plus_rect.y = (int(width * 0.58), int(height * 0.366))

    def display_volume():
        texto_musica.show_text()
        texto_new_volume.show_text()
        screen.blit(minus, [minus_rect.x, minus_rect.y])
        screen.blit(small_minus, [small_minus_rect.x, small_minus_rect.y])
        screen.blit(plus, [plus_rect.x, plus_rect.y])
        screen.blit(small_plus, [small_plus_rect.x, small_plus_rect.y])
        screen.blit(sound_minus, [sound_minus_rect.x, sound_minus_rect.y])
        screen.blit(sound_small_minus, [sound_small_minus_rect.x, sound_small_minus_rect.y])
        screen.blit(sound_plus, [sound_plus_rect.x, sound_plus_rect.y])
        screen.blit(sound_small_plus, [sound_small_plus_rect.x, sound_small_plus_rect.y])

        texto_sonido.show_text()
        texto_new_SFX.show_text()

    def display_name():
        texto_nombre.show_text()
        texto_new_name.show_text()
        texto_guion.show_text()
        texto_press_enter.show_text()

        screen.blit(main_character_img, (int(width * 0.5 - 270), int(height * 0.4)))
        texto_titulo.show_text()

    def display_dificulty():
        texto_dificultad.show_text()
        texto_dificultad_placeholder.show_text()

        if conseguir_dificultad() == "easy":
            screen.blit(diffuculty_shields, (int(width * 0.18), int(height * 0.45)))
            texto_facil.show_text()
        else:
            screen.blit(diffuculty_no_shields, (int(width * 0.18), int(height * 0.45)))
            texto_dificil.show_text()

        screen.blit(back_arrow, (back_arrow_rect.x, back_arrow_rect.y))
        screen.blit(next_arrow, ((next_arrow_rect.x, next_arrow_rect.y)))

    def event_manager():
        new_volume = music.get_volume()
        new_sound_volume = sound.get_SFX_volume()
        text_cont = len(texto_new_name.text)
        dificultad = conseguir_dificultad()

        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if volume_button.is_pressed(event, x, y):
                    display[0] = True
                    display[1] = False
                    display[2] = False

                if name_button.is_pressed(event, x, y):
                    display[1] = True
                    display[0] = False
                    display[2] = False

                if dificulty_button.is_pressed(event, x, y):
                    display[2] = True
                    display[0] = False
                    display[1] = False

                if exit_button.is_pressed(event, x, y):
                    title_screen.title_screen()

                if display[0]:
                    if small_minus_rect.collidepoint(x, y):
                        if new_volume - 0.01 >= 0:
                            new_volume -= 0.01
                            music.set_volume(round(new_volume, 2))
                            music.reset_volume()
                            texto_new_volume.text = str(music.get_volume())

                    if minus_rect.collidepoint(x, y):
                        if new_volume - 0.1 >= 0:
                            new_volume -= 0.1
                            music.set_volume(round(new_volume, 2))
                            music.reset_volume()
                            texto_new_volume.text = str(music.get_volume())

                    if plus_rect.collidepoint(x, y):
                        if new_volume + 0.1 <= 1:
                            new_volume += 0.1
                            music.set_volume(round(new_volume, 2))
                            music.reset_volume()
                            texto_new_volume.text = str(music.get_volume())

                    if small_plus_rect.collidepoint(x, y):
                        if new_volume + 0.01 <= 1:
                            new_volume += 0.01
                            music.set_volume(round(new_volume, 2))
                            music.reset_volume()
                            texto_new_volume.text = str(music.get_volume())

                    if sound_small_minus_rect.collidepoint(x, y):
                        if new_sound_volume - 0.01 >= 0:
                            new_sound_volume -= 0.01
                            sound.set_SFX_volume(round(new_sound_volume, 2))
                            texto_new_SFX.text = str(sound.get_SFX_volume())

                    if sound_minus_rect.collidepoint(x, y):
                        if new_sound_volume - 0.1 >= 0:
                            new_sound_volume -= 0.1
                            sound.set_SFX_volume(round(new_sound_volume, 2))
                            texto_new_SFX.text = str(sound.get_SFX_volume())

                    if sound_small_plus_rect.collidepoint(x, y):
                        if new_sound_volume + 0.01 <= 1:
                            new_sound_volume += 0.01
                            sound.set_SFX_volume(round(new_sound_volume, 2))
                            texto_new_SFX.text = str(sound.get_SFX_volume())

                    if sound_plus_rect.collidepoint(x, y):
                        if new_sound_volume + 0.1 <= 1:
                            new_sound_volume += 0.1
                            sound.set_SFX_volume(round(new_sound_volume, 2))
                            texto_new_SFX.text = str(sound.get_SFX_volume())

                if display[2]:
                    if back_arrow_rect.collidepoint(x, y):
                        if dificultad == "easy":
                            cambiar_dificultad("hard")
                        else:
                            cambiar_dificultad("easy")

                        texto_dificultad_placeholder.text = conseguir_dificultad()

                    if next_arrow_rect.collidepoint(x, y):
                        if dificultad == "easy":
                            cambiar_dificultad("hard")
                        else:
                            cambiar_dificultad("easy")

                        texto_dificultad_placeholder.text = conseguir_dificultad()

            if display[1]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if texto_new_name.text.strip() != "":
                            editar_nombre(texto_new_name.text)
                            texto_titulo.text = f"Ex piloto estrella de la armada 15 - {conseguir_nombre()}"

                    elif event.key == pygame.K_BACKSPACE:
                        texto_new_name.text = texto_new_name.text[:-1]
                        if text_cont > 0:
                            text_cont -= 1
                    else:
                        texto_new_name.text += event.unicode
                        text_cont += 1

    while True:
        event_manager()

        volume_button.init_button()
        name_button.init_button()
        dificulty_button.init_button()
        exit_button.init_button()

        screen.blit(background, [0, 0])

        texto_descripcion.show_text()

        if display[0]:
            display_volume()

        if display[1]:
            display_name()

        if display[2]:
            display_dificulty()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
