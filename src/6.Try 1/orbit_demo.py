# orbit_demo.py
# 轨道演示主模块

import sys
import math
import pygame
from pygame.locals import *

from point import Point
from utils import print_text, wrap_angle, rotate_ship
from resources import ResourceManager
from button import Button
from circle_effect import CircleEffect

class OrbitDemo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Orbit Demo")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 18)
        
        # 初始化资源管理器
        self.resources = ResourceManager()
        
        # 初始化按钮
        self.button1 = Button(650, 100, 120, 40, "EA", self.font)
        self.button2 = Button(650, 160, 120, 40, "VE", self.font)
        
        # 初始化圆形特效
        self.circle_effect = CircleEffect(800, 600)
        
        # 初始化飞船状态
        self.mode = 1  # 1: 太极绕行, 2: 垂直飞行
        self.radius1 = 250  # 飞船1轨道半径
        self.radius2 = 250  # 飞船2轨道半径
        self.angle1 = 0.0   # 飞船1当前角度
        self.angle2 = 180.0 # 飞船2当前角度（镜像）
        self.pos1 = Point(0, 0)
        self.pos2 = Point(0, 0)
        self.old_pos1 = Point(0, 0)
        self.old_pos2 = Point(0, 0)
        
        # 飞船缩放
        self.ship1_scale = 1.0
        self.ship2_scale = 1.0
    def handle_events(self):
        """处理事件"""
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    mouse_click = True
        
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return False
        
        # 更新按钮状态
        mouse_pos = pygame.mouse.get_pos()
        if self.button1.update(mouse_pos, mouse_click):
            self.mode = 1
            self.radius2 = 250
            self.ship2_scale = 1
            self.button1.reset_click()
        
        if self.button2.update(mouse_pos, mouse_click):
            self.mode = 2
            self.circle_effect.start(pygame.time.get_ticks())
            self.button2.reset_click()
        
        return True
    
    def update_ships(self):
        """更新飞船位置和状态"""
        current_time = pygame.time.get_ticks()
        
        # 模式2的特殊处理：圆形特效
        if self.mode == 2:
            if self.circle_effect.update(current_time):
                # 特效期间保持原有运动
                self.angle1 = wrap_angle(self.angle1 - 0.1)
                self.angle2 = wrap_angle(self.angle2 - 0.1)
            else:
                # 特效结束后切换到垂直飞行模式
                self.radius2 = 200
                self.ship2_scale = 0.6  # 飞船2缩小
                self.angle1 = wrap_angle(self.angle1 - 0.1)
                self.angle2 = self.angle1  # 相同角度
        else:
            # 模式1：太极绕行
            self.angle1 = wrap_angle(self.angle1 - 0.1)
            self.angle2 = wrap_angle(self.angle2 - 0.1)
        
        # 计算飞船位置
        self.pos1.x = math.sin(math.radians(self.angle1)) * self.radius1
        self.pos1.y = math.cos(math.radians(self.angle1)) * self.radius1
        
        self.pos2.x = math.sin(math.radians(self.angle2)) * self.radius2
        self.pos2.y = math.cos(math.radians(self.angle2)) * self.radius2
    
    def draw(self):
        """绘制游戏场景"""
        # 绘制背景
        self.screen.blit(self.resources.space, (0, 0))
        
        # 绘制行星
        width, height = self.resources.planet.get_size()
        self.screen.blit(self.resources.planet, (400 - width/2, 300 - height/2))
        
        # 绘制圆形特效（如果激活）
        self.circle_effect.draw(self.screen)
        
        # 计算飞船旋转
        delta_x1 = (self.pos1.x - self.old_pos1.x)
        delta_y1 = (self.pos1.y - self.old_pos1.y)
        delta_x2 = (self.pos2.x - self.old_pos2.x)
        delta_y2 = (self.pos2.y - self.old_pos2.y)
        
        # 旋转飞船
        rotated_ship1 = rotate_ship(
            self.resources.resize_ship(1, self.ship1_scale), 
            delta_x1, delta_y1
        )
        rotated_ship2 = rotate_ship(
            self.resources.resize_ship(2, self.ship2_scale), 
            delta_x2, delta_y2
        )
        
        # 绘制飞船1
        width1, height1 = rotated_ship1.get_size()
        x1 = 400 + self.pos1.x - width1 // 2
        y1 = 300 + self.pos1.y - height1 // 2
        self.screen.blit(rotated_ship1, (x1, y1))
        
        # 绘制飞船2
        width2, height2 = rotated_ship2.get_size()
        x2 = 400 + self.pos2.x - width2 // 2
        y2 = 300 + self.pos2.y - height2 // 2
        self.screen.blit(rotated_ship2, (x2, y2))
        
        # 绘制按钮
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        
        # 显示调试信息
        debug_info = [
            f"Mode: {self.mode}",
            f"Ship1 Orbit: {self.angle1:.0f}",
            f"Ship2 Orbit: {self.angle2:.0f}",
            f"Ship1 Position: {self.pos1}",
            f"Ship2 Position: {self.pos2}",
            f"Ship1 Radius: {self.radius1}",
            f"Ship2 Radius: {self.radius2}"
        ]
        
        for i, text in enumerate(debug_info):
            imgText, pos = print_text(self.font, 0, i * 20, text)
            self.screen.blit(imgText, pos)
        
        pygame.display.update()
        
        # 记录当前位置作为下一帧的"旧位置"
        self.old_pos1.x = self.pos1.x
        self.old_pos1.y = self.pos1.y
        self.old_pos2.x = self.pos2.x
        self.old_pos2.y = self.pos2.y
    
    def run(self):
        """运行游戏主循环"""
        running = True
        while running:
            running = self.handle_events()
            self.update_ships()
            self.draw()
            self.clock.tick(60)  # 限制帧率为60FPS

if __name__ == "__main__":
    demo = OrbitDemo()
    demo.run()