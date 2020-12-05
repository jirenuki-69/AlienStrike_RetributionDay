import pygame, sys, const
from pygame import mixer
from clases.Button import Button
import title_screen, history,main_menu, user_screen, tutorial, boss_fight, game_over, option_screen, credits

pygame.init()
pygame.display.set_caption("Alien Strike: Retribution Day")
pygame.display.set_icon(const.LOGO)
#title_screen.title_screen()
user_screen.username()
history.history()
#test.boss_fight()
#credits.credits()
#option_screen.option_screen()
#tutorial.tutorial()
#boss_fight.boss_fight()
#LVL_3.lvl_3()
#game_over.game_over()
