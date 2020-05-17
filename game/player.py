import pygame
from .constants import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)
        
        self.image= pygame.Surface( (40,40) )
        self.rect= self.image.get_rect()
        
        self.image.fill(AQUA)
        self.rect.left , self.rect.bottom= left, bottom
        self.pos_y= self.rect.bottom
        self.vel_y=0
        self.playing=True
        self.jumping=True
        
    def update_pos(self):
        self.vel_y+= GRAV
        self.pos_y+=self.vel_y + .5*GRAV
        
    def col_platform(self, platform):
        if pygame.sprite.collide_rect(self, platform):
            self.pos_y=platform.rect.top
            self.vel_y=0
            self.jumping=True
            
            
    def jump(self):
        if self.jumping:
            self.vel_y=-23
            self.jumping=False
        
    def collide_top(self, wall):
        return self.rect.colliderect(wall.rect_top)
       
   
    def surf(self, wall):
        self.pos_y=wall.rect.top
        self.vel_y=0
        self.jumping=True
        
    def collide_with(self, sprites):
        objects= pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]
        
    def update(self):
        if self.playing:
            self.update_pos()
            self.rect.bottom=self.pos_y

            
    def stop(self):
        self.playing=False
        
    
         