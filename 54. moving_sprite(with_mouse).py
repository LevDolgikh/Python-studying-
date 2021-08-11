# Date: 11.08.2021
# Author: Lev Dolgikh

# Соударение объектов
# Демонстрирует соударение объектов

import pygame

# Константы
WINDOW_NAME = "Движение спрайта"
WIDTH = 640
HEIGHT = 480
BACKGROUND_POS = (0,0)
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)

# Позиция спайта
BACKGR = 300
ypos = 50

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установка фона
screen.fill((255,255,255))
# Загрузка спрайтов
background = pygame.image.load("54. back.bmp")
screen.blit(background,BACKGROUND_POS)
fairy = pygame.image.load("54. fairy.bmp")
fairy.set_colorkey(BLACK)
screen.blit(fairy,(xpos,ypos))
wand = pygame.image.load("54. wand.bmp")
wand.set_colorkey(WHITE)
screen.blit(wand,(300,200))



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
        # Получение данных с мыши (просто вставляем координаты мыши в координаты спрайта)
        xpos, ypos = pygame.mouse.get_pos()
        screen.blit(background,(0,0))
        screen.blit(fairy,(xpos-30,ypos-30))
        screen.blit(wand,(300,200))
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()
            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
