import pygame
from pygame.locals import *
from Laser import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load('chewbacca.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, win):
        win.blit(self.img,(self.rect.x,self.rect.y))

    def move_down(self):
        self.rect.y +=10
    
    def move_up(self):
        self.rect.y -=10

    def get_x(self):
        return self.rect.x
    
    def get_y(self):
        return self.rect.y
