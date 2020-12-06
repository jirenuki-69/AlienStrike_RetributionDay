import pygame, sys, const
from pygame import mixer
from clases.Button import Button
from clases.Shield import Escudo
import title_screen, history,main_menu, user_screen, endgame_history, tutorial, boss_fight, game_over, option_screen, credits
import LVL_1, LVL_2, LVL_3
import intro_boss, boss_end_scene

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Alien Strike: Retribution Day")
pygame.display.set_icon(const.LOGO)

screen = pygame.display.set_mode((1200, 800))
shields = []

vidas = 5
shield1 = Escudo(
    (int(1200 * .20), int(800 * .75)),
    (1200, 800),
    screen
)
shield2 = Escudo(
    (int(1200 * .5), int(800 * .75)),
    (1200, 800),
    screen
)
shield3 = Escudo(
    (int(1200 * .80), int(800 * .75)),
    (1200, 800),
    screen
)

shields.append(shield1)
shields.append(shield2)
shields.append(shield3)


LVL_2.lvl_2("hard", shields, vidas)
#intro_boss.intro_boss()
#endgame_history.endgame_history()
#LVL_1.lvl_1()
#LVL_2.lvl_2()
#LVL_3.lvl_3()
#boss_fight.boss_fight()
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
