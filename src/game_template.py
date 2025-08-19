# game_template.py
import sys
import pygame

# ---------- 基础配置 ----------
WIDTH, HEIGHT = 640, 480
FPS            = 60
TITLE          = "Game Template"

# ---------- 核心类 ----------
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock  = pygame.time.Clock()
        self.running = True

    # 处理事件
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # TODO: 添加键盘/鼠标事件

    # 更新逻辑
    def update(self, dt):
        # TODO: 在此更新游戏对象
        pass

    # 绘制
    def draw(self):
        self.screen.fill((30, 30, 30))  # 清屏
        # TODO: 在此绘制精灵/文字等
        pygame.display.flip()

    # 主循环
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # 秒
            self.handle_events()
            self.update(dt)
            self.draw()
        self.quit()

    # 退出
    def quit(self):
        pygame.quit()
        sys.exit()

# ---------- 运行 ----------
if __name__ == "__main__":
    Game().run()