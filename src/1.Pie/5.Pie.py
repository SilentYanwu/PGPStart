import math
import pygame,sys
from pygame.locals import *
# ---------- 参数设置 ----------
WIDTH=1000
HEGIHT=800
bg_color=(129, 216, 208)
color=(200,80,60)
completed_color = (255, 255, 0)  
width=4
x=WIDTH/2
y=HEGIHT/2
radius=200
# 圈定了圆弧范围（范围左上角x值，左上角y值，长，宽）
position=(x-radius,y-radius,2*radius,2*radius)

piece1=False
piece2=False
piece3=False
piece4=False
# ---------- 初始化 ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEGIHT))
pygame.display.set_caption("The Pie Game")
# 创建字体对象
try:
    myfont = pygame.font.Font(None, 50)
except:
    myfont = pygame.font.SysFont('arial', 50)  # 备用字体

# ----------函数定义---------
def draw_number(text,x,y,color):
    textimg=myfont.render(text,True,color)
    screen.blit(textimg,(x,y))
# ---------- 循环 ----------
loop=True
while loop:
    for event in pygame.event.get():
        if event.type== QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_1:
                piece1=True
            elif event.key==pygame.K_2:
                piece2=True
            elif event.key==pygame.K_3:
                piece3=True
            elif event.key==pygame.K_4:
                piece4=True

    screen.fill(bg_color)
    #画出数字
    draw_number("1",x+radius/2,y-radius/2,color)
    draw_number("2",x-radius/2,y-radius/2,color)
    draw_number("3",x-radius/2,y+radius/2,color)
    draw_number("4",x+radius/2,y+radius/2,color)
                
    # 是否应该涂饼
    if piece1:
        start_angle=math.radians(0)
        end_angle=math.radians(90)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
    if piece2:
        start_angle=math.radians(90)
        end_angle=math.radians(180)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
    if piece3:
        start_angle=math.radians(180)
        end_angle=math.radians(270)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
    if piece4:
        start_angle=math.radians(270)
        end_angle=math.radians(360)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
        
    # 检测饼完成
    if (piece1 and piece2 and piece3 and piece4):
        color=completed_color
        Finishfont = pygame.font.SysFont('simhei', 50)  # 黑体
        FinishImg=Finishfont.render("你过关!",True,color)
        screen.blit(FinishImg,(x-75,y-1.5*radius))
        

    pygame.display.flip()