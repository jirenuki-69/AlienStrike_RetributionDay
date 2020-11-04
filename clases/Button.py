import pygame

class Button():
    def __init__(self, screen, pos, width, height, primaryColor, secondaryColor, text, font, textColor):
        self.screen = screen
        self.font = font
        self.text = text
        self.textColor = textColor
        self.pos = pos
        self.width = width
        self.height = height
        self.color, self.primaryColor = primaryColor, primaryColor
        self.secondaryColor = secondaryColor
        self.rect = pygame.draw.rect(self.screen, self.color, ( self.pos[0], self.pos[1], self.width, self.height ))

    def init_button(self):
        self.buttonText = self.font.render(self.text, True, self.textColor)
        self.buttonTextRect = self.buttonText.get_rect()
        self.rect = pygame.draw.rect(self.screen, self.color, ( self.pos[0], self.pos[1], self.width, self.height ))
        self.buttonTextRect.center = self.rect.center
        self.screen.blit( self.buttonText, self.buttonTextRect )

    def is_hovered(self, x, y):
        if self.rect.collidepoint(x, y):
            if self.color == self.primaryColor:
                self.color = self.secondaryColor
        else:
            self.color = self.primaryColor

    def is_pressed(self, event, x, y):
        if self.rect.collidepoint(x, y):
            return True

        return False
