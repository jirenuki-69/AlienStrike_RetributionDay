import pygame, sys, const
from pygame import mixer
from clases.Button import Button
import title_screen, history,main_menu, user_screen, endgame_history, tutorial, boss_fight, game_over, option_screen, credits
import LVL_1, LVL_2, LVL_3
import intro_boss

pygame.init()
pygame.display.set_caption("Alien Strike: Retribution Day")
pygame.display.set_icon(const.LOGO)
intro_boss.intro_boss()
#LVL_1.lvl_1()
#LVL_2.lvl_2()
#LVL_3.lvl_3()
#boss_fight.boss_fight()
#title_screen.title_screen()
user_screen.username()
history.history()
#endgame_history.endgame_history()
#test.boss_fight()
#credits.credits()
#option_screen.option_screen()
#tutorial.tutorial()
#boss_fight.boss_fight()
#LVL_3.lvl_3()
#game_over.game_over()
