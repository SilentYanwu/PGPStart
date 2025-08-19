import pygame
import sys
from pygame.locals import *

'''
pygame.draw.circle(surface, color, center, radius, width=0)
surface	要画到的 Surface（通常是 screen）
color	颜色，RGB 三元组，如 (255, 255, 0)
center	圆心坐标，整型元组 (x, y)
radius	半径，整数
width	可选，描边粗细；
'''
# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("画个圆")  # 添加窗口标题

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # 按ESC键退出
                pygame.quit()
                sys.exit()
                
    screen.fill((0,0,200))
    
    #画个圆
    color=255,255,0
    position=300,250
    radius =200
    width=10
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()
    
    