import pygame, boss_end_scene, game_over
import sys
from pygame import mixer
from clases.Music import Music
from clases.Sound import Sound
from clases.Nave import Nave
import const
from clases.Enemy import Enemy
from clases.MiniEnemy import MiniEnemy
import main_menu, endgame_history
import random
from clases.Kboom import Explosion
from clases.Boss import Boss
from clases.BigLaser import Laser
from clases.Shield import Escudo
from clases.SpecialLaser import SpecialLaser
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
objeto2 = 0
objeto3 = 0
boom = []
cont = 0
enemyShoot = True
mainExplode = False
nave = 0
objeto1 = 0
boss = 0
def boss_fight(cursor, controller, difficulty, shields, vidas):
    global nave
    global response
    global objeto3
    global boom
    global cont
    global objeto2
    global mainExplode
    global enemyShoot
    global objeto1
    global boss
    music = Music()
    sound = Sound()
    #pygame.mixer.music.load("assets/music/special_tracks/teachmenow.mp3")
    #pygame.mixer.music.set_volume(.1)
    #pygame.mixer.music.play(-1)
    width = 1200
    height = 800
    size = (width, height)
    screen = pygame.display.set_mode(size)

    #Global values
    background = pygame.image.load("assets/visual/gameplay_assets/boss_background.png")
    background = pygame.transform.scale(background, size)
    vidaImage = pygame.image.load("assets/visual/gameplay_assets/navevidas.png")
    vidaImage = pygame.transform.scale(vidaImage, (25, 25))
    HUD = pygame.image.load("assets/visual/gameplay_assets/HUD.png")
    HUD = pygame.transform.scale(HUD, (325, 150))
    dialogo = pygame.image.load("assets/visual/gameplay_assets/dialogo_negro.png")
    font = pygame.font.Font("fonts/Pixel LCD-7.ttf", 18)
    # settings = pygame.image.load("assets/settings.png")
    clock = pygame.time.Clock()
    fps = 60
    ban = False
    cont = 0
    mag = True
    time = 1.2
    objarrg = []
    cantidad = 1
    shootCont = 0
    exCont = 0
    enemyShoot = True
    boolEnemy = True
    mainExplode = False
    response = 0
    attCont = 0
    objeto1 = 0
    objeto2 = 0
    objeto3 = 0
    boom = []
    shootCont = [0, 0, 0]
    responseEnemy = [0, 0, 0]
    deathCont = [0, 0, 0]
    step = 0
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

    boss = Boss(
        (int(width * 0.50), int(height * 0.35)),
        size,
        screen
    )
    backup = boss.health / 4
    nave = Nave(
        (int(width * 0.50), int(height * 0.9)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )
    spcLaser = Laser(
        (int(boss.rect.center[0] + 10), int(boss.rect.center[1]) + 435),
        size
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
        "- Boss",
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

    def nave_Laser(nave, blueLaser):

        damage = 0
        if nave.rect.colliderect((blueLaser.rect.x, 0, 144, 800)) and not blueLaser.hit_ship:
            blueLaser.hit_ship = True
            damage = 2

        return damage

    def startLaser():
        global objeto1
        laser = SpecialLaser(
            (0, 0),
            size
        )

        objeto1 = laser

    def moveLaser(laser):
        global nave
        if laser.num < 0:
            laser.num = nave.rect.center[0]
        laser.update()
        screen.blit(laser.image, (laser.rect[0], 0))

    def bigShips():
        global objeto2
        bigShip = []
        size = (1200, 800)
        screen = pygame.display.set_mode(size)
        enemigo1 = Enemy(
            (int(width * 0.20), int(height * -0.15)),
            5,
            size,
            screen,
            "assets/visual/gameplay_assets/other_ship.png"
        )
        enemigo2 = Enemy(
            (int(width * 0.50), int(height * -0.15)),
            5,
            size,
            screen,
            "assets/visual/gameplay_assets/other_ship.png"
        )
        enemigo3 = Enemy(
            (int(width * 0.80), int(height * -0.15)),
            5,
            size,
            screen,
            "assets/visual/gameplay_assets/other_ship.png"
        )

        bigShip.append(enemigo1)
        bigShip.append(enemigo2)
        bigShip.append(enemigo3)


        objeto2 = bigShip

    def print_Enemy(bigShip):
        for x in bigShip:
            x.move()
            screen.blit(x.image, x.rect)

    def enemyFire(character, objarrg):
        global mainExplode
        global enemyShoot

        damage = 0
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y += 10
        if character.misilrect.colliderect(objarrg.rect):
            damage = 1
            objarrg.exploded = True
            character.misilrect.y = 900
            enemyShoot = False

        return damage

    def shield_fire(shields, bigShip):
        for i in shields:
            for x in bigShip:
                if x.misilrect.colliderect(i.rect)and i.print:
                    x.misilrect.y = 900
                    if i.change:
                        i.destroy()
                        return
                    i.update(True)

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

    def explosion(list):
        global boom
        global cont
        for x in boom:
            x.explode()
            if x in list:
                list.remove(x)
        if len(boom) == 1 and cont > fps:
            boom.pop()

    def select_attack(boss):
        global objeto2
        global objeto3
        list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
        attack = random.randint(0, len(list) - 1)
        if list[attack] == 1:
            startLaser()
        if list[attack] == 2:
            bigShips()
            #print(objeto2)
        if list[attack] == 3:
            smallEnemy((1200, 800))

    def smallEnemy(size):
        global boss
        global objeto3
        global boom
        boom = []
        objarrg = []
        screen = pygame.display.set_mode(size)
        for x in range(20):
            num = random.randint(1, 3)
            if num == 1:
                ship = "assets/visual/gameplay_assets/alien_ships/1.png"
            elif num == 2:
                ship = "assets/visual/gameplay_assets/alien_ships/2.png"
            if num == 3:
                ship = "assets/visual/gameplay_assets/alien_ships/3.png"
            enemy = MiniEnemy(
                (int(1200 * 0.045 *(x+1)), int(800 * (-.1))),
                num,
                size,
                screen,
                ship,
                boss.enrage
            )
            print(enemy.movementSpeed)
            objarrg.append(enemy)

        objeto3 = objarrg

    def fire(character, objarrg):
        global boom
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        #character.misilrect.y -= 10

        if len(objarrg) > 0:
            for x in objarrg:
                if character.misilrect.colliderect(x.rect):
                    #objarrg.remove(x)
                    boom.append(x)
                    character.misilrect.y = -100
                    break

    def health_bar(screen, x, y, boss):
        largo  = 800
        ancho = 15
        calculo_barra = int((boss.health/100 * largo))
        borde = pygame.Rect(x, y, largo, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, (255, 0, 0), borde)
        if boss.health > 0:
            pygame.draw.rect(screen, (0, 255, 0), rectangulo)

    def magazine(screen, x, y, data):
        largo = 130
        ancho = 20
        calculo_barra = int((data/100 * largo))
        borde = pygame.Rect(x, y, 90, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, const.WHITE, borde, 3)
        pygame.draw.rect(screen, const.GREEN, rectangulo)

    def specialLaser(spcLaser):
        if not spcLaser.off:
            screen.blit(spcLaser.image, spcLaser.rect)
        spcLaser.update()

    def shootBoss(character, boss):
          screen.blit(character.misilimage, character.misilrect)
          character.get_frame()
          character.misilrect.y -= 10

          if boss.hit_left >= 4 and boss.hit_right >= 4:
              boss.contador += 1
              if character.misilrect.colliderect(boss.hitBox_center):
                  boss.health -= 4
                  character.misilrect.y = -100

          if boss.hit_left < 4:
              if character.misilrect.colliderect(boss.hitBox_left):
                  boss.hit_left += 1
                  character.misilrect.y = -100
                  boss.health -= 1

          if boss.hit_right < 4:
              if character.misilrect.colliderect(boss.hitBox_right):
                  boss.hit_right += 1
                  character.misilrect.y = -100
                  boss.health -= 1

          if boss.hit_left == 4 and not boss.boom_left.boom_end:
              boss.explode()
          if boss.hit_right == 4 and not boss.boom_right.boom_end:
              boss.explode_right()


          if boss.contador > 60 * 8:
              boss.contador = 0
              boss.hit_left = 0
              boss.hit_right = 0
              boss.boom_left.boom_end = False
              boss.boom_right.boom_end = False

    def event_manager(controller):
        global step
        global response

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if controller != None:
                response = nave.event_manager(mag, controller, event)

        if response == 0:
            response = nave.event_manager_mouse(mag)

        if controller != None:
            controller_x = controller.get_left_stick()[0]
            nave.controller_update(controller_x)

    def spcLaser_nave(nave, spcLaser):
        damage = 0

        if nave.rect.colliderect((spcLaser.rect.x + 60, spcLaser.rect.y, 154 - 155, 954)) and not spcLaser.off and not spcLaser.hit_ship:
            spcLaser.hit_ship = True
            damage = 1

        return damage

    def main_enemy(nave, objarrg):
        damage = 0
        for i in objarrg:
            if i.rect.colliderect(nave.rect) and not i.damageNave:
                i.damageNave = True
                nave.exploded = True
                objarrg.remove(i)
                damage += 1
        return damage

    def bigLaser(spcLaser, shields):
        for x in shields:
            if spcLaser.rect.colliderect(x) and not spcLaser.off:
                if x.change:
                    x.destroy()
                    return
                x.update(True)


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
            game_over.game_over(cursor, controller)
        if boss.health <= 0:
            sound.boss_explosion()
            music.stop()
            while boss.health <= 0:
                cont += 1
                event_manager(controller)
                screen.blit(background, [width * 0, height * 0])
                boss.update()
                screen.blit(boss.image,boss.rect)
                screen.blit(nave.image, nave.rect)
                health_bar(screen, 200, 30, boss)

                boss.explode_end()
                #duración 8 secs
                if cont >= 60 * 5:
                    #Aqui puedo poner una escena despues de derrotar al boss
                    boss_end_scene.boss_end_scene((nave.rect.x, nave.rect.y), cursor, controller)
                    break

                pygame.display.flip()
                clock.tick(fps)
            break
        screen.blit(background, [width * 0, height * 0])
        screen.blit(HUD, [0, height - 150])
        texto_nombre.show_text()
        texto_dificultad.show_text()
        texto_level.show_text()
        boss.update()
        screen.blit(boss.image,boss.rect)
        screen.blit(nave.image, nave.rect)

        magazine(screen, width * 0.01, height * .94, cont )
        for x in range(vidas):
            screen.blit(vidaImage, [width * 0.1 + (x * 40), height * .935])
        if objeto1 != 0:
            moveLaser(objeto1)
        if objeto3 != 0:
            if len(objeto3) == 0:
                attCont = 0
                boss.activity = False
                objeto3 = 0
            else:
                for i in objeto3:
                    i.move()
                    if not i.alive:
                        objeto3.remove(i)
                    screen.blit(i.image, i.rect)

        if objeto2 != 0:
            boss.activity = True
            print_Enemy(objeto2)

        specialLaser(spcLaser)
        if ban:
            if cont < fps * time:
                cont += 1
            if objeto3 != 0:
                fire(nave, objeto3)
                explosion(objeto3)
            shootBoss(nave, boss)
            nave.get_frame()

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

        attCont += 1
        if attCont == fps * boss.attTime and not boss.activity:
            boss.activity = True
            select_attack(boss)
            attCont = 0


        step = 0
        if objeto2 != 0 and len(objeto2) > 0:
            for x in objeto2:
                shootCont[step] += 1
                responseEnemy[step] = x.event_manager(shootCont[step])
                if responseEnemy[step] != 0:
                    x.misilrect.center = responseEnemy[step].center
                      #objeto2[x].misilrect.y += objeto2[x].rect.y * .1
                if shootCont[step] >= 180:
                    if x.misilrect.y > height:
                          shootCont[step] = 0

                    vidas -= enemyFire(x, nave)
                    shield_fire(shields, objeto2)
                step += 1

        if objeto2 != 0:
            if objeto2[0].cont > 800:
                    shootCont = [0, 0, 0]
                    responseEnemy = [0, 0, 0]
                    deathCont = [0, 0, 0]
                    objeto2 = 0
            boss.activity = False
            attCont = 0
        if boss.health <= backup:
            spcLaser.speed = 270
            boss.attTime = 6
            boss.enrage = 2

        vidas -= spcLaser_nave(nave, spcLaser)
        health_bar(screen, 200, 30, boss)
        if objeto3 != 0:
            shield_enemy(shields, objeto3)
            vidas -= main_enemy(nave, objeto3)
        boss.show()
        bigLaser(spcLaser, shields)
        for i in shields:
            if i.print:
                screen.blit(i.image, i.rect)
        if objeto1 != 0:
            if objeto1.rect.x <= -150 or objeto1.rect.x >= 1350:
                objeto1 = 0
                attCont = 0
                boss.activity = False
        if objeto1 != 0:
            vidas -= nave_Laser(nave, objeto1)
            moveLaser(objeto1)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
