import pygame, sys, xbox360_controller, endgame_history
from pygame import mixer
from clases.Escena import Escena
from clases.Music import Music
from clases.Cursor import Cursor
import const, title_screen

index = 0
mouse_on_movement = False
x, y = 0, 0

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def history():
    global index, mouse_on_movement

    music = Music()
    music.history_music()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    nombre = conseguir_nombre()
    ESCENAS_TEXTO = [
        "El año era 20xx. Después de una pandemia Biológica espontanea por parte de los aliados Comunistas de china, la humanidad se encontraba en un momento de caos total.",
        "Todos los países estaban en tensiones políticas Enormes.",
        "China no pudo guardar el secreto más tiempo, admitiendo que ellos crearon el virus, pero no para un propósito de conquista global…",
        "El verdadero motivo de la creación de un arma biológica de tal poder, era para erradicar a los invasores que se han mantenido en secreto por mucho tiempo…",
        "Pero ahora se han descontrolado, los “SNATCHERS” han tomado acción y se han infiltrado en los armamentos y defensas de todos los países…",
        "Los gobiernos de todo el mundo se ponen de acuerdo para llamar al piloto mas experimentado, el cual fue el único que logro defender al planeta del primer ataque de los SNATCHERS…",
        f"Ahí es donde entras tú, {nombre} el piloto estrella de la ex armada 15, al recibir la llamada del gobierno la rechazas inmediatamente, porque prefieres pasar el máximo tiempo posible con tu esposa a arriesgar tu vida otra vez….",
        f"Ahí es donde entras tú, {nombre} el piloto estrella de la ex armada 15, al recibir la llamada del gobierno la rechazas inmediatamente, porque prefieres pasar el máximo tiempo posible con tu esposa a arriesgar tu vida otra vez….",
        "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
        "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
        "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
        "Destrozado en llanto con el cuerpo de tu supuesta esposa en tus brazos, decides aceptar el trabajo.",
        "Destrozado en llanto con el cuerpo de tu supuesta esposa en tus brazos, decides aceptar el trabajo.",
        "Al llegar al hangar de despegue, te encuentras con tu vieja nave “IKARUGA” en la cual entras inmediatamente para no perder mas tiempo y terminar con esta invasión…",
        """Recuerda…. Eres la única esperanza para proteger a la tierra…. ¡¡¡Adelante soldado… EL MUNDO TE NECESITA!!!
        """,
        """Recuerda…. Eres la única esperanza para proteger a la tierra…. ¡¡¡Adelante soldado… EL MUNDO TE NECESITA!!!
        """
    ]
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 30)
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 10000)
    escena = Escena(
        const.ESCENAS[index],
        ESCENAS_TEXTO[index],
        const.WHITE,
        font,
        screen,
        size,
        (size[0], size[1])
    )

    cursor = Cursor(
        (int(width * 0.9), int(height * 0.3)),
        screen
    )

    mouse_on_movement = False
    x, y = cursor.x, cursor.y

    try:
        controller = xbox360_controller.Controller()
    except:
        controller = None

    #endgame_history.endgame_history(cursor.x, cursor.y, controller)

    def change_scene():
        escena.load_new_image(
            const.ESCENAS[index],
            ESCENAS_TEXTO[index],
        )

    def event_manager(cursor):
        global index, mouse_on_movement, x, y

        for event in pygame.event.get():
            if controller.get_left_stick() == (0 , 0):
                mouse_on_movement = True
                if pygame.mouse.get_pos() != (x, y):
                    cursor.mouse_movement(x, y)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if escena.next_pressed(x, y):
                    if index < len(const.ESCENAS) - 1:
                        index += 1
                        change_scene()
                        pygame.time.set_timer(timer_event, 0)
                        pygame.time.set_timer(timer_event, 10000)
                    else:
                        title_screen.title_screen(cursor.x, cursor.y, controller)
                if escena.skip_pressed(x, y):
                    title_screen.title_screen(cursor.x, cursor.y, controller)

            #Eventos con el control
            elif event.type == pygame.JOYBUTTONDOWN:
                if escena.next_pressed(cursor.x, cursor.y):
                    if index < len(const.ESCENAS) - 1:
                        index += 1
                        change_scene()
                        pygame.time.set_timer(timer_event, 0)
                        pygame.time.set_timer(timer_event, 10000)
                    else:
                        title_screen.title_screen(cursor.x, cursor.y, controller)
                if escena.skip_pressed(cursor.x, cursor.y):
                    title_screen.title_screen(cursor.x, cursor.y, controller)

            elif event.type == timer_event:
                if index < len(const.ESCENAS) - 1:
                    index += 1
                    change_scene()
                else:
                    title_screen.title_screen(cursor.x, cursor.y, controller)

        if mouse_on_movement:
            x, y = pygame.mouse.get_pos()

        if controller != None:
            x_controller, y_controller = controller.get_left_stick()
            cursor.movement(x_controller, y_controller)

            if (x_controller, y_controller) != (0, 0):
                mouse_on_movement = False

    while True:
        event_manager(cursor)

        screen.fill(const.BLACK)

        escena.show_scene()

        cursor.update()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
