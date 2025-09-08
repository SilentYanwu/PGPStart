import pygame
import sys
from pygame.locals import *

# 定义颜色
white = (255, 255, 255)
blue = (0, 0, 200)

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Hello Pygame")  # 添加窗口标题

# 创建字体对象
try:
    myfont = pygame.font.Font(None, 50)
except:
    myfont = pygame.font.SysFont('arial', 50)  # 备用字体

textImage = myfont.render("Hello Pygame", True, white) #添加内容

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
    
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()