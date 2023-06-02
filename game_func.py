import sys

import pygame


def check_key_up(evt, ship):
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


def check_key_down(evt, ship):
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


def check_events(ship):
    """检查事件响应"""
    for evt in pygame.event.get():
        match evt.type:
            case pygame.QUIT:
                sys.exit()  # 退出游戏
            case pygame.KEYDOWN:
                check_key_up(evt, ship)
            case pygame.KEYUP:
                check_key_down(evt, ship)


def draw(settings, screen, ship):
    """绘制屏幕"""
    # 设置背景色
    screen.fill(settings.bg_color)
    # 重绘飞船
    ship.display()
    # 渲染游戏界面
    pygame.display.flip()
