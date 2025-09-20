# 鼠标事件示例

import sys, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    """在屏幕上打印文本的辅助函数"""
    imgText = font.render(text, True, color)  # 渲染文本为图像
    screen.blit(imgText, (x,y))               # 绘制文本到屏幕
    

# 主程序开始
pygame.init()
screen = pygame.display.set_mode((600,500))  # 创建600x500像素窗口
pygame.display.set_caption("Mouse Demo")     # 设置窗口标题
font1 = pygame.font.Font(None, 30)           # 创建30号字体
white = 255,255,255                          # 定义白色

# 初始化鼠标相关变量
seconds = 10              # 游戏时间（未使用）
score = 0                 # 得分（未使用）
clock_start = 0           # 计时开始时间（未使用）
game_over = True          # 游戏结束标志（未使用）
mouse_x = mouse_y = 0     # 鼠标当前位置坐标
move_x = move_y = 0       # 鼠标相对移动距离
mouse_down = mouse_up = 0 # 鼠标按下/释放的按钮编号
mouse_down_x = mouse_down_y = 0  # 鼠标按下时的坐标
mouse_up_x = mouse_up_y = 0      # 鼠标释放时的坐标

# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == QUIT:           # 退出事件
            sys.exit()
        elif event.type == MOUSEMOTION:  # 鼠标移动事件
            mouse_x,mouse_y = event.pos  # 获取鼠标当前位置
            move_x,move_y = event.rel    # 获取鼠标相对移动距离
        elif event.type == MOUSEBUTTONDOWN:  # 鼠标按下事件
            mouse_down = event.button    # 获取按下的按钮编号
            mouse_down_x,mouse_down_y = event.pos  # 获取按下时的坐标
        elif event.type == MOUSEBUTTONUP:    # 鼠标释放事件
            mouse_up = event.button      # 获取释放的按钮编号
            mouse_up_x,mouse_up_y = event.pos  # 获取释放时的坐标

    # 键盘检测
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:  # 按ESC键退出
        sys.exit()

    # 清屏（深绿色背景）
    screen.fill((0,100,0))

    # 显示鼠标事件信息
    print_text(font1, 0, 0, "Mouse Events")  # 标题
    print_text(font1, 0, 20, "Mouse position: " + str(mouse_x) +
               "," + str(mouse_y))  # 鼠标当前位置
    print_text(font1, 0, 40, "Mouse relative: " + str(move_x) +
               "," + str(move_y))   # 鼠标相对移动距离

    print_text(font1, 0, 60, "Mouse button down: " + str(mouse_down) +
               " at " + str(mouse_down_x) + "," + str(mouse_down_y))  # 鼠标按下信息

    print_text(font1, 0, 80, "Mouse button up: " + str(mouse_up) +
               " at " + str(mouse_up_x) + "," + str(mouse_up_y))  # 鼠标释放信息

    # 显示鼠标轮询信息
    print_text(font1, 0, 160, "Mouse Polling")  # 轮询方式标题
    
    # 使用轮询方式获取鼠标位置
    x,y = pygame.mouse.get_pos()
    print_text(font1, 0, 180, "Mouse position: " + str(x) + "," + str(y))

    # 使用轮询方式获取鼠标按钮状态
    b1, b2, b3 = pygame.mouse.get_pressed()
    print_text(font1, 0, 200, "Mouse buttons: " + 
               str(b1) + "," + str(b2) + "," + str(b3))  # 左键、中键、右键状态
    
    # 更新显示
    pygame.display.update()