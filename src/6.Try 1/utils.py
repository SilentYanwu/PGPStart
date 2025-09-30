# utils.py
# 工具函数模块

import math
import pygame

def print_text(font, x, y, text, color=(255,255,255)):
    """在屏幕上绘制文本"""
    imgText = font.render(text, True, color)  # 渲染文本为图像
    return imgText, (x, y)  # 返回文本图像和位置

def wrap_angle(angle):
    """将角度限制在0-360度范围内"""
    return angle % 360

def rotate_ship(ship_image, delta_x, delta_y):
    """根据运动方向旋转飞船"""
    rangle = math.atan2(delta_y, delta_x)  # 计算运动方向的角度（弧度）
    rangled = wrap_angle(-math.degrees(rangle))  # 转换为角度并包装
    rotated_ship = pygame.transform.rotate(ship_image, rangled)  # 旋转飞船图像
    return rotated_ship