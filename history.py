import pygame, sys
from pygame import mixer
from clases.Escena import Escena
import const, title_screen

index = 0

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def history():
    global index

    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    pygame.mixer.music.load("assets/music/Alien Soldier - Sidelimits.mp3")
    pygame.mixer.music.set_volume(const.MUSIC_VOLUME)
    pygame.mixer.music.play(-1)
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

    def change_scene():
        escena.load_new_image(
            const.ESCENAS[index],
            ESCENAS_TEXTO[index],
        )

    def event_manager():
        global index

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if escena.next_pressed(x, y):
                    if index < len(const.ESCENAS) - 1:
                        index += 1
                        change_scene()
                    else:
                        title_screen.title_screen()
                if escena.skip_pressed(x, y):
                    title_screen.title_screen()

            elif event.type == timer_event:
                if index < len(const.ESCENAS) - 1:
                    index += 1
                    change_scene()
                else:
                    title_screen.title_screen()
    while True:
        event_manager()

        screen.fill(const.BLACK)

        escena.show_scene()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
