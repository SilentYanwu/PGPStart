import sys, pygame
from pygame.locals import *
import os


# 颜色定义字典
Colors = {
    'white': (255, 255, 255),   # 白色
    'green': (0, 255, 0),       # 绿色（正确）
    'red': (255, 0, 0),         # 红色（错误）
    'yellow': (255, 255, 0),    # 黄色（问题）
    'purple': (255, 0, 255),    # 紫色（提示）
    'cyan': (0, 255, 255),       # 青色（可选）
    'difn': (129,216,208),
    'hailan':(0, 105, 148)
}


class Trivia(object):
    """问答游戏类，管理游戏状态和逻辑"""
    
    def __init__(self, filename):
        # 初始化游戏状态变量
        self.data = []              # 存储所有问答数据
        self.current = 0            # 当前题目索引
        self.total = 0              # 总题目数量
        self.correct = 0            # 正确答案编号(1-4)
        self.score = 0              # 玩家得分
        self.scored = False         # 是否答对
        self.failed = False         # 是否答错
        self.wronganswer = 0        # 错误答案编号
        self.game_over = False  # 游戏是否结束
        self.colors = [Colors['white'], Colors['white'], Colors['white'], Colors['white']]  
        # 选项颜色

        # 读取问答数据文件
        try:
            with open(filename, "r", encoding='utf-8') as f:
                trivia_data = f.readlines()
        except FileNotFoundError:
            print(f"错误：找不到文件 {filename}")
            sys.exit(1)
        except Exception as e:
            print(f"读取文件时出错：{e}")
            sys.exit(1)
            
        # 处理数据：清理并存储
        for text_line in trivia_data:
            cleaned_line = text_line.strip()  # 去除每行首尾空白字符
            self.data.append(cleaned_line)    # 添加到数据列表
            self.total += 1                   # 增加总题目计数

    def show_question(self):
        """显示当前问题和选项"""
        if self.game_over == True:
            self.show_game_over()
        else:
        # 显示游戏标题和说明
            print_text(font1, 210, 5, "问答游戏")
            print_text(font2, 190, 480, "按数字键(1-4)选择答案", Colors['purple'])
            print_text(font2, 530, 5, "得分", Colors['purple'])
            print_text(font2, 550, 25, str(self.score), Colors['purple'])

            # 获取正确答案（每组数据的第6个元素）
            self.correct = int(self.data[self.current + 5])

            # 显示当前问题编号和内容
            question = self.current // 6 + 1  # 计算当前是第几题
            print_text(font1, 5, 80, "问题 " + str(question))
            print_text(font2, 20, 120, self.data[self.current], Colors['yellow'])

            # 处理答题结果显示
            if self.scored:  # 如果答对了
                self.colors = [Colors['white'], Colors['white'], Colors['white'], Colors['white']]
                self.colors[self.correct - 1] = Colors['green']  # 正确答案显示绿色
                print_text(font1, 230, 380, "回答正确!", Colors['green'])
                print_text(font2, 170, 420, "按回车键进入下一题", Colors['green'])
            elif self.failed:  # 如果答错了
                self.colors = [Colors['white'], Colors['white'], Colors['white'], Colors['white']]
                self.colors[self.wronganswer - 1] = Colors['red']    # 错误答案显示红色
                self.colors[self.correct - 1] = Colors['green']      # 正确答案显示绿色
                print_text(font1, 220, 380, "回答错误!", Colors['red'])
                print_text(font2, 170, 420, "按回车键进入下一题", Colors['red'])

            # 显示四个选项
            print_text(font1, 5, 170, "选项")
            print_text(font2, 20, 210, "1 - " + self.data[self.current + 1], self.colors[0])
            print_text(font2, 20, 240, "2 - " + self.data[self.current + 2], self.colors[1])
            print_text(font2, 20, 270, "3 - " + self.data[self.current + 3], self.colors[2])
            print_text(font2, 20, 300, "4 - " + self.data[self.current + 4], self.colors[3])

    def handle_input(self, number):
        """处理玩家输入的答案"""
        if self.game_over:  # 游戏结束时的输入处理
            if number == 1:  # 重新开始
                self.__init__(file)  # 重新初始化游戏
            elif number == 2:  # 退出游戏
                pygame.quit()
                sys.exit()
            return
        # 主要作用：游戏状态保护，确保玩家只能答一次题，正确答案出现以后，界面就保存了，无法改动。
        if not self.scored and not self.failed:  # 只有在未答题时才处理
            if number == self.correct:  # 答案正确
                self.scored = True
                self.score += 1  # 增加得分
            else:  # 答案错误
                self.failed = True
                self.wronganswer = number  # 记录错误答案

    def next_question(self):
        """进入下一题"""
        if self.scored or self.failed:  # 只有在答题后才可以进入下一题
            # 重置状态
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [Colors['white'], Colors['white'], Colors['white'], Colors['white']]
            
            # 移动到下一组题目（每组6行数据）
            self.current += 6
            # 如果超过总题目数，则触发结束标志位。
            if self.current >= self.total:
                self.game_over = True   

    def show_game_over(self):
        """显示游戏结束界面"""
        # 清空背景
        screen.fill(Colors['hailan'])
        
        # 显示结束标题
        print_text(font1, 210, 50, "游戏结束", Colors['yellow'])
        
        # 显示最终分数
        print_text(font1, 210, 120, f"最终得分: {self.score}/{self.total//6}", Colors['white'])
        
        # 显示选项
        print_text(font2, 200, 200, "1 - 重新开始", Colors['green'])
        print_text(font2, 200, 240, "2 - 退出游戏", Colors['red'])
        print_text(font2, 200, 280, "按数字键选择", Colors['purple'])
                

