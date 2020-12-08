import pygame, sys, LVL_1, arcade_splash_screen, practice_splash_screen, tutorial_splash_screen
from pygame import mixer
import const, tutorial
import title_screen
from clases.Texto import Texto
from clases.Music import Music
from clases.Cursor import Cursor

mouse_on_movement = False
mouse_x, mouse_y = 0, 0

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def main_menu(cursor_x, cursor_y, controller):
    global mouse_on_movement, mouse_x, mouse_y

    music = Music()
    music.chilling_grilling()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/select_mode_menu.png")
    background = pygame.transform.scale(background, size)
    nombre = conseguir_nombre()
    USUARIO_DESCRIPCION = f"Soy {str(nombre)}, ex piloto estrella de la armada15, he sobrevivido incontables guerras espaciales desde que tengo memoria y ahora solo estoy cansado de pelear, quiero morir en una vida aburrida y tranquila junto a mi esposa."


    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 25)
    description_font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 20)

    texto_arcade = Texto(
        "ARCADE",
        (width * 0.852, height * 0.05),
        font,
        screen,
        None
    )

    texto_practice = Texto(
        "PRACTICE",
        (width * 0.84, height * 0.13),
        font,
        screen,
        None
    )

    texto_tutorial = Texto(
        "TUTORIAL",
        (width * 0.84, height * 0.21),
        font,
        screen,
        None
    )

    texto_return = Texto(
        "RETURN",
        (width * 0.852, height * 0.29),
        font,
        screen,
        None
    )

    texto_descripcion = Texto(
        USUARIO_DESCRIPCION,
        (width * 0.09, height * 0.74),
        description_font,
        screen,
        55
    )

    cursor = Cursor(
        (cursor_x, cursor_y),
        screen
    )

    mouse_on_movement = False
    mouse_x, mouse_y = cursor_x, cursor_y

    def event_manager(cursor, controller):
        global mouse_on_movement, mouse_x, mouse_y

        for event in pygame.event.get():
            if controller.get_left_stick() == (0 , 0):
                mouse_on_movement = True
                if pygame.mouse.get_pos() != (mouse_x, mouse_y):
                    cursor.mouse_movement(mouse_x, mouse_y)

            if event.type == pygame.QUIT:
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if texto_arcade.text_rect.collidepoint(x, y):
                    arcade_splash_screen.arcade_splash_screen(cursor.x, cursor.y, controller)
                elif texto_practice.text_rect.collidepoint(x, y):
                    practice_splash_screen.practice_splash_screen(cursor.x, cursor.y, controller)
                elif texto_tutorial.text_rect.collidepoint(x, y):
                    tutorial_splash_screen.tutorial_splash_screen(cursor.x, cursor.y, controller)
                elif texto_return.text_rect.collidepoint(x, y):
                    title_screen.title_screen(cursor.x, cursor.y, controller)

            elif event.type == pygame.JOYBUTTONDOWN:
                if texto_arcade.text_rect.collidepoint(cursor.x, cursor.y):
                    arcade_splash_screen.arcade_splash_screen(cursor.x, cursor.y, controller)
                elif texto_practice.text_rect.collidepoint(cursor.x, cursor.y):
                    practice_splash_screen.practice_splash_screen(cursor.x, cursor.y, controller)
                elif texto_tutorial.text_rect.collidepoint(cursor.x, cursor.y):
                    tutorial_splash_screen.tutorial_splash_screen(cursor.x, cursor.y, controller)
                elif texto_return.text_rect.collidepoint(cursor.x, cursor.y):
                    title_screen.title_screen(cursor.x, cursor.y, controller)

        if mouse_on_movement:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if controller != None:
            x_controller, y_controller = controller.get_left_stick()
            cursor.movement(x_controller, y_controller)

            if (x_controller, y_controller) != (0, 0):
                mouse_on_movement = False

    while True:
        event_manager(cursor, controller)

        screen.blit(background, [0, 0])

        texto_arcade.show_text()
        texto_practice.show_text()
        texto_tutorial.show_text()
        texto_return.show_text()
        texto_descripcion.show_text()

        cursor.update()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
