# Date: 07.08.2021
# Author: Lev Dolgikh

# Спрайт
# Демонстрирует создание спрайте

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
bgdImage = pygame.image.load("51. background_image.jpg")
screen.blit(bgdImage,(0,0))
# Загрузка и установка спрайта
sprite = pygame.image.load("51. sprite.png") # Нормальную картинку пытался загрузить но он ее плохо обрабатывает
sprite.set_colorkey((255,0,255))
screen.blit(sprite,(140,320))

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
        
