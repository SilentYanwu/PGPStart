# resources.py
# 资源管理模块

import pygame
from pathlib import Path

class ResourceManager:
    def __init__(self):
        self.space = None
        self.planet = None
        self.ship1 = None
        self.ship2 = None
        self.load_resources()
    
    def load_resources(self):
        """加载所有游戏资源"""
        # 直接构建图片路径
        base_path = Path(__file__).parent
        
        # 加载位图
        space_path = base_path / "Res" / "space.png"
        planet_path = base_path / "Res" / "planet2.png"
        ship1_path = base_path / "Res" / "freelance.png"
        ship2_path = base_path / "Res" / "military.png"
        
        self.space = pygame.image.load(str(space_path)).convert_alpha()
        self.planet = pygame.image.load(str(planet_path)).convert_alpha()
        
        # 加载飞船并调整大小
        ship1_original = pygame.image.load(str(ship1_path)).convert_alpha()
        ship2_original = pygame.image.load(str(ship2_path)).convert_alpha()
        
        # 调整飞船大小 - 缩小为原来的一半
        width1, height1 = ship1_original.get_size()
        width2, height2 = ship2_original.get_size()
        
        self.ship1 = pygame.transform.smoothscale(ship1_original, (width1//2, height1//2))
        self.ship2 = pygame.transform.smoothscale(ship2_original, (width2//2, height2//2))
    
    def resize_ship(self, ship_type, scale_factor):
        """根据缩放因子调整飞船大小"""
        if ship_type == 1:
            original_size = self.ship1.get_size()
            new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
            return pygame.transform.smoothscale(self.ship1, new_size)
        else:
            original_size = self.ship2.get_size()
            new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
            return pygame.transform.smoothscale(self.ship2, new_size)