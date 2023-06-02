import pygame.image


class Ship:
    """飞船管理类"""

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        # 加载飞船图片
        self.image = pygame.image.load("assets/images/ship.bmp")
        # 获取图片的矩形surface
        self.ship_rect = self.image.get_rect()
        # 获取界面的矩形
        self.screen_rect = screen.get_rect()

        # 移动方向
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        # 将飞船显示在界面的底部居中，注意pygame中(0,0)坐标为左上角，而不是中心位置
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom
        # center属性用于计算水平移动距离，ship_rect 只能存储整数值，因此需要用center来存储累加的小数
        self.center = float(self.ship_rect.centerx)  # 设置初始值
        self.bottom = float(self.ship_rect.bottom)  # 设置初始值

    def display(self):
        """在指定位置绘制飞船"""
        # 在ship_rect位置处绘制image
        self.screen.blit(self.image, self.ship_rect)

    def moving(self):
        if self.moving_up and self.ship_rect.top > self.screen_rect.top:
            self.bottom -= self.settings.speed
        elif self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.speed
        elif self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.center -= self.settings.speed
        elif self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.settings.speed
        # print(f'center: {self.center}')
        self.ship_rect.centerx = self.center
        self.ship_rect.bottom = self.bottom
