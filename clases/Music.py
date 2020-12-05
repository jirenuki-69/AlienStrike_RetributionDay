import pygame, const

class Music():
    def __init__(self):
        self.music = pygame.mixer
        self.music.init()
        self.music.music.set_volume(self.get_volume())
        self.jump = "music/jump.mp3"
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

    def game_over(self):
        self.music.music.load("assets/music/GAME OVER MUSIC.mp3")
        self.music.music.play(-1)
        pass

    def options(self):
        self.music.music.load("assets/music/Smocking shibuya decks.mp3")
        self.music.music.play(-1)
        pass

    def boss(self):
        self.music.music.load("assets/music/boss/final_boss_theme.mp3")
        self.music.music.play(-1)
        pass

    def get_volume(self):
        with open ("volumen.txt") as archivo:
            for linea in archivo.readlines():
                return float(str(linea.split("-")[0]))

    def set_volume(self, new_volume):
        my_file = open("volumen.txt", "w")
        my_file.writelines(str(new_volume))

        my_file.close()

    def reset_volume(self):
        self.music.music.set_volume(self.get_volume())
