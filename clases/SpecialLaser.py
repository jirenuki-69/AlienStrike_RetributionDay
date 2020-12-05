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
        self.laser_start = None
        self.num = -1
        self.move_left = False
        self.move_right = False
        self.enter = False
        self.direction = 1

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


    def update(self):
        if not self.enter:
            self.enter = True
            if self.num < 600:
                self.laser_start = "-+"
            if self.num >= 600:
                self.laser_start = "+-"

        if self.laser_start == "-+":
            self.rect.x = -144
            self.laser_start = None
            self.move_right = True
            self.move_left = False

        if self.laser_start == "+-":
            self.laser_start = None
            self.move_left = True
            self.move_right = False
            self.rect.x = 1200

        if self.move_right:
            if self.rect.x >= 466:
                self.direction = -1
            self.rect.x += 2 * self.direction
        if self.move_left:
            if self.rect.x < 600:
                self.direction = -1
            self.rect.x -= 2 * self.direction

        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
