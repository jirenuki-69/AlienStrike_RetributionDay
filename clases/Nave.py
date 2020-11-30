import pygame

class Nave():
    def __init__(self, position, movementSpeed, screenSize, img):
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
        self.screenSize = screenSize
        #Velocidad de movimiento del Personaje
        self.movementSpeed = movementSpeed
        #Detectar si el usuario está disparando
        self.ban = True
        #Qué respuesta dar a la clase principal
        self.response = 0
        #Disparo
        self.misil = pygame.image.load("assets/visual/gameplay_assets/disparo_prueba.png")
        self.misilimage = self.misil.subsurface(self.misil.get_clip())
        self.misilrect = self.misilimage.get_rect()

    def shoot(self):
        self.response = self.rect

    def update(self, direction):
        if direction == "left" and self.rect.x - self.movementSpeed > 0:

            self.rect.x -= self.movementSpeed

        elif direction == "right" and self.rect.x + self.movementSpeed < self.screenSize[0] - 50:

            self.rect.x += self.movementSpeed

    def event_manager(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_a]:
            self.update("left")
        if keys[pygame.K_d]:
            self.update("right")
        if mouse[0] or keys[pygame.K_SPACE]:
            self.ban = True
            self.shoot()
        else:
            self.ban = False
            self.response = 0

        return self.response
