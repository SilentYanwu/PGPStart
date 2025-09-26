# Analog Clock Demo - 模拟时钟演示程序
# Chapter 5 - 第5章

import sys, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time

# 打印文本的辅助函数
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)  # 使用指定字体和颜色渲染文本
    screen.blit(imgText, (x,y))  # 在屏幕的(x,y)位置绘制文本

# 角度包装函数，确保角度在0-360度范围内
def wrap_angle(angle):
    return angle % 360  # 使用模运算将角度限制在0-359度

# 主程序开始
pygame.init()  # 初始化pygame所有模块
screen = pygame.display.set_mode((600,500))  # 创建600x500像素的窗口
pygame.display.set_caption("Analog Clock Demo")  # 设置窗口标题为"模拟时钟演示"
font = pygame.font.Font(None, 36)  # 创建默认字体，大小36像素

# 定义颜色常量
orange = 220,180,0    # 橙色 - 用于分钟指针
white = 255,255,255   # 白色 - 用于表盘和中心点
yellow = 255,255,0    # 黄色 - 用于秒钟指针
pink = 255,100,100    # 粉色 - 用于小时指针

# 时钟几何参数设置
pos_x = 300   # 表盘中心点的x坐标（屏幕水平中心）
pos_y = 250   # 表盘中心点的y坐标（屏幕垂直中心）
radius = 250  # 表盘的半径
angle = 360   # 初始角度值

# 主游戏循环
while True:
    # 事件处理部分
    for event in pygame.event.get():  # 获取所有待处理的事件
        if event.type == QUIT:  # 如果检测到窗口关闭事件
            sys.exit()  # 退出程序
    
    # 键盘状态检测
    keys = pygame.key.get_pressed()  # 获取所有按键的当前状态
    if keys[K_ESCAPE]:  # 如果ESC键被按下
        sys.exit()  # 退出程序

    # 清空屏幕并填充背景色
    screen.fill((0,0,100))  # 用深蓝色(0,0,100)填充整个屏幕

    # 绘制表盘外圈
    # 参数：表面，颜色，中心位置，半径，线宽
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)  # 绘制白色空心圆，线宽6像素

    # 绘制时钟数字1-12
    for n in range(1,13):  # 循环12次，对应1到12的数字
        angle = math.radians( n * (360/12) - 90 )  # 计算每个数字的角度并转换为弧度
        # 12个数字均匀分布在圆周上，每个间隔30度(360/12)
        # 减去90度使12点位置在正上方（默认0度在正右方）
        
        x = math.cos( angle ) * (radius-20)-10 # 计算数字的x坐标：(半径-20)使数字向内偏移，-10用于文本居中
        y = math.sin( angle ) * (radius-20)-10  # 计算数字的y坐标
        
        print_text(font, pos_x+x, pos_y+y, str(n))  # 在计算出的位置绘制数字

    # 获取当前时间
    today = datetime.today()  # 获取当前日期时间对象
    hours = today.hour % 12   # 获取小时数并转换为12小时制（0-11）
    minutes = today.minute    # 获取分钟数（0-59）
    seconds = today.second    # 获取秒数（0-59）

    # 绘制时针
    hour_angle = wrap_angle( hours * (360/12) - 90 )  # 计算时针角度：每小时30度(360/12)
    hour_angle = math.radians( hour_angle )  # 将角度转换为弧度供三角函数使用
    hour_x = math.cos( hour_angle ) * (radius-80)  # 计算时针端点的x坐标（时针比表盘短80像素）
    hour_y = math.sin( hour_angle ) * (radius-80)  # 计算时针端点的y坐标
    target = (pos_x+hour_x, pos_y+hour_y)  # 时针端点目标位置
    #参数  ：表面，颜色，起点，终点，线宽
    pygame.draw.line(screen, pink, (pos_x,pos_y), target, 25)  # 绘制粉色时针，线宽25像素

    # 绘制分针
    min_angle = wrap_angle( minutes * (360/60) - 90 )  # 计算分针角度：每分钟6度(360/60)
    min_angle = math.radians( min_angle )  # 角度转弧度
    min_x = math.cos( min_angle ) * (radius-60)  # 分针端点x坐标（比表盘短60像素）
    min_y = math.sin( min_angle ) * (radius-60)  # 分针端点y坐标
    target = (pos_x+min_x, pos_y+min_y)  # 分针端点目标位置
    #参数  ：表面，颜色，起点，终点，线宽
    pygame.draw.line(screen, orange, (pos_x,pos_y), target, 12)  # 绘制橙色分针，线宽12像素

    # 绘制秒针
    sec_angle = wrap_angle( seconds * (360/60) - 90 )  # 计算秒针角度：每秒6度(360/60)
    sec_angle = math.radians( sec_angle )  # 角度转弧度
    sec_x = math.cos( sec_angle ) * (radius-40)  # 秒针端点x坐标（比表盘短40像素）
    sec_y = math.sin( sec_angle ) * (radius-40)  # 秒针端点y坐标
    target = (pos_x+sec_x, pos_y+sec_y)  # 秒针端点目标位置
    pygame.draw.line(screen, yellow, (pos_x,pos_y), target, 6)  # 绘制黄色秒针，线宽6像素

    # 绘制中心覆盖圆点
    # 参数：表面，颜色，中心位置，半径
    pygame.draw.circle(screen, white, (pos_x,pos_y), 20)  # 在中心绘制白色实心圆，半径20像素

    # 在屏幕左上角显示数字时间
    print_text(font, 0, 0, str(today.hour) + ":" + str(minutes) + ":" + str(seconds))
    
    # 更新显示
    pygame.display.update()  # 刷新屏幕，显示所有绘制的内容