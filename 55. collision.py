# Date: 11.08.2021
# Author: Lev Dolgikh

# Соударение объектов
# Демонстрирует соударение объектов

import math
import random
import pygame

# Константы
WINDOW_NAME = "Соударения спрайтов"
WIDTH = 640
HEIGHT = 480
BACKGROUND_POS = (0,0)
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)

# Позиции и размеры спрайтов
fairy_XPOS = 300
fairy_YPOS = 50
fairy_H = 140
fairy_W = 150
wand_XPOS = 300
wand_YPOS = 200
wand_H = 64
wand_W = 64


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
screen.blit(fairy,(fairy_XPOS,fairy_YPOS))
wand = pygame.image.load("54. wand.bmp")
wand.set_colorkey(WHITE)
screen.blit(wand,(wand_XPOS,wand_YPOS))



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
        fairy_XPOS, fairy_YPOS = pygame.mouse.get_pos()
        screen.blit(background,(0,0))
        screen.blit(wand,(wand_XPOS,wand_YPOS))
        screen.blit(fairy,(fairy_XPOS-fairy_W/2,fairy_YPOS-fairy_H/2))
        # Определение соударения (на основе расстояния между центрами спрайтов)
        fairyCenter = (fairy_XPOS-fairy_W/2,fairy_YPOS-fairy_H/2)
        wandCenter = (wand_XPOS-wand_W/2,wand_YPOS-wand_H/2)
        D = math.sqrt((fairyCenter[0]-wandCenter[0])**2 + (fairyCenter[1]-wandCenter[1])**2)
        minD = fairy_H/2 + wand_H/2
        if D < minD:
            wand_XPOS = random.randrange(0,WIDTH-60)
            wand_YPOS = random.randrange(0,HEIGHT-60)
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()
            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
