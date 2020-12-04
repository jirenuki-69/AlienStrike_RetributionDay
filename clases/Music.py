import pygame, const

class Music():
    def __init__(self):
        self.music = pygame.mixer
        self.music.init()
        self.music.music.set_volume(const.MUSIC_VOLUME)
        self.jump = "music/jump.mp3"
        pass

    def saltar(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.jump)
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(.5)
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
