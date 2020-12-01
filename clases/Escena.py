import pygame, textwrap

class Escena():
    def __init__(self, image, text, text_color, font, screen, screen_size, size):
        self.image = pygame.image.load(image).convert()
        self.text = text
        self.text_color = text_color
        self.font = font
        self.screen = screen
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect()
        self.screen_size = screen_size
        self.next_button = pygame.image.load("assets/visual/history_scenes/buttons/NEXT_button.png").convert()
        self.skip_button = pygame.image.load("assets/visual/history_scenes/buttons/SKIP_button.png").convert()
        self.next_button = pygame.transform.scale(self.next_button, (70, 40))
        self.skip_button = pygame.transform.scale(self.skip_button, (70, 40))
        self.next_button_rect = self.next_button.get_rect()
        self.skip_button_rect = self.skip_button.get_rect()
        self.next_button_rect.x, self.next_button_rect.y, = (self.screen_size[0] * 0.75, self.screen_size[1] * 0.9)
        self.skip_button_rect.x, self.skip_button_rect.y, = (self.screen_size[0] * 0.82, self.screen_size[1] * 0.9)

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

    def show_scene(self):
        self.screen.blit(self.image, [self.image_rect.x, self.image_rect.y])
        self.screen.blit(self.next_button, [self.next_button_rect.x, self.next_button_rect.y])
        self.screen.blit(self.skip_button, [self.skip_button_rect.x, self.skip_button_rect.y])

        text_wrapped = textwrap.wrap(self.text, 85)

        scene_text_list = []

        for i in range(len(text_wrapped) + 1):
            if i == len(text_wrapped):
                scene_text_list.append("")
            else:
                scene_text_list.append(text_wrapped[i])

        for i in range(len(scene_text_list)):
            scene_text = self.font.render(scene_text_list[i], True, self.text_color)
            scene_text_rect = scene_text.get_rect()
            scene_text_rect.x, scene_text_rect.y = (self.screen_size[0] * 0.1 , self.screen_size[1] * 0.78 + (50 * i))

            self.screen.blit(scene_text, scene_text_rect)
