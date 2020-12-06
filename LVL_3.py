import pygame, game_over
import sys
from pygame import mixer
from clases.Nave import Nave
import const
import main_menu
import random
from clases.Shield import Escudo
from clases.MiniEnemy import MiniEnemy
from clases.Enemy import Enemy
from clases.Music import Music
import boss_fight, intro_boss

response = 0
boom = []
boomExplode = []
cont = 0
enemyShoot = True
mainExplode = False

def lvl_3(difficulty, shields, vidas):
    global response
    global boom
    global boomExplode
    global cont
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
    pygame.display.set_icon(const.LOGO)
    music = Music()
    music.lvl_3()
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/last_level.png")
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
    rows = 0
    mainExplode = False
    response = 0
    boom = []
    boomExplode = []
    exCont = 0
    bigShip = []
    shootCont = [0, 0, 0]
    responseEnemy = [0, 0, 0]
    deathCont = [0, 0, 0]

    if difficulty == "easy" or difficulty == "easy ":
        print("enter")
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

    enemigo1 = Enemy(
        (int(width * 0.20), int(height * 0.15)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/other_ship.png"
    )
    enemigo2 = Enemy(
        (int(width * 0.50), int(height * 0.15)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/other_ship.png"
    )
    enemigo3 = Enemy(
        (int(width * 0.80), int(height * 0.15)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/other_ship.png"
    )

    bigShip.append(enemigo1)
    bigShip.append(enemigo2)
    bigShip.append(enemigo3)



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

    def shield_fire(shields, bigShip):
        for i in shields:
            for x in bigShip:
                if x.misilrect.colliderect(i.rect)and i.print:
                    x.misilrect.y = 900
                    if i.change:
                        i.destroy()
                        return
                    i.update(True)


    def main_enemy(nave, objarrg):
        damage = 0
        for i in objarrg:
            if i.rect.colliderect(nave.rect) and not i.damageNave:
                i.damageNave = True
                nave.exploded = True
                objarrg.remove(i)
                damage += 1
        return damage

    def main_bigShip(character, objarrg):
        if len(objarrg) > 0:
            for x in objarrg:
                if character.misilrect.colliderect(x.rect):
                    x.health -= 1
                    character.misilrect.y = -100
                    break


    def magazine(screen, x, y, data):
        largo  = 180
        ancho = 15
        calculo_barra = int((data/100 * largo))
        borde = pygame.Rect(x, y, 130, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, (255, 255, 255), borde, 3)
        pygame.draw.rect(screen, (255, 255, 255), rectangulo)

    def enemyFire(character, objarrg):
        global mainExplode
        global enemyShoot
        global vidas
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y += 10
        if character.misilrect.colliderect(objarrg.rect):
            vidas -= 1
            objarrg.exploded = True
            character.misilrect.y = 900
            enemyShoot = False


    def event_manager():
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        response = nave.event_manager(cont)

    while True:
        event_manager()
        if vidas <= 0:
            game_over.game_over()
            #boss_fight.boss_fight(difficulty, shields, vidas)
        if rows <= 0 and len(bigShip) <= 0:
            intro_boss.intro_boss(difficulty, shields, vidas)
            break
        screen.blit(background, [width * 0, height * 0])
        screen.blit(nave.image, nave.rect)
        if rows > 0 and len(objarrg) == 0:
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

        for x in bigShip:
            screen.blit(x.image, x.rect)

        if ban:
            if cont < fps * time:
                cont += 1
            fire(nave, objarrg)
            main_bigShip(nave, bigShip)
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
        step = 0
        for x in bigShip:
            shootCont[step] += 1
            responseEnemy[step] = x.event_manager(shootCont[step])
            if responseEnemy[step] != 0:
                x.misilrect.center = responseEnemy[step].center
                #bigShip[x].misilrect.y += bigShip[x].rect.y * .1
            if shootCont[step] >= 180:
                if x.misilrect.y > height:
                    shootCont[step] = 0
                enemyFire(x, nave)
                shield_fire(shields, bigShip)
            step += 1

        for x in bigShip:
            if x.health <= 0:
                deathCont[bigShip.index(x)] += 1
                if deathCont[bigShip.index(x)] >= 60:
                    shootCont.pop(bigShip.index(x))
                    responseEnemy.pop(bigShip.index(x))
                    deathCont.pop(bigShip.index(x))
                    bigShip.remove(x)
                x.explode()


        shield_enemy(shields, objarrg)

        for i in shields:
            if i.print:
                screen.blit(i.image, i.rect)
        vidas -= main_enemy(nave, objarrg)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
