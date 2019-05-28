import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射子弹管理的类"""

    def __init__(self, ai_setting, screen, ship):
        """建一在飞船所处的位置创个子弹对象"""
        super().__init__()  # 通过使用Sprite，可将游戏中相关的元素编组，进而同时操作编组的所有元素
        self.screnn = screen

        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,  # 使用Rect获取子弹的矩形属性
                                ai_setting.bullet_heigth)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

        # 子弹移动的标记
        # self.bullet_up = False

    def update(self):
        """向上移动子弹"""
        # if self.bullet_up:
        self.y -= self.speed_factor
        self.rect.y = self.y  # 更新子弹的位置

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screnn, self.color, self.rect)
