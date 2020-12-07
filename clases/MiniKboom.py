import pygame
#from pygame import mixer
from clases.Sound import Sound

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, screenSize):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/smaller_boom.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 62.33 ))
        #Se genera el surface para mostrar algo en la pantalla
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #Se representa la imagen y moverla
        self.rect = self.image.get_rect()
        #Paso el rect a la posicion del personaje
        self.rect.center = position
        #En qué superficie se encuentra
        self.screenSize = screenSize
        #States
        self.states = {
            0:(0, 0, 64, 62.33), 1:(64, 0, 64, 62.33), 2:(128, 0, 64, 62.33), 3:(192, 0, 64, 62.33), 4:(256, 0, 64, 62.33),
            5:(0, 62.33, 64, 62.33), 6:(64, 62.33, 64, 62.33), 7:(128, 62.33, 64, 62.33), 8:(192, 62.33, 64, 62.33), 9:(256, 62.33, 64, 62.33),
            10:(0, 124.66, 64, 62.33), 11:(64, 124.66, 64, 62.33), 12:(128, 124.66, 64, 62.33), 13:(192, 124.66, 64, 62.33), 14:(256, 124.66, 64, 62.33),
        }
        self.frame = 0
        self.cont = 0
        self.secs = 1
        self.boom_initiaded = False
        self.exploded = False
        self.boom_end = False

        self.sound = Sound()

    def get_frame(self, frame_set):
        if self.cont % 4 * self.secs == 0:
            self.frame += 1
        if self.frame > (len(frame_set) - 1):

            self.frame = 0
        return frame_set[self.frame]


    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))

        return clipped_rect


    def update(self):
        if self.cont > 60 * self.secs:
            self.cont = 0
            self.boom_end = True
            #self.exploded = True
            #self.boom_sound.stop()
            self.boom_initiaded = False

        if not self.boom_initiaded:
            self.sound.alien_explosion()
            self.boom_initiaded = True

        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
