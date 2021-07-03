import os
from pygame import mixer

class Sound:
    def __init__(self):
        self.ball_sound = mixer.Sound(os.path.join("assets", "quick_jump.wav"))

    def volume_control(self, value):
        self.ball_sound.set_volume(value)
        mixer.music.set_volume(value)

    def play_background_music(self):
        mixer.music.load(os.path.join("assets", "rise-and-shine.mp3"))
        mixer.music.play(-1)

    def stop_background_music(self):
        mixer.music.stop()
