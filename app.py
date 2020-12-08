import pygame, sys, const
from pygame import mixer
import history, user_screen

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Alien Strike: Retribution Day")
pygame.display.set_icon(const.LOGO)

user_screen.username()
history.history()
