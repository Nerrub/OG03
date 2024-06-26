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

font = pygame.font.Font(None, 36)
hits=0

target_x=random.randint(0,SCREEN_WIGHT-target_weight)
target_y=random.randint(0,SCREEN_HEIGHT-target_height)

color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

running= True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_weight and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIGHT - target_weight)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1
    screen.blit(target_img, (target_x,target_y))
    hit_text=font.render(f'Попадания: {hits}', True, (255,255,255))
    screen.blit(hit_text, (10,10))
    pygame.display.update()

pygame.quit()
