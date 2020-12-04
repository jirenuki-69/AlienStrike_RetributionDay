import pygame
from clases.Kboom import Explosion

class Enemy():
    def __init__(self, position, movementSpeed, screenSize, screen, img):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load(img)
        self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
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
        #Detectar si el usuario está disparando
        self.ban = True
        #Qué respuesta dar a la clase principal
        self.response = 0
        #Disparo
        self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/alien1.png")
        self.misilbool = True
        self.misilimage = self.misil.subsurface(self.misil.get_clip())
        self.misilrect = self.misilimage.get_rect()
        self.health = 5

        #Explosion
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
        self.screen.blit(self.boom.image, (self.rect.x - 20, self.rect.y - 70))

    def get_frame(self):
        if self.misilbool:
            self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/alien1.png")
            self.misilbool = False
        else:
            self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/alien1.png")
            self.misilbool = True

    def shoot(self):
        self.response = self.rect

    def update(self, direction):
        if direction == "left" and self.rect.x - self.movementSpeed > -15:

            self.rect.x -= self.movementSpeed

        elif direction == "right" and self.rect.x + self.movementSpeed < self.screenSize[0] - self.rect.x * .15:

            self.rect.x += self.movementSpeed

    def event_manager(self, cont):
        if cont == 180:
            self.ban = True
            self.shoot()
        else:
            self.ban = False
            self.response = 0

        return self.response
