from typing import Any

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""

    def __init__(self, settings, screen, ship):
        # 调用父类构造器
        super(Bullet, self).__init__()
        self.settings = settings
        self.screen = screen
        # 在(0, 0)处创建子弹，并更新位置
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.ship_rect.centerx  # 居中
        self.rect.top = ship.ship_rect.top  # 位置与飞船的位置重合，看起来像从飞船中发射出来的
        self.y = float(self.rect.y)  # 初始位置，后续可移动

    def update(self, *args: Any, **kwargs: Any) -> None:
        """重载方法，更新子弹的位置"""
        super().update(*args, **kwargs)
        self.y -= self.settings.speed  # 向上移动
        self.rect.y = self.y

    def draw(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
