import pygame
from game_project.Setting import Settings
from game_project.ship import Ship
from game_project.game_functions import check_events, update_screen, update_bullets, create_fleet, update_aliens
from pygame.sprite import Group


def run_game():

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_setting, screen)  # 绘制一艘飞船
    bullets = Group()  # 创建一个用于存储子弹的编组
    aliens = Group()

    # 创建外星人群
    create_fleet(ai_setting, screen, ship, aliens)

    while True:  # 游戏的主循环
        check_events(ai_setting, screen, ship, bullets)  # 检测玩家键盘事件
        ship.update()  # 调整飞船的位置
        update_bullets(aliens, bullets)  # 删除未消失的子弹
        update_aliens(ai_setting, aliens)  # 更新wxr的位置
        update_screen(ai_setting, screen, ship, aliens, bullets)  # 更新屏幕渲染


run_game()
