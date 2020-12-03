import pygame

class Escudo():
    def __init__(self, position, screenSize, screen):
        #Cargo la imagen en memoria
        self.sheet = pygame.image.load("assets/visual/escudos/ESCUDO_fullhp.png")
        self.sheet = pygame.transform.scale(self.sheet, (int(screenSize[0] * 0.15), int(screenSize[1] * 0.15)))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #Se genera el surface para mostrar algo en la pantalla
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #Se representa la imagen y moverla
        self.rect = self.image.get_rect()
        #Paso el rect a la posicion del personaje
        self.rect.center = position
        #En qué superficie se encuentra
        self.screenSize = screenSize
        self.change = False
        self.print = True

    def update(self, damaged):
        if damaged and not self.change:
            self.sheet = pygame.image.load("assets/visual/escudos/ESCUDO_halfhp.png")
            self.sheet = pygame.transform.scale(self.sheet, (int(self.screenSize[0] * 0.15), int(self.screenSize[1] * 0.15)))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            #self.rect = self.image.get_rect()
            self.change = True
    def destroy(self):
        self.print = False
        self.image.fill((0, 0, 0, 0))
