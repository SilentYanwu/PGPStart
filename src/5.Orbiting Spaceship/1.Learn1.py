import sys, random, math, pygame
from pygame.locals import *
from pathlib import Path

# main
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbiting Demo")

# 直接构建图片路径
space_path = Path(__file__).parent / "Res" / "space.png"
ship_path = Path(__file__).parent / "Res" / "freelance.png"
planet_path = Path(__file__).parent / "Res" / "planet2.png"

try:
    space = pygame.image.load(str(space_path)).convert()
    planet= pygame.image.load(str(planet_path)).convert_alpha()
    ship= pygame.image.load(str(ship_path)).convert_alpha()
    print("图片加载成功!")
except:
    print("图片加载失败，使用黑色背景")
    space = pygame.Surface((800, 600))
    space.fill((0, 0, 0))

clock = pygame.time.Clock()
# 缩小飞船(放在循环外)
width,height = ship.get_size()
ship=pygame.transform.smoothscale(ship, (width//2, height//2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
    

    screen.blit(space, (0, 0))
    width,height = planet.get_size()
    screen.blit(planet, (400-width//2, 300-height//2))

    screen.blit(ship,(50,50))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()