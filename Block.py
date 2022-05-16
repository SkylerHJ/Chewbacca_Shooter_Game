import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = (0, 0, 0)
        self.image = pygame.Surface([30, 30])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, win):
        pygame.draw.rect(self.image, self.color, [self.rect.x, self.rect.y, 30, 30])

    