def print_text(font, x, y, text, color=(255, 255, 255), shadow=True):
    """在屏幕上打印文本，带有阴影效果"""
    if shadow:  # 添加阴影效果
        imgText = font.render(text, True, (0, 0, 0))  # 黑色阴影
        screen.blit(imgText, (x - 2, y - 2))
    imgText = font.render(text, True, color)  # 主要文本
    screen.blit(imgText, (x, y))
    

if __name__ == "__main__":
    # 主程序开始
    pygame.init()
    screen = pygame.display.set_mode((600, 500))  # 创建游戏窗口
    pygame.display.set_caption("问答游戏")        # 设置窗口标题
    
    # 下面是关于Pygame没有中文的统一解决方案
    # 设置中文字体 - 根据系统选择字体
    # Windows系统常用中文字体
    chinese_fonts = [
        'simhei.ttf',       # 黑体
        'msyh.ttc',         # 微软雅黑
        'simsun.ttc',       # 宋体
        'STSONG.TTF',       # 华文宋体
        'C:/Windows/Fonts/simhei.ttf',  # Windows完整路径
    ]
    
    # 尝试加载字体
    font1 = None
    font2 = None
    
    # 尝试所有可能的字体路径
    all_fonts = chinese_fonts
    
    for font_path in all_fonts:
        try:
            font1 = pygame.font.Font(font_path, 40)
            font2 = pygame.font.Font(font_path, 24)
            print(f"成功加载字体: {font_path}")
            break
        except:
            continue
    
    # 如果所有字体都加载失败，使用默认字体并提示
    if font1 is None:
        print("警告：无法加载中文字体，将使用默认字体（可能无法显示中文）")
        font1 = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 24)
    

    # 加载问答数据文件
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, "trivia_data.txt")
    trivia = Trivia(file)

    # 游戏主循环
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == QUIT:  # 退出事件
                sys.exit()
            elif event.type == KEYUP:  # 键盘松开事件
                if event.key == pygame.K_ESCAPE:  # ESC键退出
                    sys.exit()
                elif trivia.game_over:  # 游戏结束时只处理1和2
                    if event.key == pygame.K_1:
                        trivia.handle_input(1)
                    elif event.key == pygame.K_2:
                        trivia.handle_input(2)
                elif event.key == pygame.K_1:     # 数字键1选择选项1
                    trivia.handle_input(1)
                elif event.key == pygame.K_2:     # 数字键2选择选项2
                    trivia.handle_input(2)
                elif event.key == pygame.K_3:     # 数字键3选择选项3
                    trivia.handle_input(3)
                elif event.key == pygame.K_4:     # 数字键4选择选项4
                    trivia.handle_input(4)
                elif event.key == pygame.K_RETURN:  # 回车键进入下一题
                    trivia.next_question()

        # 清空屏幕（蓝色背景）
        screen.fill(Colors['hailan'])

        # 显示当前问答内容
        trivia.show_question()
        
        # 更新显示
        pygame.display.update()