#Numeros
MUSIC_VOLUME = 0.1

#Textos

ESCENAS = [
    "assets/visual/history_scenes/1.png",
    "assets/visual/history_scenes/2.png",
    "assets/visual/history_scenes/3.png",
    "assets/visual/history_scenes/3.png",
    "assets/visual/history_scenes/4.png",
    "assets/visual/history_scenes/5.png",
    "assets/visual/history_scenes/6.png",
    "assets/visual/history_scenes/7.png",
    "assets/visual/history_scenes/8.png",
    "assets/visual/history_scenes/9.png",
    "assets/visual/history_scenes/10.png",
    "assets/visual/history_scenes/11.png",
    "assets/visual/history_scenes/12.png",
    "assets/visual/history_scenes/13.png",
    "assets/visual/history_scenes/14.png",
    "assets/visual/history_scenes/15.png",
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
