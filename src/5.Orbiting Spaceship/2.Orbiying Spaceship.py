# Orbit Demo
# Chapter 5

import sys, random, math, pygame
from pygame.locals import *
from pathlib import Path

# Point类 - 表示二维空间中的一个点
class Point(object):
    def __init__(self, x, y):
        self.__x = x  # 私有x坐标
        self.__y = y  # 私有y坐标

    # property修饰器的用处:不改变接口，直接修改数据。
    # X属性 - 使用property装饰器实现getter和setter
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    # Y属性 - 使用property装饰器实现getter和setter
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        # 返回点的字符串表示，格式为 {X:值,Y:值}
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"
    
# print_text函数 - 在屏幕上绘制文本
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)  # 渲染文本为图像
    screen.blit(imgText, (x,y))  # 在指定位置绘制文本

# wrap_angle函数 - 将角度限制在0-360度范围内，规范角度
def wrap_angle(angle):
    return angle % 360

# 主程序开始
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((800,600))  # 创建800x600的窗口
pygame.display.set_caption("Orbit Demo")  # 设置窗口标题
font = pygame.font.Font(None, 18)  # 创建字体对象，使用默认字体，大小18

# 直接构建图片路径
# 使用pathlib构建跨平台的资源文件路径
space_path = Path(__file__).parent / "Res" / "space.png"  # 星空背景图片路径
ship_path = Path(__file__).parent / "Res" / "freelance.png"  # 飞船图片路径
planet_path = Path(__file__).parent / "Res" / "planet2.png"  # 行星图片路径
ship2_path=Path(__file__).parent / "Res" / "military.png"

# 加载位图
space = pygame.image.load(str(space_path)).convert_alpha()  # 加载星空背景，支持透明通道
planet = pygame.image.load(str(planet_path)).convert_alpha()  # 加载行星图片，支持透明通道
ship = pygame.image.load(str(ship_path)).convert_alpha()  # 加载飞船图片，支持透明通道
ship2 =pygame.image.load(str(ship2_path)).convert_alpha()  # 加载飞船图片，支持透明通道
# 调整飞船大小 - 缩小为原来的一半
width,height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width//2, height//2))

# 初始化变量
radius = 250  # 飞船绕行星飞行的轨道半径
angle = 0.0   # 飞船当前角度
pos = Point(0,0)  # 飞船当前位置
old_pos = Point(0,0)  # 飞船上一帧的位置
# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == QUIT:  # 如果点击关闭按钮
            sys.exit()  # 退出程序
    keys = pygame.key.get_pressed()  # 获取按键状态
    if keys[K_ESCAPE]:  # 如果按下ESC键
        sys.exit()  # 退出程序

    # 绘制背景
    screen.blit(space, (0,0))

    # 绘制行星 - 将行星绘制在屏幕中央
    width,height = planet.get_size()
    screen.blit(planet, (400-width/2,300-height/2))

    # 移动飞船 - 沿着圆形轨道运动
    angle = wrap_angle(angle - 0.1)  # 角度递减，逆时针旋转

    
    # 根据角度计算飞船在轨道上的位置（使用三角函数）
    pos.x = math.sin( math.radians(angle) ) * radius
    pos.y = math.cos( math.radians(angle) ) * radius


    # 旋转飞船 - 根据运动方向调整飞船朝向
    delta_x = ( pos.x - old_pos.x )  # x方向变化量
    delta_y = ( pos.y - old_pos.y )  # y方向变化量
    # atan2函数作用:返回点 (delta_y, delta_x) 与 x 轴正方向的夹角（弧度），范围[-π, π]
    # 飞船一
    rangle = math.atan2(delta_y, delta_x)  # 计算运动方向的角度（弧度）
    rangled = wrap_angle( -math.degrees(rangle) )  # 转换为角度并包装
    # 用法 pygame.transform.rotate(图像, 角度) 旋转图像，角度为逆时针方向
    scratch_ship = pygame.transform.rotate(ship, rangled)  # 旋转飞船图像
    
    # 绘制飞船
    width,height = scratch_ship.get_size()  # 获取旋转后飞船的尺寸
    x = 400+pos.x-width//2  # 计算飞船绘制位置的x坐标（屏幕中心+轨道位置）
    y = 300+pos.y-height//2  # 计算飞船绘制位置的y坐标（屏幕中心+轨道位置）
    screen.blit(scratch_ship, (x,y))  # 在计算位置绘制飞船

    # 显示调试信息
    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))  # 显示轨道角度
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))  # 显示旋转角度
    print_text(font, 0, 40, "Position: " + str(pos))  # 显示当前位置
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))  # 显示上一帧位置
    
    pygame.display.update()  # 更新屏幕显示
    
    # 记录当前位置作为下一帧的"旧位置"
    old_pos.x = pos.x
    old_pos.y = pos.y