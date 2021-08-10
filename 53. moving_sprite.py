# Date: 10.08.2021
# Author: Lev Dolgikh

# Движужийся спрайт
# Демонстрирует движение спрайта

import pygame

# Константы
WINDOW_NAME = "Движение спрайта"
WIDTH = 640
HEIGHT = 480
FPS = 60
WHITE = (255,255,255)

# Позиция спайта
xpos = 300
ypos = 220
# Перемещение спрайта
dx = 5
dy = 5

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установка фона
screen.fill((255,255,255))
# Установка зугрузка спрайта
sprite = pygame.image.load("53. sprite.png")
sprite.set_colorkey((255,0,255))
screen.blit(sprite,(xpos,ypos))

# Обновление экрана
pygame.display.flip()

# Переменаня цикла
running = True
frames = pygame.time.Clock()

# Запуск цикла событий
while running:
    # Обновление дисплея
    pygame.display.update()
    # Проверка на то, вышел ли спрайт за границы экрана
    if xpos > WIDTH-64 or xpos < 0:
        dx = -dx
    if ypos > HEIGHT-64 or ypos < 0:
        dy = -dy
    # Изменение позиции спрйта
    xpos += dx
    ypos += dy
    # Обновление позиции спрайта не экране
    screen.fill((255,255,255))
    screen.blit(sprite, (xpos, ypos))
    # Для каждого события
    for event in pygame.event.get():
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()
            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
