import sys

import pygame

from bullet import Bullet


def check_key_down(evt, settings, screen, ship, bullets):
    """监测按键按下事件"""
    match evt.key:
        case pygame.K_UP:  # 按下上方向键
            ship.moving_up = True
        case pygame.K_DOWN:  # 按下下方向键
            ship.moving_down = True
        case pygame.K_LEFT:  # 按下左方向键
            ship.moving_left = True
        case pygame.K_RIGHT:  # 按下右方向键
            ship.moving_right = True
        case pygame.K_SPACE:  # 按下空格键
            create_bullet(settings, screen, ship, bullets)


def check_key_up(evt, ship):
    """监测按键弹起事件"""
    match evt.key:
        case pygame.K_UP:  # 弹起上方向键
            ship.moving_up = False
        case pygame.K_DOWN:  # 弹起下方向键
            ship.moving_down = False
        case pygame.K_LEFT:  # 弹起左方向键
            ship.moving_left = False
        case pygame.K_RIGHT:  # 弹起右方向键
            ship.moving_right = False


def check_events(settings, screen, ship, bullets):
    """检查事件响应"""
    for evt in pygame.event.get():
        match evt.type:
            case pygame.QUIT:
                sys.exit()  # 退出游戏
            case pygame.KEYDOWN:
                check_key_down(evt, settings, screen, ship, bullets)
            case pygame.KEYUP:
                check_key_up(evt, ship)


def draw(settings, screen, ship, bullets):
    """绘制屏幕"""
    # 设置背景色
    screen.fill(settings.bg_color)
    # 重绘子弹
    for bullet in bullets:
        bullet.draw()
    # 重绘飞船
    ship.display()
    # 渲染游戏界面
    pygame.display.flip()


def create_bullet(settings, screen, ship, bullets):
    # 创建一颗子弹并加入到组
    if len(bullets) < settings.bullet_limit:
        bullets.add(Bullet(settings, screen, ship))


def update_bullet(bullets):
    # 调用update方法检测子弹移动，组上调用方法会在其每一个元素中都会调用该方法
    bullets.update()
    # 检测子弹是否已经消失，消失后从组内移除
    for bullet in bullets:  # TODO 循环时先拷贝一份？再循环中拷贝代价也挺高？
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(self.bullets))
