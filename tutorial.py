import pygame
import sys
from pygame import mixer
from clases.Nave import Nave
import const
from clases.Enemy import Enemy
import main_menu
import random
from clases.Kboom import Explosion

step = 0
response = 0
exploded = False
EnemyShoot = True
mainExplode = False
def tutorial():
    global enemyShoot
    global step
    global exploded
    global mainExplode
    step = 0
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
    background = pygame.image.load("assets/visual/gameplay_assets/gencity.png")
    background = pygame.transform.scale(background, size)
    # settings = pygame.image.load("assets/settings.png")
    dialogo = pygame.image.load("assets/visual/gameplay_assets/Tutorial/tutoverde.png")
    gui_movement = pygame.image.load("assets/visual/gameplay_assets/Tutorial/movement.png")
    gui_shoot = pygame.image.load("assets/visual/gameplay_assets/Tutorial/shoot.png")
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



    nave = Nave(
        (int(width * 0.10), int(height * 0.65)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )

    #My values
    rectSize = (275, 100)

    def text(data, x, y, color, size, screen):
        font = pygame.font.Font(const.FONT_v2, size)
        texto_marcador = font.render(data, True, color)
        texto_marcador_rect = texto_marcador.get_rect()
        screen_rec = screen.get_rect()

        texto_marcador_rect.center = screen_rec.center

        if x == -1:
            x = texto_marcador_rect[0]
        if y == -1:
            y = texto_marcador_rect[1]

        screen.blit(texto_marcador, [x, y, texto_marcador_rect[2],  texto_marcador_rect[3]])

    def fire(character, objarrg):
        global exploded
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y -= 10
        if len(objarrg) > 0:
            for x in objarrg:
                if character.misilrect.colliderect(x.rect):
                    #objarrg.remove(x)
                    #print("hit")
                    exploded = True
                    character.misilrect.y = -100

    def enemyFire(character, objarrg):
        global mainExplode
        global enemyShoot
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y += 10
        if character.misilrect.colliderect(objarrg.rect):
            mainExplode = True
            character.misilrect.y = -100
            enemyShoot = False


    def event_manager():
        global step
        global response
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if step == len(const.TUTORIAL) - 1:
                        main_menu.main_menu()
                    step += 1



        response = nave.event_manager()

    while True:
        event_manager()
        screen.blit(background, [width * 0, height * 0])
        screen.blit(dialogo, [0, height - 200])


        if ban:
            if cont < fps * time:
                cont += 1
            fire(nave, objarrg)
            nave.get_frame()

        if step == 1 or step == 2:
            screen.blit(gui_movement, [width * 0.7, height * 0.05])

        if step == 3 or step == 4:
            screen.blit(gui_shoot, [width * 0.7, height * 0.05])

        screen.blit(nave.image, nave.rect)
        text(const.TUTORIAL[step], width * .135, height * .88, const.BLACK, 18, screen)
        if cont == fps * time:
            cont = 0
            mag = True

        if response != 0 and mag and step !=5:
            mag = False
            nave.misilrect.center = response.center
            nave.misilrect.y -= nave.rect.y * .1
            ban = True

        if step == 4 or step == 5:
            if len(objarrg) < cantidad:
                for x in range(cantidad):
                    objenemy = Enemy(
                        (int(width * 0.10 * 1), int(height * 0.15)),
                        5,
                        size,
                        screen,
                        "assets/visual/gameplay_assets/other_ship.png"
                    )
                    objarrg.append(objenemy)
            screen.blit(objarrg[0].image, (int(nave.rect.x), int(objarrg[0].rect.y)))
            objarrg[0].rect.x = int(nave.rect.x)
            nave.movementSpeed = 0
        else:
            nave.movementSpeed = 5

        if step == 5:
            shootCont += 1
            responseEnemy = objarrg[0].event_manager(shootCont)
            if responseEnemy != 0:
                objarrg[0].misilrect.center = responseEnemy.center
                #objarrg[0].misilrect.y += objarrg[0].rect.y * .1
            if shootCont >= 180 and enemyShoot:
                if boolEnemy:
                    objarrg[0].misilrect.y += objarrg[0].rect.y * 1
                    boolEnemy = False
                enemyFire(objarrg[0], nave)


        if exploded:
            exCont += 1
            objarrg[0].explode()
            if exCont >= 60 * 1:
                exploded = False
                exCont = 0

        if mainExplode:
            exCont += 1
            nave.explode()
            if exCont >= 60 / 3:
                mainExplode = False
                exCont = 0

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
