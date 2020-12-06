import pygame, const

class Sound():
    def __init__(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/player_shoot.wav")

    def player_shoot(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/player_shoot.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def alien_shoot(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/alien_shoot.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def boss_laser(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/master_laser_super_ray.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def alien_explosion(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/dead_boom.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def player_explosion(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/dead_boom.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def boss_explosion(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/boss_explosion.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def get_ready(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/get_ready.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def dialogue_change(self):
        self.sound = pygame.mixer.Sound("assets/music/SFX/dialogue_change.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def get_SFX_volume(self):
        with open ("SFX.txt") as archivo:
            for linea in archivo.readlines():
                return float(str(linea.split("-")[0]))
        pass

    def set_SFX_volume(self, new_volume):
        my_file = open("SFX.txt", "w")
        my_file.writelines(str(new_volume))

        my_file.close()

        self.sound = pygame.mixer.Sound("assets/music/SFX/player_shoot.wav")
        self.sound.set_volume(self.get_SFX_volume())
        self.sound.play()
        pass

    def stop(self):
        self.sound.stop()
