#  键盘事件示例
# 导入必要的模块
import sys       # 系统相关功能，如退出程序
import random    # 生成随机数
import time      # 时间相关功能
import pygame    # 游戏开发库
from pygame.locals import *  # 导入Pygame常量

def print_text(font, x, y, text, color=(255,255,255)):
    """
    在屏幕上打印文本的辅助函数
    
    参数:
    font: 字体对象
    x, y: 文本显示的坐标位置
    text: 要显示的文本内容
    color: 文本颜色，默认为白色
    """
    imgText = font.render(text, True, color)  # 将文本渲染为图像
    screen.blit(imgText, (x,y))               # 将文本图像绘制到屏幕上
    

# 主程序开始
pygame.init()  # 初始化Pygame所有模块

# 创建游戏窗口，大小为600x500像素
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Keyboard Demo")  # 设置窗口标题

# 创建两种字体对象
font1 = pygame.font.Font(None, 24)   # 小字体，用于说明文字和状态信息
font2 = pygame.font.Font(None, 200)  # 大字体，用于显示目标字母

# 定义颜色元组（RGB格式）
white = 255,255,255   # 白色
yellow = 255,255,0    # 黄色，用于显示目标字母
deepgreen = 0,100,0       # 绿色，可用于其他提示（虽然代码中未使用）

# 初始化游戏状态变量
key_flag = False          # 标记是否有按键按下（True表示有按键按下）
correct_answer = 97       # 初始目标字母的ASCII码（97对应小写字母'a'）
seconds = 10              # 游戏总时间（秒）
score = 0                 # 玩家得分（正确输入的字母数量）
clock_start = 0           # 游戏开始的时间点
game_over = True          # 游戏是否结束的标志（True表示游戏未开始或已结束）

# 游戏主循环（无限循环，直到用户退出）
while True:
    # 事件处理循环：处理所有待处理的事件
    for event in pygame.event.get():
        if event.type == QUIT:           # 如果收到退出事件（如点击窗口关闭按钮）
            sys.exit()                   # 退出程序
        elif event.type == KEYDOWN:      # 如果检测到按键按下事件
            key_flag = True              # 设置按键标志为True
        elif event.type == KEYUP:        # 如果检测到按键释放事件
            key_flag = False             # 设置按键标志为False

    # 获取所有按键的当前状态（实时检测，不同于事件驱动的方式）
    keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]:  # 如果ESC键被按下
        sys.exit()      # 退出程序

    # 处理回车键：开始或重新开始游戏
    if keys[K_RETURN]:
        if game_over:   # 只有在游戏结束状态才能开始新游戏
            game_over = False  # 设置游戏状态为进行中
            score = 0          # 重置得分为0
            seconds = 11       # 设置游戏时间为11秒（为了让倒计时从10开始显示）
            clock_start = time.perf_counter()  # 修正：使用perf_counter()替代clock()

    # 计算游戏进行的时间
    current = time.perf_counter() - clock_start  # 修正：使用perf_counter()替代clock()
    
    # 计算打字速度：每分钟输入的字母数（10秒内的得分乘以6）
    speed = score * 6

    # 检查游戏是否应该结束
    if seconds - current < 0:  # 如果剩余时间小于0（时间到）
        game_over = True       # 设置游戏结束标志
    elif current <= 10:        # 如果游戏还在进行中（时间未到）
        if keys[correct_answer]:  # 如果玩家按下了目标字母键
            correct_answer = random.randint(97, 122)  # 随机生成新的目标字母（97-122对应a-z）
            score += 1          # 增加得分

    # 清空屏幕，用深绿色填充背景
    screen.fill(deepgreen)

    # 显示游戏标题和说明文字
    print_text(font1, 0, 0, "Let's see how fast you can type!")
    print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

    # 如果有按键按下，在屏幕右上角显示提示
    if key_flag:
        print_text(font1, 500, 0, "<key>")

    # 如果游戏正在进行中，显示剩余时间
    if not game_over:
        print_text(font1, 0, 80, "Time: " + str(int(seconds - current)))

    # 显示当前打字速度（字母/分钟）
    print_text(font1, 0, 100, "Speed: " + str(speed) + " letters/min")

    # 如果游戏已结束，显示开始游戏的提示
    if game_over:
        print_text(font1, 0, 160, "Press Enter to start...")

    # 显示当前目标字母（将ASCII码转换为大写字母显示）
    # correct_answer-32：将小写字母ASCII码转换为大写字母ASCII码
    # chr()：将ASCII码转换为对应的字符
    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    # 更新显示，将绘制的内容显示到屏幕上
    pygame.display.update()