import os
from pygame import mixer

class Sound:
    def __init__(self):
        self.ball_sound = mixer.Sound(os.path.join("assets", "quick_jump.wav"))

    def volume_control(self, value):
        self.ball_sound.set_volume(value)