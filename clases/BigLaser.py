import pygame
import random

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, screenSize):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/gameplay_assets/laser/boss_laser.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.x_value = 1850/12
        self.y_value = 318
        self.sheet.set_clip(pygame.Rect(0, 0, self.x_value, self.y_value ))
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
            0:(0, 0, self.x_value, self.y_value), 1:(self.x_value, 0, self.x_value, self.y_value), 2:(self.x_value * 2, 0, self.x_value, self.y_value), 3:(self.x_value * 3, 0, self.x_value, self.y_value),
            4:(self.x_value * 4, 0, self.x_value, self.y_value), 5:(self.x_value * 5, self.y_value * 0, self.x_value, self.y_value), 6:(self.x_value * 6, self.y_value * 0, self.x_value, self.y_value), 7:(self.x_value * 7, self.y_value * 0, self.x_value, self.y_value),
            8:(self.x_value * 8, self.y_value * 0, self.x_value, self.y_value), 9:(self.x_value * 9, self.y_value * 0, self.x_value, self.y_value), 10:(self.x_value * 10, self.y_value * 0, self.x_value, self.y_value), 11:(self.x_value * 11, self.y_value * 0, self.x_value, self.y_value)
        }
        self.frame = 0
        self.cont = 0
        self.secs = 1
        self.off = False
        self.random1 = random.randint(0, 3)
        self.random2 = random.randint(4, 7)

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
        self.rect.x += 2.5


        if self.rect.x > 100 * self.random1 and self.rect.x < (100 * (self.random1 + 1) + 50) or self.rect.x > 100 * self.random2 and self.rect.x < (100 * (self.random2 + 1) + 50):
            self.off = True
        else:
            self.off = False

        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
