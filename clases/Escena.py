import pygame, textwrap

class Escena():
    def __init__(self, image, text, text_color, font, screen, screen_size, size, wrap_criteria = 85, line_height = 50):
        self.image = pygame.image.load(image).convert()
        self.text = text
        self.text_color = text_color
        self.font = font
        self.screen = screen
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect()
        self.screen_size = screen_size
        self.wrap_criteria = wrap_criteria
        self.line_height = line_height
        self.next_button = pygame.image.load("assets/visual/history_scenes/buttons/NEXT_button.png").convert()
        self.skip_button = pygame.image.load("assets/visual/history_scenes/buttons/SKIP_button.png").convert()
        self.next_button = pygame.transform.scale(self.next_button, (70, 40))
        self.skip_button = pygame.transform.scale(self.skip_button, (70, 40))
        self.next_button_rect = self.next_button.get_rect()
        self.skip_button_rect = self.skip_button.get_rect()
        self.next_button_rect.x, self.next_button_rect.y, = (self.screen_size[0] * 0.75, self.screen_size[1] * 0.9)
        self.skip_button_rect.x, self.skip_button_rect.y, = (self.screen_size[0] * 0.82, self.screen_size[1] * 0.9)
        self.enter_image = pygame.image.load("assets/visual/history_scenes/endgame/enter_key.png")
        self.enter_image = pygame.transform.scale(self.enter_image, (70, 40))
        self.enter_image_rect = self.enter_image.get_rect()
        self.enter_image_rect.x, self.enter_image_rect.y = (self.screen_size[0] * 0.75, self.screen_size[1] * 0.9)
        self.is_last_scene = False
        self.cont = 0

    def next_pressed(self, x, y):
        if self.next_button_rect.collidepoint(x, y):
            print("Siguiente")
            return True
        return False

    def skip_pressed(self, x, y):
        if self.skip_button_rect.collidepoint(x, y):
            print("Siguiente")
            return True
        return False

    def load_new_image(self, image, text):
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect()
        self.text = text

    def last_scene(self):
        self.is_last_scene = True
        self.next_button_rect.x, self.next_button_rect.y = (2000, 300)
        self.skip_button_rect.x, self.skip_button_rect.y = (2000, 300)

    def show_scene(self):
        if self.cont > 60 * 1:
            self.cont = 0

        self.cont += 1
        self.screen.blit(self.image, [self.image_rect.x, self.image_rect.y])
        self.screen.blit(self.next_button, [self.next_button_rect.x, self.next_button_rect.y])
        self.screen.blit(self.skip_button, [self.skip_button_rect.x, self.skip_button_rect.y])

        if self.is_last_scene:
            if self.cont % 25 * 1 >= 1:
                self.screen.blit(self.enter_image, [self.enter_image_rect.x, self.enter_image_rect.y])

        text_wrapped = textwrap.wrap(self.text, self.wrap_criteria)

        scene_text_list = []

        for i in range(len(text_wrapped) + 1):
            if i == len(text_wrapped):
                scene_text_list.append("")
            else:
                scene_text_list.append(text_wrapped[i])

        for i in range(len(scene_text_list)):
            scene_text = self.font.render(scene_text_list[i], True, self.text_color)
            scene_text_rect = scene_text.get_rect()
            scene_text_rect.x, scene_text_rect.y = (self.screen_size[0] * 0.1 , self.screen_size[1] * 0.78 + (self.line_height * i))

            self.screen.blit(scene_text, scene_text_rect)
