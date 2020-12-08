import xbox360_controller, pygame, const

class Cursor():
    def __init__(self, position, screen):
        self.x, self.y = position
        self.screen = screen
        self.movementSpeed = 12
        self.sheet = pygame.image.load("assets/visual/cursor.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 31, 31))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.states = {
            0: (0, 0, 31, 31), 1: (31, 0, 31, 31),
            2: (0, 31, 31, 31), 3: (31, 31, 31, 31),
            4: (0, 62, 31, 31), 5: (31, 62, 31, 31)
        }
        self.frame = 0
        self.cont = 0

    def update(self):
        if self.cont >= 60:
            self.cont = 0

        self.screen.blit(self.image, (self.x, self.y))

        self.cont += 1
        self.clip(self.states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def movement(self, x, y):
        if self.x + int(x * self.movementSpeed) < 1160 and self.x + int(x * self.movementSpeed) > 0:
            self.x += int(x * self.movementSpeed)
        if self.y + int(y * self.movementSpeed) < 760 and self.y + int(y * self.movementSpeed) > 0:
            self.y += int(y * self.movementSpeed)

    def mouse_movement(self, x, y):
        self.x, self.y = x, y

    def get_frame(self, frame_set):
        if self.cont % 8 * 3 == 0:
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
