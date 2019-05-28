import pygame


class Ship:

    def __init__(self, ai_setting, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen  # 屏幕属性
        self.ai_settings = ai_setting  # 获取飞船的速度设置

        self.image = pygame.image.load('images/ship.bmp')  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片的矩形属性  （rect只存取值的整数部分）
        self.screen_rect = screen.get_rect()  # 获取屏幕属性矩形属性

        # 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。
        # 在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。
        # 将飞船放入屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # x坐标
        self.rect.bottom = self.screen_rect.bottom  # y坐标

        # 在飞船的属性center中存储最小值
        self.center = float(self.rect.centerx)
        self.botton = float(self.rect.bottom)

        # 移动标志
        self.moving_rigth = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 根据recr指定位置绘制飞船

    def update(self):
        """根据移动的标志调整飞船的位置"""
        if self.moving_rigth and self.rect.right < self.screen_rect.right:  # 更新飞船center值不是rect
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.botton -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.botton += self.ai_settings.ship_speed_factor

        # 更具self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.botton
