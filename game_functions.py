import sys
import pygame
from game_project.bullet import Bullet
from game_project.alien import Alien


def check_events(ai_setting, screen, ship, bullets):
    """响应键盘和鼠标事件。每次按键都被注册为一个KEYDOWN 事件。
    检测到KEYDOWN事件时，需要检测按下的是否特定的建。"""

    for event in pygame.event.get():  # 检测用户鼠标和键盘事件
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # 检测到键盘按下事件
            check_keydown_events(event, ai_setting, screen, ship, bullets)

        elif event.type == pygame.KEYUP:  # 检测键盘按键弹起事件
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    """键盘响应按键"""

    if event.key == pygame.K_q:
        sys.exit()

    if event.key == pygame.K_RIGHT:  # 读取event.key的属性，向右移动飞船
        # ship.rect.centerx += 1
        ship.moving_rigth = True

    if event.key == pygame.K_UP:
        ship.moving_up = True

    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_DOWN:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)


def fire_bullet(ai_setting, screen, ship, bullets):
    # 创建一颗新子弹并将其加入到编组bullets中
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """键盘响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False

    if event.key == pygame.K_DOWN:
        ship.moving_down = False

    if event.key == pygame.K_SPACE:
        Bullet.bullet_up = False


def update_screen(ai_setting, screen, ship, aliens, bullets):
    screen.fill(ai_setting.by_color)  # 用背景色填充屏幕
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():  # bullets.sprites反回一个列表，其中包含编组bullets所有Sprite，遍历每个精灵
        bullet.draw_bullet()  # 在屏幕绘制每一颗子弹
    ship.blitme()
    aliens.draw(screen)  # 在屏幕上绘制编组中的每个外星人

    pygame.display.flip()  # 让最近重绘的屏幕可见


def update_bullets(aliens, bullets):
    bullets.update()
    # 更新子弹的位置，并删除以消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中了外星人，如果是这样，就删除相应的子弹和外星人
    # 遍历每个偏组的属性，两个实参True 告诉Pygame删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)


def get_number_alien_x(ai_setting, alien_width):
    """计算一行可容纳多少个外星人"""
    available_space_x = ai_setting.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 计算除空行外可容纳多少个外星人
    return number_aliens_x


def get_number_rows(ai_setting, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_setting.height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    # 创建一个外星人并放在当前行
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width  # wxr的宽度
    alien.x = alien_width + 2 * alien_width * alien_number  # 通过设置x坐标将其加入当前行，将每个wxr都往右推一个wxr的宽度
    alien.rect.x = alien.x  # 每个wxr占据的空间（包括其右边的空白区域）,在计算当前wxr在当前行的位置
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  # 计算屏幕可以存放多少行wxr
    aliens.add(alien)  # 将外星人添加到编组中


def create_fleet(ai_setting, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_setting, screen)  # 创建一个外星人
    number_alien_x = get_number_alien_x(ai_setting, alien.rect.width)  # 并计算每行可容纳多少个wxr
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):  # 创建wxr群
        for alien_number in range(number_alien_x):  # 创建第一行外星人
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_setting, aliens):
    """有wxr到达边缘时采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    """将wxr群下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def update_aliens(ai_setting, aliens):
    """更新wxr群中所有wxr的位置"""
    check_fleet_edges(ai_setting, aliens)
    aliens.update()  # 对偏组alines调用update方法，这将自动对每个wxr调用update
