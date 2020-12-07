import pygame, const

class Music():
    def __init__(self):
        self.music = pygame.mixer
        self.music.init()
        self.music.music.set_volume(self.get_volume())
        pass

    def stop(self):
        self.music.music.stop()
        pass

    def chilling_grilling(self):
        self.music.music.load("assets/music/menu_music/Chilling and Grilling.mp3")
        self.music.music.play(-1)
        pass

    def title_screen(self):
        self.music.music.load("assets/music/Alien Soldier - Title Theme(sugiero como musica del titulo).mp3")
        self.music.music.play(-1)
        pass

    def history_music(self):
        self.music.music.load("assets/music/Alien Soldier - Sidelimits.mp3")
        self.music.music.play(-1)
        pass

    def tutorial(self):
        self.music.music.load("assets/music/special_tracks/teachmenow.mp3")
        self.music.music.play(-1)
        pass

    def intro_level(self):
        self.music.music.load("assets/music/special_tracks/Alien Soldier - Slap-Up.mp3")
        self.music.music.play(-1)
        pass

    def game_over(self):
        self.music.music.load("assets/music/GAME OVER MUSIC.mp3")
        self.music.music.play(-1)
        pass

    def options(self):
        self.music.music.load("assets/music/Smocking shibuya decks.mp3")
        self.music.music.play(-1)
        pass

    def splash_screen(self):
        self.music.music.load("assets/music/special_tracks/Star Fox 2 Soundtrack Continue (1080p).mp3")
        self.music.music.play(-1)
        pass

    def lvl_1(self):
        self.music.music.load("assets/music/Alien Soldier - Soltype.mp3")
        self.music.music.play(-1)
        pass

    def lvl_2(self):
        self.music.music.load("assets/music/M.U.S.H.A. - 03 - Galvanic Gear.mp3")
        self.music.music.play(-1)
        pass

    def lvl_3(self):
        self.music.music.load("assets/music/Alien Soldier - Runner AD2025.mp3")
        self.music.music.play(-1)
        pass

    def boss(self):
        self.music.music.load("assets/music/boss/final_boss_theme.mp3")
        self.music.music.play(-1)
        pass

    def endgame(self):
        self.music.music.load("assets/music/special_tracks/Maria_Ending.mp3")
        self.music.music.play(-1)
        pass

    def credits(self):
        self.music.music.load("assets/music/special_tracks/creditos.mp3")
        self.music.music.play(-1)
        pass

    def get_volume(self):
        with open ("volumen.txt") as archivo:
            for linea in archivo.readlines():
                return float(str(linea.split("-")[0]))
        pass

    def set_volume(self, new_volume):
        my_file = open("volumen.txt", "w")
        my_file.writelines(str(new_volume))

        my_file.close()
        pass

    def reset_volume(self):
        self.music.music.set_volume(self.get_volume())
        pass
