# Date: 20.08.2021
# Author: Lev Dolgikh

# Звук и музыка
# Демонстрирует воспроизведение звуков и музыкальных файлов
# Управление программой из консоли
# Убедитесь, что файлы 60. music.wav и 60. rocket_launch находятся в папке с игрой

import pygame

# Константы
WINDOW_NAME = "Музыка и звук"
WIDTH = 640
HEIGHT = 480
BACKGROUND_POS = (0,0)
FPS = 15 # Специально поменьше, что бы не вводить переменные времени, ибо цель программы - отработать способ введения анимации
WHITE = (255,255,255)
BLACK = (0,0,0)

# Инициализация
pygame.init()
# Установа заголовка программы
pygame.display.set_caption(WINDOW_NAME)
# Задание размеров
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Загрузка белый фон
screen.fill(WHITE)
# Загрузка музыки и звуков
pygame.mixer.music.load("60. music.wav")
rocket_launch = pygame.mixer.Sound("60. rocket_launch.wav")
# Обновление экрана
pygame.display.flip()

# Переменаня цикла
running = True
frames = pygame.time.Clock()

# Запуск цикла событий
while running:
    # Делаем что бы консолька работала
    choise = ""
    print("""
    Звук и музыка:

    0 - Выйти
    1 - Воспроизвести звук ракетного залпа
    2 - Воспроизвести музыкальную тему игры
    3 - Циклировать музыкальную тему игры
    4 - Остановить музыкальную тему игры

    """)
    
    while choise not in range(0,5):
        choise = int(input("Ваш выбор: "))

    if choise == 0:
        pygame.quit()
    elif choise == 1:
        rocket_launch.play()
    elif choise == 2:
        pygame.mixer.music.play(0)
    elif choise == 3:
        pygame.mixer.music.play(-1)
    elif choise == 4:
        pygame.mixer.music.stop()
        
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
