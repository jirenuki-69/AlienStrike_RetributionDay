import pygame

#Logo
LOGO = pygame.image.load("assets/visual/logo.png")

#Numeros
MUSIC_VOLUME = 0.1

#Textos

SETTINGS_DESCRIPTION = "Este es el menu de opciones, aqui podras cambiar alguna que otras cosas para diferente experiencia de juego, mucha suerte configurando como quieres salvar la tierra jugador"

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

TUTORIAL = [
    "Presione la tecla Enter para continuar en el tutorial",
    "Manten presionado D para mover a la derecha",
    "Manten presionado A para mover a la izquierda",
    "Presiona Espacio o haz click izquierdo en el mouse para disparar",
    "Hay enemigos en cada nivel y debes eliminarlos",
    "O pueden atacarte y quitarte vida",
    "Vuelve a presionar Enter para regresar al menu principal"
]

#Colores
GREEN = (0, 255, 0)
RED = (217, 31, 11)
DARK_RED = (156, 24, 9)
DARK_GREEN = (51, 97, 28)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
TRANSPARENT = (0, 0, 0, 0)

#Fuente principal
FONT = "fonts/ufonts.com_windpower.ttf"
FONT_v2 = "fonts/Pixel LCD-7.ttf"

#Métodos
def cambiar_nombre(nombre):
    if nombre.strip() != "":
        NOMBRE_USUARIO = nombre
    else:
        print("Nombre inválido")
