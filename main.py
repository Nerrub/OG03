import pygame
import random
pygame.init()

SCREEN_WIGHT=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon=pygame.image.load("img/4c9255d3-aade-4db4-87d2-9054fd5d4093.jpg")
pygame.display.set_icon(icon)

target_img=pygame.image.load("img/klipartz.com(1).png")
target_weight=80
target_height=80

target_x=random.randint(0,SCREEN_WIGHT-target_weight)
target_y=random.randint(0,SCREEN_HEIGHT-target_height)

color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

running= True

while running:
    pass

pygame.quit()
