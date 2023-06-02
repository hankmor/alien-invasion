class Settings:
    def __init__(self):
        # 游戏基础设置
        self.caption = "外星人入侵"  # 游戏名称
        self.version = "0.1.0"  # 游戏版本
        self.width = 1200  # 屏幕宽度
        self.height = 800  # 屏幕高度
        self.bg_color = (230, 230, 230)  # 屏幕背景色
        # 飞船设置
        self.speed = 2.5  # 飞船的移动速度
        # 子弹设置
        self.bullet_speed = 1  # 子弹速度
        self.bullet_width = 3  # 子弹宽
        self.bullet_height = 16  # 子弹高
        self.bullet_color = (60, 60, 60)  # 子弹颜色
        self.bullet_limit = 5  # 最大子弹数量
