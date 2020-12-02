import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, screenSize, screen):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/boss_frames/Boss_Sheet_v2.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.x_value = 872
        self.y_value = 632
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
            0:(0, 0, self.x_value, self.y_value), 1:(self.x_value, 0, self.x_value, self.y_value), 2:(self.x_value * 2, 0, self.x_value, self.y_value), 3:(self.x_value * 3, 0, self.x_value, self.y_value), 4:(self.x_value * 4, 0, self.x_value, self.y_value),
            5:(self.x_value * 5, 0, self.x_value, self.y_value), 6:(self.x_value * 6, 0, self.x_value, self.y_value), 7:(self.x_value * 7, 0, self.x_value, self.y_value), 8:(self.x_value * 8, 0, self.x_value, self.y_value), 9:(self.x_value * 9, 0, self.x_value, self.y_value),
            10:(self.x_value * 10, 0 * 2, self.x_value, self.y_value), 11:(self.x_value * 11, 0 * 2, self.x_value, self.y_value), 12:(self.x_value * 12, 0 * 2, self.x_value, self.y_value), 13:(self.x_value * 13, 0 * 2, self.x_value, self.y_value), 14:(self.x_value * 14, 0 * 2, self.x_value, self.y_value),
            15:(self.x_value * 15, 0, self.x_value, self.y_value), 16:(self.x_value * 16, 0, self.x_value, self.y_value), 17:(self.x_value * 17, 0, self.x_value, self.y_value), 18:(self.x_value * 18, 0, self.x_value, self.y_value), 19:(self.x_value * 19, 0, self.x_value, self.y_value),
        }
        self.frame = 0
        self.cont = 0
        self.secs = 2

    def get_frame(self, frame_set):
        if self.cont % 3 * self.secs == 0:
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


        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
