import pygame
import time

class Sound:
    def __init__(self):
        pygame.init()

        self.sound_click = pygame.mixer.Sound("/home/nesvera/Documents/urna-tedx-democracia/sound/click-1.mp3")
        self.sound_confirm = pygame.mixer.Sound("/home/nesvera/Documents/urna-tedx-democracia/sound/confirm-1.mp3")

    def play_click(self):
        self.sound_click.play()

    def play_confirm(self):
        self.sound_confirm.play()
