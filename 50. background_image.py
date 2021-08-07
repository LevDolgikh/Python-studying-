# Date: 07.08.2021
# Author: Lev Dolgikh

# Фоновая картинка
# Демонстрирует назначение фоновой картинки для графического экрана

import pygame

# Константы
WINDOW_NAME = "Фоновая картинка"
WIDTH = 640
HEIGHT = 480
FPS = 60

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установка фона
bgdImage = pygame.image.load("50. background_image.jpg")
screen.blit(bgdImage,(0,0))

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
        
