import pygame
from .constants import *

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, left, bottom, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface( (width, height) )
        self.image.fill( GREEN )
        
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.bottom=bottom
        self.rect_top= pygame.Rect( (self.rect.x, self.rect.y, self.rect.width, 1) )
        
        self.vel_y=SPEED
        
        
    def stop(self):
        self.vel_y=0
        
    def update(self):
        self.rect.left -= self.vel_y
        self.rect_top.x =self.rect.x
        