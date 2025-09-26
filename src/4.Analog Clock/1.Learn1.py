# Circle Demo - 圆形演示程序
# Chapter 5 - 第5章
# 一个特炫酷的效果

import random, math, pygame,sys
from pygame.locals import *

# 主程序开始
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((600,500))  # 创建600x500像素的窗口
pygame.display.set_caption("Circle Demo")  # 设置窗口标题
screen.fill((0,0,100))  # 用深蓝色填充背景

# 初始化变量
pos_x = 300  # 圆心x坐标（屏幕水平中心）
pos_y = 250  # 圆心y坐标（屏幕垂直中心）
radius = 200  # 圆形轨迹半径
angle = 360   # 起始角度（360度）

# 主循环开始
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == QUIT:  # 如果点击关闭按钮
            sys.exit()  # 退出程序
    
        # 键盘输入检测
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:  # 如果按下ESC键
            sys.exit()  # 退出程序

    # 角度递增
    angle += 1  # 每帧角度增加1度
    if angle >= 360:  # 如果角度超过360度（完成一圈）
        angle = 0  # 重置角度为0
        # 随机生成新颜色 三元组元素法
        r = random.randint(0,255)  # 红色分量
        g = random.randint(0,255)  # 绿色分量
        b = random.randint(0,255)  # 蓝色分量
        color = r,g,b  # 组合成RGB颜色元组

    # 计算圆形轨迹上的坐标
    # 使用三角函数计算圆上的点坐标
    # math.radians()将角度转换为弧度
    x = math.cos( math.radians(angle) ) * radius  # x坐标 = cos(角度) × 半径
    y = math.sin( math.radians(angle) ) * radius  # y坐标 = sin(角度) × 半径

    # 在圆形轨迹上绘制一个点
    pos = ( int(pos_x + x), int(pos_y + y) )  # 计算实际屏幕位置（圆心坐标 + 偏移量）
    pygame.draw.circle(screen, color, pos, 10, 0)  # 绘制半径为10像素的实心圆

    # 更新显示
    pygame.display.update()  # 刷新屏幕，显示最新绘制的内容