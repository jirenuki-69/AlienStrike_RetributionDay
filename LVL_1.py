import pygame
import sys
from pygame import mixer
from clases.Nave import Nave
import const
import main_menu
import random
from clases.Shield import Escudo
from clases.MiniEnemy import MiniEnemy
from clases.Music import Music
import LVL_2



response = 0
boom = []
boomExplode = []
cont = 0
def lvl_1():
    global response
    global boom
    global boomExplode
    global cont
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    music = Music()
    music.lvl_1()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/BG_level1.png")
    background = pygame.transform.scale(background, size)
    vidaImage = pygame.image.load("assets/visual/gameplay_assets/navevidas.png")
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
    rows = 3
    mainExplode = False
    response = 0
    shields = []
    boom = []
    boomExplode = []
    vidas = 5
    exCont = 0

    def conseguir_dificultad():
        with open ("difficulty.txt") as archivo:
            for linea in archivo.readlines():
                return str(linea.split("-")[0])

    difficulty = conseguir_dificultad()

    print(len(difficulty))

    nave = Nave(
        (int(width * 0.50), int(height * 0.87)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )
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
        largo  = 180
        ancho = 15
        calculo_barra = int((data/100 * largo))
        borde = pygame.Rect(x, y, 130, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, (255, 255, 255), borde, 3)
        pygame.draw.rect(screen, (255, 255, 255), rectangulo)


    def event_manager():
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        response = nave.event_manager()

    while True:
        event_manager()
        if vidas <= 0:
            #de aqui
            cont = 0
            while vidas <= 0:
                cont += 1
                event_manager()
                screen.blit(background, [width * 0, height * 0])
                screen.blit(nave.image, nave.rect)
                magazine(screen, width * 0, height * .97, 0 )
                for x in range(vidas):
                    if x == 0:
                        screen.blit(vidaImage, [width - 40 * (x) - 40 - 1, height * .95])
                    else:
                        screen.blit(vidaImage, [width - 40 * (x) - 40 - (10 * x), height * .95])
                nave.update_explode_position_end()
                nave.explode_end(cont)
                if cont >= 60 * 5:
                    break
                pygame.display.flip()
                clock.tick(fps)
            #termina
            break
        if rows < 0:
            LVL_2.lvl_2(difficulty, shields, vidas)
        screen.blit(background, [width * 0, height * 0])
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
                    1
                )
                objarrg.append(enemy)
            rows -= 1

        magazine(screen, width * 0, height * .97, cont )
        for x in range(vidas):
            if x == 0:
                screen.blit(vidaImage, [width - 40 * (x) - 40 - 1, height * .95])
            else:
                screen.blit(vidaImage, [width - 40 * (x) - 40 - (10 * x), height * .95])


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
