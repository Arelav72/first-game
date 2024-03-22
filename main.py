import pygame
import random
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Размер окна

pygame.display.set_caption("Игра Тир") # Заголовок окна
icon = pygame.image.load('image/icon.jpg') # Путь к изображению
pygame.display.set_icon(icon) # Иконка окна


target = pygame.image.load('image/target.png') # Путь к изображению мишени
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width) #  координаты мишени по Х
target_y = random.randint(0, SCREEN_HEIGHT - target_height) #  координаты мишени по У

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) # цвет фона



running = True
while running:
    pass


pygame.quit()