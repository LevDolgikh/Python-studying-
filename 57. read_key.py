# Date: 17.08.2021
# Author: Lev Dolgikh

# Читаю с клавиатуры
# Демонстрирует чтение клавиатурного ввода

import pygame

# Константы
WINDOW_NAME = "Читаю с клавиатуры"
WIDTH = 640
HEIGHT = 480
BACKGROUND_POS = (0,0)
FPS = 60
WHITE = (247,247,247)
BLACK = (0,0,0)

# Позиция корабля
xpos = WIDTH/2-50
ypos = HEIGHT/2-50

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Загрузка спрайтов
background = pygame.image.load("57. background.bmp")
screen.blit(background,BACKGROUND_POS)
spaceship = pygame.image.load("57. spaceship.bmp")
spaceship.set_colorkey(WHITE)
screen.blit(spaceship,(xpos,ypos))

# Обновление экрана
pygame.display.flip()

# Переменаня цикла
running = True
frames = pygame.time.Clock()

# Запуск цикла событий
while running:
    # Если кнопка нажата, то двигаем кораблик
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [pygame.K_a]:
        xpos -= 1
    if pressed_keys [pygame.K_w]:
        ypos -= 1
    if pressed_keys [pygame.K_d]:
        xpos += 1
    if pressed_keys [pygame.K_s]:
        ypos += 1
    # Обновляем картинки
    screen.blit(background,BACKGROUND_POS)
    screen.blit(spaceship,(xpos,ypos))
    # Обновление дисплея
    pygame.display.update()
    # Для каждого события
    for event in pygame.event.get():
        # Получение данных с клавиатуры (Одиночные нажатия)
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_a:
        #        xpos -= 1
        #    if event.key == pygame.K_w:
        #       ypos -= 1
        #    if event.key == pygame.K_d:
        #        xpos += 1
        #    if event.key == pygame.K_s:
        #        ypos += 1
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()

            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
