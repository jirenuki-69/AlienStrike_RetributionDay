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

response = 0
def lvl_1():
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
    background = pygame.image.load("assets/visual/gameplay_assets/BG_level1.png")
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
    mainExplode = False
    response = 0


    nave = Nave(
        (int(width * 0.50), int(height * 0.9)),
        5,
        size,
        screen,
        "assets/visual/gameplay_assets/main_ship.png"
    )


    def fire(character, objarrg):
        global exploded
        screen.blit(character.misilimage, character.misilrect)
        character.get_frame()
        character.misilrect.y -= 10
        #if len(objarrg) > 0:
            #for x in objarrg:
                #if character.misilrect.colliderect(x.rect):
                    #objarrg.remove(x)
                    #print("hit")
                    #exploded = True
                    #character.misilrect.y = -100

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
        screen.blit(nave.image, nave.rect)
        print(cont)
        if ban:
            if cont < fps * time:
                cont += 1
            fire(nave, objarrg)
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

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
