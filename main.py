import sys
import pygame

from settings import Settings


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

    def start(self):
        """启动游戏"""

        # 循环渲染屏幕，每一帧都会在循环中渲染到界面
        while True:
            # 监听键盘和鼠标事件
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    # 退出游戏
                    sys.exit()
            # 设置背景色
            self.screen.fill(self.settings.bg_color)
            # 渲染游戏界面
            pygame.display.flip()


if __name__ == '__main__':
    # 创建启动类
    ai = AlienInvasion()
    # 启动游戏
    ai.start()
