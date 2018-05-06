#!/usr/bin/env python
# coding=utf-8



class GameStats():
    '''跟踪游戏统计信息'''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
