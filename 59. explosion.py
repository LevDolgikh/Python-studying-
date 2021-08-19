# Date: 19.08.2021
# Author: Lev Dolgikh

# Взрыв
# Демонстрирует создание анимации

import pygame

# Константы
WINDOW_NAME = "Анимация взрыва"
WIDTH = 640
HEIGHT = 480
BACKGROUND_POS = (0,0)
FPS = 15 # Специально поменьше, что бы не вводить переменные времени, ибо цель программы - отработать способ введения анимации
WHITE = (255,255,255)
BLACK = (0,0,0)

# Позиция корабля
xpos = WIDTH/2-50
ypos = HEIGHT/2-50
angle = 0

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Загрузка спрайтов
background = pygame.image.load("58. background.bmp")
screen.blit(background,BACKGROUND_POS)
asteroid = pygame.image.load("59. asteroid1.bmp")
asteroid.set_colorkey(WHITE)
screen.blit(asteroid,(xpos,ypos))
asteroidDestructionAnimation = []
for i in range(1,4):
    fileName = "59. destruction" + str(i) + ".bmp"
    animation = pygame.image.load(fileName)
    animation.set_colorkey(WHITE)
    asteroidDestructionAnimation.append(animation) # наполняем список картинками с анимацией

# Обновление экрана
pygame.display.flip()

# Переменаня цикла
running = True
asteroidDestroyed = False # Переменная, отображающая уничтожен ли астероид или нет
asteroidDestrustionPhase = 0 # Отображает номер фазы анимации
currentAsteroid = asteroid # Содержит изображение текущего атеройда (его фазы уничножения)
frames = pygame.time.Clock()

# Запуск цикла событий
while running:
    # Обновляем картинки (реализация анимации)
    if asteroidDestroyed == True:
        if asteroidDestrustionPhase == 3:
            asteroidDestrustionPhase = 0
            asteroidDestroyed = False
            currentAsteroid = asteroid
        else:
            currentAsteroid = asteroidDestructionAnimation[asteroidDestrustionPhase]
            asteroidDestrustionPhase += 1
    screen.blit(background,BACKGROUND_POS)
    screen.blit(currentAsteroid,(xpos,ypos))
    # Обновление дисплея
    pygame.display.update()
    # Для каждого события
    for event in pygame.event.get():
        # Получение данных с клавиатуры (Одиночные нажатия), если 1 - анимируется уничтожение 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                asteroidDestroyed = True
        # Если событие - выход
        if event.type == pygame.QUIT:
            # Закрываем программу
            running = False
            pygame.quit()

            
    # Определяем частоту обновлений
    frames.tick(FPS)
        
