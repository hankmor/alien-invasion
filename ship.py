import pygame.image


class Ship:
    """飞船管理类"""

    def __init__(self, screen):
        self.screen = screen
        # 加载飞船图片
        self.image = pygame.image.load("assets/images/ship.bmp")
        # 获取图片的矩形surface
        self.ship_rect = self.image.get_rect()
        # 获取界面的矩形
        self.screen_rect = screen.get_rect()

        # 移动方向
        self.moving_left = False
        self.moving_right = False
        # 将飞船显示在界面的底部居中，注意pygame中(0,0)坐标为左上角，而不是中心位置
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def display(self):
        """在指定位置绘制飞船"""
        # 在ship_rect位置处绘制image
        self.screen.blit(self.image, self.ship_rect)

    def moving(self):
        if self.moving_left:
            self.ship_rect.centerx -= 1
        elif self.moving_right:
            self.ship_rect.centerx += 1
