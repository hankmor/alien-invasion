import sys

import pygame


def check_events(ship):
    """检查事件响应"""
    for evt in pygame.event.get():
        match evt.type:
            case pygame.QUIT:
                sys.exit()  # 退出游戏
            case pygame.KEYDOWN:
                match evt.key:
                    case pygame.K_LEFT:  # 按下左方向键
                        ship.moving_left = True
                    case pygame.K_RIGHT:  # 按下右方向键
                        ship.moving_right = True
            case pygame.KEYUP:
                match evt.key:
                    case pygame.K_LEFT:  # 按下左方向键
                        ship.moving_left = False
                    case pygame.K_RIGHT:  # 按下右方向键
                        ship.moving_right = False


def draw(settings, screen, ship):
    """绘制屏幕"""
    # 设置背景色
    screen.fill(settings.bg_color)
    # 重绘飞船
    ship.display()
    # 渲染游戏界面
    pygame.display.flip()
