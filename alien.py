import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_setting, screen):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.ai_setting = ai_setting
        self.screen = screen

        # 加载外星人，并设置rect属性
        self.image = pygame.image.load("images/alien.bmp")  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片的矩形属性  （rect只存取值的整数部分）

        # 将每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果wxr处于屏幕边缘反悔True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """让外星人向左或右移动"""
        self.x += (self.ai_setting.alien_speed_factor *
                   self.ai_setting.fleet_direction)
        self.rect.x = self.x  # 更新外星人的rect位置

    def blitme(self):
        """在指定的位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
