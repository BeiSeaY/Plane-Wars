class Settings:
    # 所有设置的类
    def __init__(self):
        """初始化游戏的设置"""
        self.width = 1200
        self.height = 600
        self.by_color = (230, 230, 230)

        # 飞船的属性设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_heigth = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3  # 限制子弹的数量

        # 外星人设置
        self.alien_speed_factor = 1  # 移动的速度
        self.fleet_drop_speed = 10  #wxr向下移动的速度
        self.fleet_direction = 1  # 为1时向左移，-1向右移
