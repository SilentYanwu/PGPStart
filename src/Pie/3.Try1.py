import math
import pygame
import sys

# ---------- 常量 ----------
WIDTH, HEIGHT = 1000, 800
FPS = 60
TITLE = "会动的圆"
BG_COLOR = (129,216,208)
CIRCLE_COLOR = (255, 255, 0)
LINE_WIDTH = 10

# ---------- 初始化 ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# ---------- 动画参数 ----------
base_radius = 150               # 圆的基准半径
radius_amplitude = 70           # 半径变化幅度
speed_r = 2                     # 半径变化速度（弧度/帧）

base_x = WIDTH // 2             # x轴基准位置
x_amplitude = 200               # x方向摆动幅度
speed_x = 1.5                   # x摆动速度（弧度/帧）

time = 0                        # 帧计数器（当作角度 t）

# ---------- 主循环 ----------
running = True
while running:
    # 1. 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # 2. 更新
    time += 0.05  # 每帧时间增量（可调整速度）
    radius = base_radius + radius_amplitude * math.sin(time * speed_r)
    center_x = base_x + x_amplitude * math.sin(time * speed_x)
    center = (int(center_x), HEIGHT // 2)

    # 3. 绘制
    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, CIRCLE_COLOR, center, int(radius), LINE_WIDTH)
    pygame.display.flip()

    # 4. 控制帧率
    clock.tick(FPS)

# 5. 退出
pygame.quit()
sys.exit()