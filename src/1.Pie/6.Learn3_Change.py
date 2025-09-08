import pygame, sys, random
from pygame.locals import *

bg_color = (129, 216, 208)

# 参数定义
pos_x = 300
pos_y = 250  
vel_x = 2
vel_y = 1
WIDTH = 1000
HEIGHT = 800

# 初始化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("会变色的矩形")

# 初始颜色
color = (255, 0, 0)  # 红色
width = 5

def get_random_color():
    """生成随机颜色"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
clock = pygame.time.Clock()  # 添加时钟控制帧率

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # 按ESC键退出
                pygame.quit()
                sys.exit()
    
    # 更新位置
    pos_x += vel_x
    pos_y += vel_y
    
    # 边界检查和颜色变化
    hit_boundary = False
    if pos_x > 900 or pos_x < 0: 
        vel_x = -vel_x
        hit_boundary = True
    if pos_y > 700 or pos_y < 0:  
        vel_y = -vel_y
        hit_boundary = True
    
    # 如果撞到边界，改变颜色
    if hit_boundary:
        color = get_random_color()
 
    # 填充背景色
    screen.fill(bg_color)
    
    # 画出矩形
    pos = (pos_x, pos_y, 100, 100)
    pygame.draw.rect(screen, color, pos, width)
    
    # 显示当前颜色值（可选）
    myfont = pygame.font.SysFont('simhei', 24)  # 黑体
    color_text = f"颜色: RGB{color}"
    text_surface = myfont.render(color_text, True, color)
    screen.blit(text_surface, (10, 10))
    
    pygame.display.flip()
    clock.tick(120)  # 限制帧率为120FPS

pygame.quit()