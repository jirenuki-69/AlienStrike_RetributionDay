import pygame
import const, title_screen, sys, os

my_file = open("nombre.txt", "w")
my_file.writelines("James")

my_file.close()

def cambiar_nombre(nombre):
    my_file = open("nombre.txt", "w")
    my_file.writelines(str(nombre))

    my_file.close()

def username():
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)
    text = ""
    text_cont = 0
    x = 0
    y = 0

    #Global values
    background = pygame.image.load("assets/visual/history_scenes/nombre.png")
    background = pygame.transform.scale(background, size)

    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font("fonts/ufonts.com_windpower.ttf", 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text.strip() != "":
                        cambiar_nombre(text)
                        return
                    else:
                        return
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    if text_cont > 0:
                        text_cont -= 1
                else:
                    text += event.unicode
                    text_cont += 1



        screen.blit(background, [0, 0])
        txt_escribir = font.render("Escriba su nombre, jugador", True, const.WHITE)

        txt_surface = font.render(text, True, const.WHITE)
        txt_surface_rect = txt_surface.get_rect()
        txt_surface_rect.x, txt_surface_rect.y = (int( (width * 0.3) ), int( height * 0.85 ))

        screen.blit(txt_escribir, (350, 625))
        screen.blit(txt_surface, (txt_surface_rect.x, txt_surface_rect.y))

        pygame.display.flip()
        clock.tick(30)


    pygame.quit()
