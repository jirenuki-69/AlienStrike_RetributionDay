import pygame
import sys
from pygame import mixer
from clases.Nave import Nave
import const
from clases.Enemy import Enemy
import main_menu
import random
from clases.Kboom import Explosion
from clases.Boss import Boss
from clases.BigLaser import Laser

response = 0
def boss_fight():
    global response
    pygame.init()
    pygame.display.set_caption("Alien Strike: Retribution Day")
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
    # settings = pygame.image.load("assets/settings.png")
    clock = pygame.time.Clock()
    fps = 60
    ban = False
    cont = 0
    mag = True
    time = 1.5
    objarrg = []
    cantidad = 1
    shootCont = 0
    exCont = 0
    enemyShoot = True
    boolEnemy = True
    mainExplode = False
    response = 0


    boss = Boss(
        (int(width * 0.50), int(height * 0.35)),
        size,
        screen
    )
    nave = Nave(
        (int(width * 0.50), int(height * 0.9)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )
    spcLaser = Laser(
        (int(width * (-.1)), int(height * 0.8)),
        size
    )

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
        largo  = 180
        ancho = 15
        calculo_barra = int((data/100 * largo))
        borde = pygame.Rect(x, y, 160, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, (255, 255, 255), borde, 3)
        pygame.draw.rect(screen, (255, 255, 255), rectangulo)


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

          if boss.hit_right < 4:
              if character.misilrect.colliderect(boss.hitBox_right):
                  boss.hit_right += 1
                  character.misilrect.y = -100

          if boss.contador > 60 * 8:
              boss.contador = 0
              boss.hit_left = 0
              boss.hit_right = 0

    def event_manager():
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        response = nave.event_manager()

    while True:
        event_manager()
        screen.blit(background, [width * 0, height * 0])
        boss.update()
        screen.blit(boss.image,boss.rect)
        screen.blit(nave.image, nave.rect)
        #specialLaser(spcLaser)
        magazine(screen, width * 0, height * .97, cont )
        if ban:
            if cont < fps * time:
                cont += 1
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
        health_bar(screen, 200, 30, boss)
        boss.show()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

boss_fight()
