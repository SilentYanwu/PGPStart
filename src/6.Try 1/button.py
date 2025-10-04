# button.py
# 按钮类模块

import pygame

class Button:
    def __init__(self, x, y, width, height, text, font, normal_color=(100, 100, 200), 
                 hover_color=(150, 150, 255), text_color=(255, 255, 255)):
        # Rect(left, top, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.normal_color = normal_color # 正常状态
        self.hover_color = hover_color # 悬停状态
        self.text_color = text_color # 文字颜色
        self.is_hovered = False
        self.clicked = False
    
    def draw(self, screen):
        """绘制按钮"""
        # 三元运算符 color先判断是否是悬停状态
        color = self.hover_color if self.is_hovered else self.normal_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)  # 白色边框
        
        # 绘制文本
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def update(self, mouse_pos, mouse_click):
        """更新按钮状态"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        if self.is_hovered and mouse_click:
            self.clicked = True
            return True
        return False
    
    def reset_click(self):
        """重置点击状态"""
        self.clicked = False