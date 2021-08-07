# Date: 05.08.2021
# Author: Lev Dolgikh

# Новое графическое окно
# Демонстрирует создание графического окна

import pygame

WIDTH = 640
HEIGHT = 480
running = True

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("Новое графическое окно")

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = false
