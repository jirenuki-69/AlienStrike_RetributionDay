import pygame
from pygame import mixer
from clases.MiniKboom import Explosion
from clases.Sound import Sound

class Nave():
    def __init__(self, position, movementSpeed, screenSize, screen, img):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load(img)
        self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        #Se genera el surface para mostrar algo en la pantalla
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #Se representa la imagen y moverla
        self.rect = self.image.get_rect()
        #Paso el rect a la posicion del personaje
        self.rect.center = (position[0] - 20, position[1])
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
        self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/1.png")
        self.misilbool = True
        self.misilimage = self.misil.subsurface(self.misil.get_clip())
        self.misilrect = self.misilimage.get_rect()
        self.exploded = False

        self.sound = Sound()


        self.boom = Explosion(
            (int(position[0] * 0.50), int(position[1] * .5)),
            screenSize
        )
        self.exploded = False

    def update_explode_position(self):
        self.boom.rect.x, self.boom.rect.y = (self.rect.x, self.rect.y)

    def explode(self):
        self.sound.player_explosion()
        self.update_explode_position()
        self.boom.update()
        self.screen.blit(self.boom.image, (self.rect.x + 20, self.rect.y + 15))

    def get_frame(self):
        if self.misilbool:
            self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/1.png")
            self.misilbool = False
        else:
            self.misil = pygame.image.load("assets/visual/gameplay_assets/laser/propersize/2.png")
            self.misilbool = True

    def shoot(self, cont):
        if cont == 0:
            self.sound.player_shoot()
        self.response = self.rect

    def update(self, direction):
        if direction == "left" and self.rect.x - self.movementSpeed > -15:

            self.rect.x -= self.movementSpeed

        elif direction == "right" and self.rect.x + self.movementSpeed < self.screenSize[0] - self.rect.x * .15:

            self.rect.x += self.movementSpeed

    def event_manager(self, cont):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_a]:
            self.update("left")
        if keys[pygame.K_d]:
            self.update("right")
        if mouse[0] or keys[pygame.K_SPACE]:
            self.ban = True
            self.shoot(cont)
        else:
            self.ban = False
            self.response = 0

        return self.response
