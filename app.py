import pygame, sys, const
from pygame import mixer
from clases.Button import Button
import title_screen, history,main_menu, user_screen, tutorial, boss_fight, game_over, option_screen

pygame.init()
pygame.display.set_caption("Alien Strike: Retribution Day")
pygame.display.set_icon(const.LOGO)
#user_screen.username()
#history.history()
#test.test()
option_screen.option_screen()
#tutorial.tutorial()
#boss_fight.boss_fight()
#LVL_3.lvl_3()
#game_over.game_over()
