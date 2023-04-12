import sys
import pygame


class AlienInvasion:
    """游戏主类，管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏，创建资源"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def start(self):
        """启动游戏"""
        while True:
            # 监听键盘和鼠标事件
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    sys.exit()

            # 展示主界面
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.start()
