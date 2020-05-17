import pygame
from .constants import *

class Platform(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface( ( WIDTH, 40) )
        self.rect= self.image.get_rect()
        self.rect.y=HEIGHT-40
        self.image.fill(PURPLE)