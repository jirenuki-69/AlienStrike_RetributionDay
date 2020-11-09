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
        self.image_rect.x, self.image_rect.y = (screen_size[0] / 2 - self.size[0] / 2, self.size[1] * 0.1)
        self.screen_size = screen_size

    def load_new_image(self, image, text):
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x, self.image_rect.y = (self.screen_size[0] / 2 - self.size[0] / 2, self.size[1] * 0.1)
        self.text = text

    def show_scene(self):
        self.screen.blit(self.image, [self.image_rect.x, self.image_rect.y])

        text_wrapped = textwrap.wrap(self.text, 100)

        scene_text_list = []

        for i in range(len(text_wrapped) + 1):
            if i == len(text_wrapped):
                scene_text_list.append("")
            else:
                scene_text_list.append(text_wrapped[i])

        for i in range(len(scene_text_list)):
            scene_text = self.font.render(scene_text_list[i], True, self.text_color)
            scene_text_rect = scene_text.get_rect()
            scene_text_rect.x, scene_text_rect.y = (self.screen_size[0] * 0.05 , self.screen_size[1] * 0.8 + (50 * i))

            self.screen.blit(scene_text, scene_text_rect)
