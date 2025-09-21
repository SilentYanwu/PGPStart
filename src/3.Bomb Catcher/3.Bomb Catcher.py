# Bomb Catcher Game
# 第四章

import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    # 在屏幕上打印文本的辅助函数
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

# 主程序开始
pygame.init()
screen = pygame.display.set_mode((800,600))  # 创建游戏窗口
pygame.display.set_caption("Bomb Catching Game")  # 设置窗口标题

font1 = pygame.font.Font(None, 24)  # 创建字体对象
pygame.mouse.set_visible(False)  # 隐藏鼠标光标

white = 255,255,255  # 定义颜色：白色
red = 220, 50, 50  # 定义颜色：红色
yellow = 230,230,50  # 定义颜色：黄色
black = 0,0,0  # 定义颜色：黑色

lives = 5  # 玩家生命值
score = 0  # 玩家得分
clock_start = 0  # 游戏时钟起始时间（未使用）
game_over = True  # 游戏是否结束的标志
mouse_x = mouse_y = 0  # 鼠标坐标

pos_x = 300  # 篮子初始x坐标
pos_y = 460  # 篮子初始y坐标

bomb_x = random.randint(0,800)  # 炸弹初始x坐标（随机）
bomb_y = -50  # 炸弹初始y坐标（从屏幕上方开始）
vel_y = 0.6  # 炸弹下落速度

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()  # 退出游戏
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos  # 获取鼠标位置
            move_x,move_y = event.rel  # 获取鼠标相对移动（未使用）
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False  # 开始新游戏
                lives = 3  # 重置生命值
                score = 0  # 重置得分

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()  # 按ESC键退出游戏

    screen.fill((0,0,100))  # 用深蓝色填充屏幕

    # 移动炸弹部分
    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>")  # 显示游戏开始提示
    else:
        # 移动炸弹
        bomb_y += vel_y

        # 检查玩家是否错过了炸弹
        if bomb_y > 550:
            bomb_x = random.randint(0, 800)  # 重置炸弹位置
            bomb_y = -50
            lives -= 1  # 减少生命值
            if lives == 0:
                game_over = True  # 游戏结束

        # 检查玩家是否接住了炸弹
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10  # 增加得分
                bomb_x = random.randint(0, 500)  # 重置炸弹位置
                bomb_y = -50
        
        # 绘制炸弹（带黑色边框的黄色圆形）
        pygame.draw.circle(screen, black, (bomb_x-4,int(bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (bomb_x,int(bomb_y)), 30, 0)

        # 设置篮子位置
        pos_x = mouse_x  # 篮子跟随鼠标移动
        if pos_x < 0:
            pos_x = 0  # 限制篮子不超出左边界
        elif pos_x > 700:
            pos_x = 700  # 限制篮子不超出右边界
            
        # 绘制篮子（带黑色边框的红色矩形）
        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (pos_x,pos_y,120,40), 0)

    # 显示剩余生命数
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    # 显示得分
    print_text(font1, 700, 0, "SCORE: " + str(score))
    
    pygame.display.update()  # 更新屏幕显示