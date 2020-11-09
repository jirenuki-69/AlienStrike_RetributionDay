import pygame, textwrap, const

class Texto():
    def __init__(self, text, pos, font, screen, wrap_criteria):
        self.text = text
        self.pos = pos
        self.font = font
        self.screen = screen
        self.wrap_criteria = wrap_criteria

    def show_text(self):
        if self.wrap_criteria == None:
            texto = self.font.render(self.text, True, const.BLACK)
            texto_rect = texto.get_rect()
            texto_rect.x, texto_rect.y = self.pos
            self.text_rect = texto_rect
            self.screen.blit(texto, texto_rect)
        else:
            text_wrapped = textwrap.wrap(self.text, self.wrap_criteria)
            text_list = []

            for i in range(len(text_wrapped) + 1):
                if i == len(text_wrapped):
                    text_list.append("")
                else:
                    text_list.append(text_wrapped[i])

            for i in range(len(text_list)):
                texto = self.font.render(text_list[i], True, const.BLACK)
                texto_rect = texto.get_rect()
                texto_rect.x, texto_rect.y = (self.pos[0], self.pos[1] + (30 * i))
                self.text_rect = texto_rect
                self.screen.blit(texto, texto_rect)
