import pygame

#Logo
LOGO = pygame.image.load("assets/visual/logo.png")

#Numeros
MUSIC_VOLUME = 0.1

#Textos

SETTINGS_DESCRIPTION = "Este es el menu de opciones, aqui podras cambiar alguna que otras cosas para diferente experiencia de juego, mucha suerte configurando como quieres salvar la tierra jugador"

EASY_DESCRIPTION = "Al parecer eres de los que no toman riesgos en la vida, la dificultad fácil hará que tus escudos se regeneren por cada nivel que pases"
HARD_DESCRIPTION = "Prueba tu valentía con el modo difícil del juego, esta dificultad hará que tus escudos no se regeneren por nivel y sigan de la misma forma que el nivel anterior"

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

CITY_PULSING_LIGHTS = [
    "assets/visual/city_frames/frame_00_delay-0.04s.gif",
    "assets/visual/city_frames/frame_01_delay-0.04s.gif",
    "assets/visual/city_frames/frame_02_delay-0.04s.gif",
    "assets/visual/city_frames/frame_03_delay-0.04s.gif",
    "assets/visual/city_frames/frame_04_delay-0.04s.gif",
    "assets/visual/city_frames/frame_05_delay-0.04s.gif",
    "assets/visual/city_frames/frame_06_delay-0.04s.gif",
    "assets/visual/city_frames/frame_07_delay-0.04s.gif",
    "assets/visual/city_frames/frame_08_delay-0.04s.gif",
    "assets/visual/city_frames/frame_09_delay-0.04s.gif",
    "assets/visual/city_frames/frame_10_delay-0.04s.gif",
    "assets/visual/city_frames/frame_11_delay-0.04s.gif",
    "assets/visual/city_frames/frame_12_delay-0.04s.gif",
    "assets/visual/city_frames/frame_13_delay-0.04s.gif",
    "assets/visual/city_frames/frame_14_delay-0.04s.gif",
    "assets/visual/city_frames/frame_15_delay-0.04s.gif",
    "assets/visual/city_frames/frame_16_delay-0.04s.gif",
    "assets/visual/city_frames/frame_17_delay-0.04s.gif",
    "assets/visual/city_frames/frame_18_delay-0.04s.gif",
    "assets/visual/city_frames/frame_19_delay-0.04s.gif",
    "assets/visual/city_frames/frame_20_delay-0.04s.gif",
    "assets/visual/city_frames/frame_21_delay-0.04s.gif",
    "assets/visual/city_frames/frame_22_delay-0.04s.gif",
    "assets/visual/city_frames/frame_23_delay-0.04s.gif",
    "assets/visual/city_frames/frame_24_delay-0.04s.gif",
    "assets/visual/city_frames/frame_25_delay-0.04s.gif",
    "assets/visual/city_frames/frame_26_delay-0.04s.gif",
    "assets/visual/city_frames/frame_27_delay-0.04s.gif",
    "assets/visual/city_frames/frame_28_delay-0.04s.gif",
    "assets/visual/city_frames/frame_29_delay-0.04s.gif",
    "assets/visual/city_frames/frame_30_delay-0.04s.gif",
    "assets/visual/city_frames/frame_31_delay-0.04s.gif",
    "assets/visual/city_frames/frame_32_delay-0.04s.gif",
    "assets/visual/city_frames/frame_33_delay-0.04s.gif",
    "assets/visual/city_frames/frame_34_delay-0.04s.gif",
    "assets/visual/city_frames/frame_35_delay-0.04s.gif",
    "assets/visual/city_frames/frame_36_delay-0.04s.gif",
    "assets/visual/city_frames/frame_37_delay-0.04s.gif",
    "assets/visual/city_frames/frame_38_delay-0.04s.gif",
    "assets/visual/city_frames/frame_39_delay-0.04s.gif",
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
