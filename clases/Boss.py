import pygame
from clases.MiniKboom import Explosion
from clases.Kboom import Explosion

class Boss(pygame.sprite.Sprite):
    def __init__(self, position, screenSize, screen):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/boss_frames/Boss_Sheet_v5.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.x_value = 697.6
        self.y_value = 505.5
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
            5:(self.x_value * 5, self.y_value * 0, self.x_value, self.y_value), 6:(self.x_value * 6, self.y_value * 0, self.x_value, self.y_value), 7:(self.x_value * 7, self.y_value * 0, self.x_value, self.y_value), 8:(self.x_value * 8, self.y_value * 0, self.x_value, self.y_value), 9:(self.x_value * 9, self.y_value * 0, self.x_value, self.y_value),
            10:(self.x_value * 0, self.y_value * 1, self.x_value, self.y_value), 11:(self.x_value * 1, self.y_value * 1, self.x_value, self.y_value), 12:(self.x_value * 2, self.y_value * 1, self.x_value, self.y_value), 13:(self.x_value * 3, self.y_value * 1, self.x_value, self.y_value), 14:(self.x_value * 4, self.y_value * 1, self.x_value, self.y_value),
            15:(self.x_value * 5, self.y_value * 1, self.x_value, self.y_value), 16:(self.x_value * 6, self.y_value * 1, self.x_value, self.y_value), 17:(self.x_value * 7, self.y_value * 1, self.x_value, self.y_value), 18:(self.x_value * 8, self.y_value * 1, self.x_value, self.y_value), 19:(self.x_value * 9, self.y_value * 1, self.x_value, self.y_value),
        }
        self.frame = 0
        self.cont = 0
        self.secs = 2
        self.hitBox_center = ((self.rect.center[0] - 40, self.rect.center[1] - 30), (70, 10))
        self.hitBox_left = ((self.rect.center[0] - 120, self.rect.center[1] - 30), (10, 10)) #-117, -23
        self.hitBox_right = ((self.rect.center[0] + 101, self.rect.center[1] - 30), (10, 10))#+105, -23
        self.screen = screen
        self.contador = 0
        self.hit_left = 0
        self.hit_right = 0
        self.health = 0
        self.attTime = 10
        self.activity = False
        self.boom_left = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.boom_right = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )

        self.enrage = 1

        #End
        self.boom1 = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.boom2 = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.boom3 = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.boom4 = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.boom5 = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )


    def explode_end(self):
        # self.update_explode_position()
        self.boom1.update()
        self.screen.blit(self.boom1.image, (self.rect.center[0] - 300, self.rect.center[1] - 300))
        self.boom2.update()
        self.screen.blit(self.boom2.image, (self.rect.center[0] + 50, self.rect.center[1] - 300))
        self.boom3.update()
        self.screen.blit(self.boom3.image, (self.rect.center[0] - 330, self.rect.center[1] - 10))
        self.boom4.update()
        self.screen.blit(self.boom4.image, (self.rect.center[0] + 100, self.rect.center[1] - 10))
        self.boom5.update()
        self.screen.blit(self.boom5.image, (self.rect.center[0] - 120, self.rect.center[1] - 140))

    def update_explode_position(self):
        self.boom_left.rect.x, self.boom_left.rect.y = (self.rect.center[0] - 120, self.rect.center[1] - 30)

    def explode(self):
        # self.update_explode_position()
        self.boom_left.update()
        self.screen.blit(self.boom_left.image, (self.rect.center[0] - 150, self.rect.center[1] - 80))

    def update_explode_position_right(self):
          self.boom_right.rect.x, self.boom_right.rect.y = (self.rect.center[0] - 120, self.rect.center[1] - 30)

    def explode_right(self):
          # self.update_explode_position()
          self.boom_right.update()
          self.screen.blit(self.boom_right.image, (self.rect.center[0] + 80, self.rect.center[1] - 80))

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

    def show(self):
        pygame.draw.rect(self.screen, (255, 0, 0),  self.hitBox_center, 1)
        pygame.draw.rect(self.screen, (255, 0, 0),  self.hitBox_left)
        pygame.draw.rect(self.screen, (255, 0, 0),  self.hitBox_right)
