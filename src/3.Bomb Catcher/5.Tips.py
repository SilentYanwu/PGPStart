import pygame
import math

# 初始化
pygame.init()
screen = pygame.display.set_mode((400, 300))

# 颜色定义
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))  # 填充背景为白色
    
    # 绘制示例
    # 参数（屏幕，颜色，圆心坐标，半径，线宽）
    pygame.draw.circle(screen, RED, (100, 100), 40, 0)  # 实心圆
    pygame.draw.circle(screen, BLUE, (200, 100), 40, 3) # 空心圆

    # 圆弧（笑脸的嘴巴）
    # 参数（屏幕，颜色，矩形区域（四个角），起始角度，结束角度，线宽）
    pygame.draw.arc(screen, BLACK, (75, 75, 50, 50), math.pi, 2*math.pi, 2)

    # 直线（十字架）
    # 参数（屏幕，颜色，起点坐标，终点坐标，线宽）
    pygame.draw.line(screen, GREEN, (300, 50), (300, 150), 3)  # 竖线
    pygame.draw.line(screen, GREEN, (250, 100), (350, 100), 3) # 横线

    pygame.display.update()  # 更新屏幕显示