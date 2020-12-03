import pygame
from clases.MiniKboom import Explosion

class MiniEnemy():
    def __init__(self, position, movementSpeed, screenSize, screen, img):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load(img)
        #self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        #Se genera el surface para mostrar algo en la pantalla
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #Se representa la imagen y moverla
        self.rect = self.image.get_rect()
        #Paso el rect a la posicion del personaje
        self.rect.center = position
        #En qué superficie se encuentra
        self.screen = screen
        self.screenSize = screenSize
        #Velocidad de movimiento del Personaje
        self.movementSpeed = movementSpeed
        self.time = 5
        self.alive = True
        self.damageShield = False
        self.damageNave = False

        self.cont = 0
        self.boom = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.exploded = False

    def update_explode_position(self):
        self.boom.rect.x, self.boom.rect.y = (self.rect.x, self.rect.y)

    def explode(self):
        self.update_explode_position()
        self.boom.update()
        self.screen.blit(self.boom.image, (self.rect.x - 20, self.rect.y - 20))

    def move(self):
        self.cont += 1
        if self.cont % (6 * self.movementSpeed) == 0:
            self.rect.y += 5

        if self.rect.y > self.screenSize[1]:
            self.alive = False
