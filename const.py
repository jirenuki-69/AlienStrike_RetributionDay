#Textos
NOMBRE_USUARIO = "Miguel Fuentes"

USUARIO_DESCRIPCION = f"Soy {NOMBRE_USUARIO}, ex piloto estrella de la armada15, he sobrevivido incontables guerras espaciales desde que tengo memoria y ahora solo estoy cansado de pelear, quiero morir en una vida aburrida y tranquila junto a mi esposa."

ESCENAS = [
    "assets/visual/history_scenes/1.jpg",
    "assets/visual/history_scenes/2.png",
    "assets/visual/history_scenes/3.png",
    "assets/visual/history_scenes/3.png",
    "assets/visual/history_scenes/4.jpg",
    "assets/visual/history_scenes/5.png",
    "assets/visual/history_scenes/6.png",
    "assets/visual/history_scenes/7.png",
    "assets/visual/history_scenes/8.jpg",
    "assets/visual/history_scenes/9.png",
    "assets/visual/history_scenes/10.png",
    "assets/visual/history_scenes/11.png",
    "assets/visual/history_scenes/12.png",
    "assets/visual/history_scenes/13.jpg",
    "assets/visual/history_scenes/14.jpg",
    "assets/visual/history_scenes/15.jpg",
]

ESCENAS_TEXTO = [
    "El año era 20xx. Después de una pandemia Biológica espontanea por parte de los aliados Comunistas de china, la humanidad se encontraba en un momento de caos total.",
    "Todos los países estaban en tensiones políticas Enormes.",
    "China no pudo guardar el secreto más tiempo, admitiendo que ellos crearon el virus, pero no para un propósito de conquista global…",
    "El verdadero motivo de la creación de un arma biológica de tal poder, era para erradicar a los invasores que se han mantenido en secreto por mucho tiempo…",
    "Pero ahora se han descontrolado, los “SNATCHERS” han tomado acción y se han infiltrado en los armamentos y defensas de todos los países…",
    "Los gobiernos de todo el mundo se ponen de acuerdo para llamar al piloto mas experimentado, el cual fue el único que logro defender al planeta del primer ataque de los SNATCHERS…",
    f"Ahí es donde entras tú, {NOMBRE_USUARIO} el piloto estrella de la ex armada 15, al recibir la llamada del gobierno la rechazas inmediatamente, porque prefieres pasar el máximo tiempo posible con tu esposa a arriesgar tu vida otra vez….",
    f"Ahí es donde entras tú, {NOMBRE_USUARIO} el piloto estrella de la ex armada 15, al recibir la llamada del gobierno la rechazas inmediatamente, porque prefieres pasar el máximo tiempo posible con tu esposa a arriesgar tu vida otra vez….",
    "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
    "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
    "PERO justo después de recibir la llamada tu esposa empieza a actuar de manera extraña… ella es uno de ellos, tu esposa había sido sustituida por los SNATCHERS, ella te empieza a atacar y tú en defensa propia, acabas con ella…",
    "Destrozado en llanto con el cuerpo de tu supuesta esposa en tus brazos, decides aceptar el trabajo.",
    "Destrozado en llanto con el cuerpo de tu supuesta esposa en tus brazos, decides aceptar el trabajo.",
    "Al llegar al hangar de despegue, te encuentras con tu vieja nave “IKARUGA” en la cual entras inmediatamente para no perder mas tiempo y terminar con esta invasión…",
    """Recuerda…. Eres la única esperanza para proteger a la tierra….

       ¡¡¡Adelante soldado… EL MUNDO TE NECESITA!!!
    """,
    """Recuerda…. Eres la única esperanza para proteger a la tierra….

       ¡¡¡Adelante soldado… EL MUNDO TE NECESITA!!!
    """
]

#Colores
GREEN = (0, 255, 0)
RED = (217, 31, 11)
DARK_RED = (156, 24, 9)
DARK_GREEN = (51, 97, 28)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

#Fuente principal
#FONT = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

#Métodos
def cambiar_nombre(nombre):
    if nombre.strip() != "":
        NOMBRE_USUARIO = nombre
    else:
        print("Nombre inválido")
