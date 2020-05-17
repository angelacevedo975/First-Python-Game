import pygame
from .constants import *
import sys
from .platform import Platform
from .player import Player
from .wall import Wall
import random
from .coin import Coin
from pygame.sprite import Group


class Game:
    
    def __init__(self):
        pygame.init()
        
        self.surface= pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption( NAME )
        self.running=True
        self.clock=pygame.time.Clock()
        self.playing=False
        #self.font= pygame.font.match_font(FONT)
        
        
    def start(self):
        self.new()
    
    
    def new(self):
        while(not self.playing):
            self.menu_interface()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                self.playing=True
            
            pygame.display.update()
        
        
        
        self.num_coins=0
        self.level=0
        self.generateElements()
        self.run()
        
    def generateElements(self):
        self.platform= Platform()
        self.player= Player(100, self.platform.rect.top -300)
        
        
        self.sprites= pygame.sprite.Group()
        
        self.walls= pygame.sprite.Group()
        self.generate_walls()
        
        self.coins= pygame.sprite.Group()
        self.generate_coins()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        #self.sprites.add(self.walls)
        #self.sprites.add(self.coins)
        
        
    def generate_walls(self):
        if len(self.walls) <=0:
            
            last_pos=WIDTH
            for w in range(10):
                wall= Wall(
                    random.randrange(last_pos+300, last_pos+500) , self.platform.rect.top,
                    50, random.randrange(100, 150)
                    )
                self.walls.add(wall)
                self.sprites.add(wall)
                last_pos=wall.rect.right
                
            print("walls",len(self.walls))
            self.level+=1
            
    def generate_coins(self):
        if len(self.coins) <=0:
            last_pos=WIDTH
            for c in range(15):
                coin=Coin(
                    random.randrange(last_pos, last_pos+200),
                    random.randrange( HEIGHT-400, HEIGHT-100)
                    )
                self.coins.add(coin)
                self.sprites.add(coin)
                last_pos=coin.rect.x+200
            print("coins", len(self.coins))
                
                
    def draw_text(self, mensaje, color, size, pos_x, pos_y):
        font =pygame.font.Font(FONT, size)
        text=font.render(mensaje, True, color)
        rect= text.get_rect()
        rect.midtop=(pos_x, pos_y)
        self.surface.blit(text, rect)
        
    def menu_interface(self):
        self.surface.fill(RED)
        self.draw_text("Python Game", WHITE,48 , WIDTH//2, HEIGHT//2-20)
        self.draw_text("Presiona scape para iniciar", WHITE, 28, WIDTH//2, HEIGHT//2+50)
        
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.event()
            self.draw()
            self.update()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
                pygame.quit()
                sys.exit()
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.player.jump()
    
    def draw(self):
        if self.playing:
            self.surface.fill(BLACK)
            self.sprites.draw(self.surface)
            self.draw_text("Score: {}".format(self.num_coins), WHITE, 36, WIDTH//2, 30)
            self.draw_text("Level: {}".format(self.level), WHITE, 26, 50, 30)
        
            
    
    def update(self):
        if self.playing:  
            pygame.display.flip()
            
            wall=self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_top(wall):
                    self.player.surf(wall)
                else:
                    self.stop()
                    self.playing=False
            
            coin=self.player.collide_with(self.coins)
            if coin:
                coin.kill()
                self.num_coins+=1
                print(self.num_coins)
            
            self.sprites.update()
            
            self.player.col_platform(self.platform)
            
            self.update_elements(self.walls, self.coins)
            
            self.generate_walls()
            self.generate_coins()
        
    
    def update_elements(self, elements, coins):
        for e in elements:
            if e.rect.right<0:
                e.kill()
        for c in coins:
            if c.rect.right<0:
                c.kill()
        
            
    def stop(self):
        self.stop_elements(self.walls)
        self.player.stop()
        self.playing=False
        self.new()
        
    def stop_elements(self, elements):
        for e in elements:
            e.stop()