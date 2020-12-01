import pygame
#from pygame import mixer

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, screenSize):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/boom_sprites.png")
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.sheet.set_clip(pygame.Rect(0, 0, 256, 249.33 ))
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
            0:(0, 0, 256, 249.33), 1:(256, 0, 256, 249.33), 2:(512, 0, 256, 249.33), 3:(768, 0, 256, 249.33), 4:(1024, 0, 256, 249.33),
            5:(0, 249.33, 256, 249.33), 6:(256, 249.33, 256, 249.33), 7:(512, 249.33, 256, 249.33), 8:(768, 249.33, 256, 249.33), 9:(1024, 249.33, 256, 249.33),
            10:(0, 498.66, 256, 249.33), 11:(256, 498.66, 256, 249.33), 12:(512, 498.66, 256, 249.33), 13:(768, 498.66, 256, 249.33), 14:(1024, 498.66, 256, 249.33),
        }
        self.frame = 0
        self.cont = 0
        self.secs = 1
        self.boom_initiaded = False
        #Mixer
        #pygame.mixer.init()
        #self.boom_sound = pygame.mixer.Sound("assets/music/SFX/dead_boom.wav")
        #self.boom_sound.set_volume(.1)

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
            #self.boom_sound.stop()
            self.boom_initiaded = False

        if not self.boom_initiaded:
            #self.boom_sound.play()
            self.boom_initiaded = True

        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
