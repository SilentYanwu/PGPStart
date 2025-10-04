import pygame, sys
from pygame.locals import *

bg_color = (129, 216, 208)

# 参数定义
pos_x = 300
pos_y = 250  
vel_x = 2
vel_y = 1
acceleration = 0.1
WIDTH=1000
HEGIHT=800

# 初始化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEGIHT))
pygame.display.set_caption("会动的矩形")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # 按ESC键退出
                pygame.quit()
                sys.exit()
                
     # 应该在事件循环外填充背景色和更新位置
    screen.fill(bg_color)
    
    # 矩形动起来
    pos_x += vel_x
    pos_y += vel_y
    
    # 保持矩形在屏幕上 (边界检查)
    if pos_x > 900 or pos_x < 0:  # 1000-100=900 (矩形宽度100)
        vel_x = -vel_x
    if pos_y > 700 or pos_y < 0:  # 800-100=700 (矩形高度100)
        vel_y = -vel_y
    
    # 画出矩形
    color = (255,0,0)
    width = 5
    pos = (pos_x, pos_y, 100, 100)  # 添加括号使元组更清晰
    # rect（surface, color, rect, width=0）-> Rect
    pygame.draw.rect(screen, color, pos, width)
    
    pygame.display.flip()
