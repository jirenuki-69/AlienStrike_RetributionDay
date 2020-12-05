import pygame
import random

class SpecialLaser(pygame.sprite.Sprite):
    def __init__(self, position, screenSize):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/gameplay_assets/laser/special_laser.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.x_value = 288/2
        self.y_value = 800
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
            0:(0, 0, self.x_value, self.y_value), 1:(self.x_value, 0, self.x_value, self.y_value)
        }
        self.frame = 0
        self.cont = 0
        self.secs = 1
        self.off = True
        self.direction = True
        self.hit_ship = False
        self.ship_value = True
        self.num = 0

    def get_frame(self, frame_set):
        if self.cont % 5 * self.secs == 0:
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


    def update(self, ship):

        if self.ship_value:
            self.num = ship
            self.ship_value = False

        if self.num <= 600:
            if self.direction:
                print(self.rect.center[0])
                self.rect.center = (0, self.rect.center[1])
                self.direction = False
            self.rect.x += 2.5
        elif self.num > 600 and not self.direction:
            self.rect.x -= 2.5

        if self.num > 600:
            if self.direction:
                self.rect.center = (1100, self.rect.center[1])
                self.direciton = False
            self.rect.x -= 2.5
        elif self.num <= 600 and not self.direction:
            self.rect.x += 2.5



        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
