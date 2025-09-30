# circle_effect.py
# 圆形特效模块（基于1号代码）

import random, math, pygame

class CircleEffect:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pos_x = screen_width // 2
        self.pos_y = screen_height // 2
        self.radius = 200
        self.angle = 360
        self.color = (255, 255, 255)
        self.active = False
        self.start_time = 0
        self.duration = 3000  # 3秒
    
    def start(self, current_time):
        """启动特效"""
        self.active = True
        self.start_time = current_time
        self.angle = 360
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    def update(self, current_time):
        """更新特效"""
        if not self.active:
            return False
        
        # 检查是否超过持续时间
        if current_time - self.start_time > self.duration:
            self.active = False
            return False
        
        # 角度递增
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
        return True
    
    def draw(self, screen):
        """绘制特效"""
        if not self.active:
            return
        
        # 计算圆形轨迹上的坐标
        x = math.cos(math.radians(self.angle)) * self.radius
        y = math.sin(math.radians(self.angle)) * self.radius
        
        # 在圆形轨迹上绘制一个点
        pos = (int(self.pos_x + x), int(self.pos_y + y))
        pygame.draw.circle(screen, self.color, pos, 10, 0)