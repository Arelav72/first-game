import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Размер окна

pygame.display.set_caption("Игра Тир")  # Заголовок окна
icon = pygame.image.load('image/icon.jpg')  # Путь к изображению
pygame.display.set_icon(icon)  # Иконка окна

target = pygame.image.load('image/target.png')  # Путь к изображению мишени
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)  # координаты мишени по X
target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # координаты мишени по Y
target_speed_x = 0.25  # Скорость мишени по горизонтали
target_speed_y = 0.25  # Скорость мишени по вертикали

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # цвет фона

# Добавляем переменную для подсчета очков
score = 0
font = pygame.font.Font(None, 35)

running = True
while running:
    screen.fill(color)  # случайная заливка окна

    # Обновляем координаты мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверяем столкновение с краями экрана
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_speed_x = -target_speed_x
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_speed_y = -target_speed_y

    screen.blit(target, (target_x, target_y))  # мишень

    # Отображение счета
    score_surface = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    pygame.display.update()  # Обновление окна

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                # pygame.mixer.Sound.play(pygame.mixer.Sound('sound/click.wav'))
                score += 1  # Увеличиваем счет
                # Для увеличения сложности можно ускорить мишень
                target_speed_x += 0.25 if target_speed_x > 0 else -1  # Увеличение скорости по X
                target_speed_y += 0.25 if target_speed_y > 0 else -1  # Увеличение скорости по Y

pygame.quit()