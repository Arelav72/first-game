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
  screen.fill(color)  # pандомная заливка окна
  screen.blit(target, (target_x, target_y))  # мишение
  pygame.display.update() # Обновление окна
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
        # pygame.mixer.Sound.play(pygame.mixer.Sound('sound/click.wav'))
        target_x = random.randint(0, SCREEN_WIDTH - target_width) #  координаты мишени по Х
        target_y = random.randint(0, SCREEN_HEIGHT - target_height) #  координаты мишени по У
  screen.blit(target, (target_x, target_y)) # отображаем мишень на экране игры

  pygame.display.update() # Обновление окна


pygame.quit()