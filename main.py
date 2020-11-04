import pygame
import sys
from pygame import mixer
from clases.Button import Button

pygame.init()
pygame.display.set_caption("Alien Strike: Retribution Day")
width = 600
height = 900
size = (width, height)
screen = pygame.display.set_mode(size)

#Global values
background = pygame.image.load("img/Fondo.png")
background = pygame.transform.scale(background, size)
clock = pygame.time.Clock()
fps = 30
font = pygame.font.Font("Fonts\\Thewitcher-jnOj.ttf", 30)

#Colores
GREEN = (0, 255, 0)
DARK_GREEN = (51, 97, 28)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

#My values
rectSize = (275, 100)
menu_button = Button(
    screen,
    (int(width / 2 - rectSize[0] / 2),
    int(height / 2 - rectSize[1])),
    rectSize[0],
    rectSize[1],
    GREEN,
    DARK_GREEN,
    "Iniciar",
    font,
    BLACK
)

secondary_button = Button(
    screen,
    (int(width / 2 - rectSize[0] / 2),
    int(height / 2 - rectSize[1] + menu_button.height + 30)),
    rectSize[0],
    rectSize[1],
    WHITE,
    GRAY,
    "Boton secundario",
    font,
    BLACK
)

def event_manager():
    global menu_button, secondary_button

    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            sys.exit()

        #Compruebo la posicion del cursos para validar el hover del botón
        menu_button.is_hovered(mouse_x, mouse_y)
        secondary_button.is_hovered(mouse_x, mouse_y)

        if pygame.mouse.get_pressed()[0]:
            x, y = event.pos
            if menu_button.is_pressed(event, x, y):
                print("Botón del menú presionado")
            elif secondary_button.is_pressed(event, x, y):
                print("Botón secundario presionado")

while True:
    event_manager()

    screen.blit(background, [0, 0])
    menu_button.init_button()
    secondary_button.init_button()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
