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
    x = 0
    y = 0

    #Global values
    background = pygame.image.load("assets/visual/menu.png")
    background = pygame.transform.scale(background, size)
    settings = pygame.image.load("assets/visual/settings.png")

    settings = pygame.transform.scale(settings, (80, 80))
    settingsRect = settings.get_rect()
    settingsRect[0], settingsRect[1] = 20, int(height * 0.85)

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
                else:
                    text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()



        screen.fill((const.BLACK))
        txt_surface = font.render(text, True, const.RED)


        screen.blit(txt_surface, (x, y))

        pygame.display.flip()
        clock.tick(30)


    pygame.quit()
