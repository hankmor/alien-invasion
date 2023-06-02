import sys

import pygame


def check_events():
    """检查事件响应"""
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            # 退出游戏
            sys.exit()


def draw(settings, screen, ship):
    """绘制屏幕"""
    # 设置背景色
    screen.fill(settings.bg_color)
    # 重绘飞船
    ship.display()
    # 渲染游戏界面
    pygame.display.flip()
