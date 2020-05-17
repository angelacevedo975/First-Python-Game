import pygame
from .constants import *

class Coin(pygame.sprite.Sprite):
    
    def __init__(self , pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( (30,30) )
        self.rect= self.image.get_rect()
        
        self.image.fill( YELLOW )
        self.rect.x, self.rect.y = pos_x, pos_y
        
    def update(self):
        self.rect.x-=SPEED