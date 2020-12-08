import pygame, loading, xbox360_controller
import sys
from pygame import mixer
from clases.Nave import Nave
import const
import main_menu
import random
from clases.Shield import Escudo
from clases.MiniEnemy import MiniEnemy
from clases.Music import Music
from clases.Sound import Sound
from clases.Texto import Texto

def conseguir_nombre():
    with open ("nombre.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

def conseguir_dificultad():
    with open ("difficulty.txt") as archivo:
        for linea in archivo.readlines():
            return str(linea.split("-")[0])

response = 0
boom = []
boomExplode = []
cont = 0
warning_text = ""

def practice(cursor, controller):
    global response, warning_text
    global boom
    global boomExplode
    global cont
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    music = Music()
    music.lvl_2()
    sound = Sound()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/mas_ciudad.png")
    background = pygame.transform.scale(background, size)
    vidaImage = pygame.image.load("assets/visual/gameplay_assets/navevidas.png")
    vidaImage = pygame.transform.scale(vidaImage, (25, 25))
    HUD = pygame.image.load("assets/visual/gameplay_assets/HUD.png")
    HUD = pygame.transform.scale(HUD, (325, 150))
    dialogo = pygame.image.load("assets/visual/gameplay_assets/dialogo_negro.png")
    dialogo_HERO = pygame.image.load("assets/visual/gameplay_assets/dialogo_negro_HERO.png")
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 18)
    # settings = pygame.image.load("assets/settings.png")
    clock = pygame.time.Clock()
    fps = 60
    ban = False
    cont = 0
    mag = True
    time = 1.2
    objarrg = []
    #enemigos
    cantidad = 20
    rows = 10000000000000000
    mainExplode = False
    response = 0

    boom = []
    boomExplode = []
    vidas = 5
    shields = []
    shield1 = Escudo(
        (int(width * .20), int(height * .75)),
        size,
        screen
    )
    shield2 = Escudo(
        (int(width * .5), int(height * .75)),
        size,
        screen
    )
    shield3 = Escudo(
        (int(width * .80), int(height * .75)),
        size,
        screen
    )

    shields.append(shield1)
    shields.append(shield2)
    shields.append(shield3)

    exCont = 0

    nave = Nave(
        (int(width * 0.50), int(height * 0.87)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    texto_nombre = Texto(
        conseguir_nombre(),
        (width * 0.1, height * 0.84),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_dificultad = Texto(
        conseguir_dificultad(),
        (width * 0.1, height * 0.87),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_level = Texto(
        "- practice",
        (width * 0.15, height * 0.87),
        font,
        screen,
        None,
        const.WHITE
    )

    texto_muerte = Texto(
        f"{conseguir_nombre()} NOOOOOOOOOOOOOOOOOO",
        (int(width * 0.15), int(height * 0.9)),
        font,
        screen,
        75,
        const.WHITE,
    )

    warning_text = Texto(
        "Presione esc o select en el control para salir",
        (int(width * 0.65), int(height * 0.92)),
        font,
        screen,
        30,
        const.WHITE,
    )

    warning_cont = [0]

    def exit_warning(screen, cont):
        global warning_text

        if cont[0] >= 90:
            cont[0] = 0

        cont[0] += 1

        if cont[0] >= 45:
            warning_text.show_text()

    def fire(character, objarrg):
        global boom
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y -= 10

        if len(objarrg) > 0:
            for x in objarrg:
                if character.misilrect.colliderect(x.rect):
                    #objarrg.remove(x)
                    boom.append(x)
                    character.misilrect.y = -100
                    break

    def explosion(list):
        global boom
        global cont
        for x in boom:
            x.explode()
            if x in list:
                list.remove(x)
        if len(boom) == 1 and cont > fps:
            boom.pop()

    def shield_enemy(shields, objarrg):
        for x in shields:
            for i in objarrg:
                if i.rect.colliderect(x.rect) and x.print and not i.damageShield:
                    i.damageShield = True
                    objarrg.remove(i)
                    if x.change:
                        x.destroy()
                        return
                    x.update(True)

    def main_enemy(nave, objarrg):
        damage = 0
        for i in objarrg:
            if i.rect.colliderect(nave.rect) and not i.damageNave:
                i.damageNave = True
                nave.exploded = True
                objarrg.remove(i)
                damage += 1
        return damage

    def magazine(screen, x, y, data):
        largo = 130
        ancho = 20
        calculo_barra = int((data/100 * largo))
        borde = pygame.Rect(x, y, 90, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, const.WHITE, borde, 3)
        pygame.draw.rect(screen, const.GREEN, rectangulo)


    def event_manager(controller):
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if controller != None:
                response = nave.event_manager(cont, controller, event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music.stop()
                    loading.loading("menu", cursor, controller)

            if event.type == pygame.JOYBUTTONDOWN:
                if event.joy == controller.get_id():
                    if event.button == xbox360_controller.BACK:
                        music.stop()
                        loading.loading("menu", cursor, controller)

        if response == 0:
            response = nave.event_manager_mouse(cont)

        if controller != None:
            controller_x = controller.get_left_stick()[0]
            nave.controller_update(controller_x)

    while True:
        event_manager(controller)
        if vidas <= 0:
            music.stop()
            sound.boss_explosion()
            cont = 0
            while vidas <= 0:
                cont += 1
                event_manager(controller)
                screen.blit(background, [width * 0, height * 0])
                screen.blit(nave.image, nave.rect)
                nave.update_explode_position_end()
                nave.explode_end(cont)
                if cont >= 60 * 4:
                    screen.blit(dialogo, [0, height - 200])
                    texto_muerte.show_text()
                if cont >= 60 * 8:
                    break
                pygame.display.flip()
                clock.tick(fps)
            loading.loading("menu", cursor, controller)

        screen.blit(background, [width * 0, height * 0])
        screen.blit(HUD, [0, height - 150])
        texto_nombre.show_text()
        texto_dificultad.show_text()
        texto_level.show_text()
        exit_warning(screen, warning_cont)
        screen.blit(nave.image, nave.rect)

        if rows > -1 and len(objarrg) == 0:
            while len(boom) > 0:
                boom.pop()

            for x in range(cantidad):
                num = random.randint(1, 3)
                if num == 1:
                    ship = "assets/visual/gameplay_assets/alien_ships/1.png"
                elif num == 2:
                    ship = "assets/visual/gameplay_assets/alien_ships/2.png"
                if num == 3:
                    ship = "assets/visual/gameplay_assets/alien_ships/3.png"

                enemy = MiniEnemy(
                    (int(width * 0.045 *(x+1)), int(height * (-.1))),
                    num,
                    size,
                    screen,
                    ship,
                    1.1
                )
                objarrg.append(enemy)

        magazine(screen, width * 0.01, height * .94, cont )
        for x in range(vidas):
            screen.blit(vidaImage, [width * 0.1 + (x * 40), height * .935])


        for i in objarrg:
            i.move()
            if not i.alive:
                objarrg.remove(i)
                vidas -= 1
            screen.blit(i.image, i.rect)

        if ban:
            if cont < fps * time:
                cont += 1
            fire(nave, objarrg)
            nave.get_frame()
            explosion(objarrg)

        if cont == fps * time:
            cont = 0
            mag = True
            ban = False


        if response != 0 and mag:
            mag = False
            nave.misilrect.center = response.center
            nave.misilrect.y -= nave.rect.y * .1
            ban = True


        if nave.exploded:
            exCont += 1
            nave.explode()
            if exCont >= 60 / 3:
                nave.exploded = False
                exCont = 0


        shield_enemy(shields, objarrg)

        for i in shields:
            if i.print:
                screen.blit(i.image, i.rect)
        vidas -= main_enemy(nave, objarrg)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
