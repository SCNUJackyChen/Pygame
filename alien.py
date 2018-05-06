#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''单个外星人的类'''

    def __init__(self, ai_settings, screen): 
        '''初始化外星人并设置初始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings 

        '''加载外星人图片'''
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        '''每个外星人最初在左上角'''
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        '''存储外星人的精确位置'''
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置控制外星人'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''向右移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

