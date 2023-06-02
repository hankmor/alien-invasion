import pygame
from pygame.sprite import Group
import game_func as gf
from settings import Settings
from ship import Ship


class AlienInvasion:
    """游戏主类，管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏，创建资源"""

        # 创建设置类实例
        self.settings = Settings()
        # 初始化pygame
        pygame.init()
        # 设置界面宽高
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        # 显示内容
        pygame.display.set_caption(self.settings.caption + " - " + self.settings.version)
        # 创建飞船实例
        self.ship = Ship(self.settings, self.screen)
        # 创建子弹编组，可以同时操作组内的元素
        self.bullets = Group()

    def start(self):
        """启动游戏"""

        # 循环渲染屏幕，每一帧都会在循环中渲染到界面
        while True:
            # 监听键盘和鼠标事件
            gf.check_events(self.settings, self.screen, self.ship, self.bullets)
            # 检测飞船移动
            self.ship.moving()
            # 更新子弹
            gf.update_bullet(self.bullets)
            # 绘制屏幕
            gf.draw(self.settings, self.screen, self.ship, self.bullets)


if __name__ == '__main__':
    # 创建启动类
    ai = AlienInvasion()
    # 启动游戏
    ai.start()
