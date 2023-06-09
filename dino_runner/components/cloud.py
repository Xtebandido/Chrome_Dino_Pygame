import random

from pygame.sprite import Sprite
from  dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(700, 1000)
        self.y = random.randint(50,100)
        self.width = self.image.get_width()

    def update(self, game_speed):
        self.x -= game_speed - 10
        if self.x <- self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50,100)

    def draw(self,screen):
        screen.blit(self.image, (self.x,self.y))
        