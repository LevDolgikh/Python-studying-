# Date: 10.08.2021
# Author: Lev Dolgikh

# Текст
# Демонстрирует отображение текста на экране

import pygame

# Константы
WINDOW_NAME = "Текст"
WIDTH = 640
HEIGHT = 480
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установка фона
screen.fill((255,255,255))
# Установка текста на экран
    # Текст со счетом
font = pygame.font.SysFont("Arial", 20)
score = font.render("1233456", True, BLACK)
screen.blit(score,(550,20-10))
    # Текст GAME OVER
title = pygame.font.SysFont("Arial", 50)
score = title.render("GAME OVER", True, RED)
screen.blit(score,(WIDTH/2-15*9,HEIGHT/2-25))


# Обновление экрана
pygame.display.flip()

# Переменаня цикла
running = True
frames = pygame.time.Clock()

# Запуск цикла событий
while running:
    # Обновление дисплея
    pygame.display.update()
    # Для каждого события
    for event in pygame.event.get():
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()
            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
