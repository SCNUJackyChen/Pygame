#!/usr/bin/env python
# coding=utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group 
from game_stats import GameStats
import game_functions as gf



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个外星人 
    alien = Alien(ai_settings, screen)
    # 创建外星人编组 
    aliens = Group()
    # 创建外星人群 
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    # 创建一个游戏信息存储示例
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
     
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()
