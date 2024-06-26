import pygame
from pygame import mixer

class Sounds:
    def __init__(self):
        mixer.init()
        self.ss = {
            'click': mixer.Sound("runnerV3/assets/clickBtn.wav"),
            'jump': mixer.Sound("runnerV3/assets/jump.wav"),
            'death': mixer.Sound("runnerV3/assets/Randomize76.wav"),
        }

    def playMusic(self):
        mixer.music.load("assets/music.mp3")
        mixer.music.play(-1)

    def play(self, key):
        pygame.mixer.Sound.play(self.ss[key])


sounds = Sounds()
