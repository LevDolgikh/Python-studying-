# Date: 12.08.2021
# Author: Lev Dolgikh

# Паника в лесу
# Игрок должен ловить падающую палочку, пока она не достигла земли
# Выбор спрайтов для данный игры был случайным, были взяты первые попавшиеся картинки одинаковой тематики
# оригинальные спрайты по книге Майкла Доусона не нашел... Собственно и модуль livewires не хочет работать... поэтому Pygames

import sys
import math
import random
import pygame

class Sprite(object):
    """Класс спрайтов"""
    def __init__(self, imgDIR, centerX, centerY):
        """Инициализация класса"""
        self.dir = imgDIR
        self.image = pygame.image.load(imgDIR)
        self.centerX = centerX
        self.centerY = centerY
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def __str__(self):
        """Выводит директорию картинки"""
        rep = self.dir
        return rep

    def blit(self, screen):
        """Помещает изображение на экран"""
        startX = self.centerX - self.width/2
        startY = self.centerY - self.height/2
        screen.blit(self.image,(startX, startY))

    def setColorKey(self, color):
        """Устанавливает значение цвета, который становиться прозрачным на спрайте"""
        self.image.set_colorkey(color)

    def getXY(self):
        """Передает значения координат спрайта"""
        return self.centerX, self.centerY

    def setX(self, x):
        """Устанавливает значение цента спрайта по ширине"""
        self.centerX = x

    def setY(self, y):
        """Устанавливает значение цента спрайта по высоте"""
        self.centerY = y

    def getHeight(self):
        """Возвращает высоту спрайта"""
        return self.height

class GameScore(object):

    WHITE = (255, 255, 255)
    RED = (236, 28, 36)
    BLACK = (0, 0, 0)
    
    """Счет игры"""
    def __init__(self, centerX, centerY):
        """Инициализация класса"""
        self.score = 0
        self.centerX = centerX
        self.centerY = centerY
        self.scorePerCatch = 10
        self.font = pygame.font.SysFont("Times New Roman", 30)

    def __str__(self):
        """Возвращает счет игры"""
        rep = "Счет игры: " + str(self.score)
        return rep
        
    def blit(self, screen):
        """Вывод счета на экран"""
        startX = self.centerX - 30
        startY = self.centerY - 30
        score = self.font.render(str(self.score), True, self.WHITE)
        screen.blit(score,(startX, startY))

    def addScore(self):
        """Увеличение счета"""
        self.score += self.scorePerCatch

    def resetScore(self):
        """Обнуление счета"""
        self.score = 0

    def getScore(self):
        """Возвращает текущий счет"""
        return self.score
        
        

class ForestPanic(object):
    """Класс под игру паника в лесу"""

    # Создание констант
    WINDOW_NAME = "Паника в лесу"
    WIDTH = 640
    HEIGHT = 480
    BACKGROUND_POS = (0, 0)
    FPS = 60
    BACKGROUND_DIR = "56. back.bmp"
    WAND_DIR = "56. wand.bmp"
    FAIRY_DIR = "56. fairy.bmp"
    GIRL_DIR = "56. girl.bmp"
    WHITE = (255, 255, 255)
    RED = (236, 28, 36)
    BLACK = (0, 0, 0)

    def __init__(self):
        """Инициализация программы"""

        # Инициализация
        pygame.init()

        # Установа заголовка программы
        pygame.display.set_caption(self.WINDOW_NAME)

        # Задание размеров
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Инициализция спрайтов
        # Фон
        try:
            self.background = Sprite(self.BACKGROUND_DIR, self.WIDTH/2, self.HEIGHT/2)
            self.background.blit(self.screen)
            # Фея
            self.fairy = Sprite(self.FAIRY_DIR, self.WIDTH/2, 70)
            self.fairy.setColorKey(self.BLACK)
            self.fairy.blit(self.screen)
            # Ловец
            self.catcher = Sprite(self.GIRL_DIR, self.WIDTH/2, 420)
            self.catcher.setColorKey(self.RED)
            self.catcher.blit(self.screen)
        except:
            # В случае ошибки выводит в концоль причину ошибки (отсутствие картинок)
            print("Не удается найти изображения к игре, убедитесь что в папке с игрой присутствуют изображения" + \
                  "56. back.bmp, 56. wand.bmp, 56. fairy.bmp, 56. girl.bmp")
            # Выход и закрытие программы (игра без картинок работать не будет)
            pygame.quit()
            sys.exit(0)

        # Счет игры
        self.score = GameScore(580,30)
        self.score.blit(self.screen)

        # Обновление экрана
        pygame.display.flip()

        # Переменная под движение верхнего спрайта
        self.destination = 0

        # Переменные времени
        self.frames = pygame.time.Clock()
        self.fairyTimer = 0
        self.wandTimer = 0

        # Переменная под падающие объекты
        self.wands = []

        # Запуск игры
        self.__startGame()

    def __str__(self):
        """Вывод информации о игре"""
        rep = "Игра 'Паника в лесу', вам нужно ловить падающие сверху палочки, перемещая персонажа находящегося внизу экрана"
        return rep

    def __startGame(self):
        """Основной цикл игры"""

        # Переменные
        # Переменные отвечающая за работу игрового цикла
        running = True
        # Переменная, содержащая информцию об падающих объектах
        wands = []
        # Переменная содержащая информацию о том, были ли доведены инструкции до игрока или нет
        instructed = 0

        # Основной цикл игры
        while running:

            # Если иструкции доведены
            if instructed:
                # Проверяет, что с момента последнего движения фейки и палочек прошло более 10 милисекунд
                if (pygame.time.get_ticks() - self.fairyTimer) > 10:
                    # Осуществляет движение фейки
                    self.__moveFairy()
                    # Осуществляет дживение палочек
                    self.__moveWands()
                    # Обновляет таймер
                    self.fairyTimer = pygame.time.get_ticks()
                # Двигает персонажа-ловца в координату мыши игрока
                self.__moveCatcher()
                # Проверяет, что с момента последнего движения фейки и палочек прошло более 2 секунд
                if (pygame.time.get_ticks() - self.wandTimer) > 2000:
                    # Генерирует палочку
                    self.wands.append(self.__generateWand())
                    # Обновляет таймер
                    self.wandTimer = pygame.time.get_ticks()
                # Проверяет поймал ли игрок палочку или вышла ли палочка за границы игрового окна
                self.__checkCollisions()
                # Проверяет победил ли игрок по счету
                self.__checkScore()
                # Отрисовыват все спрайты
                self.__blitAll()
            else:
                # Если инструкции не были доведены, то доводит инструкции
                self.__instuctions()

            # Обновление экрана
            pygame.display.update()

            # Проверка на то, были ли какие-то события
            for event in pygame.event.get():
                # Если игрок закрыл окно - то закрываем программу
                if event.type == pygame.QUIT:
                    # Закрываем программу
                    running = False
                    pygame.quit()

                # Если игрок во время инструктажа нажал любую кнопку мыши, начинает игру
                if event.type == pygame.MOUSEBUTTONDOWN and instructed == 0:
                    instructed = 1

        # Определяет обновление кадров игры
        self.frames.tick(self.FPS)

    def __moveFairy(self):
        """Перемещение спрайта скидывающего палочки"""
        # Переменная шага перемещения
        moveValue = 1

        # Получение данных о текущих координатах фейки
        fairyX, fairyY = self.fairy.getXY()

        # Генерируется координата в которую фейка должна прибыть
        if self.destination == 0 or fairyX == self.destination:
            self.destination = random.randrange(50,600,10)
        # Движение фейки к сгенерированной координате
        if fairyX > self.destination:
            self.fairy.setX(fairyX-moveValue)
        elif fairyX < self.destination:
            self.fairy.setX(fairyX+moveValue)

    def __moveCatcher(self):
        """Перемещения игрока-ловца в положение мыши"""
        xpos, ypos = pygame.mouse.get_pos()
        self.catcher.setX(xpos)

    def __generateWand(self):
        """Генерация палочки под фейкой"""
        fairyX , fairyY = self.fairy.getXY()
        wand = Sprite(self.WAND_DIR, fairyX, 150)
        wand.setColorKey(self.WHITE)
        return wand

    def __moveWands(self):
        """Движение палочек под действием гравитации (вниз)"""
        # Законы физики не совсем соблюдаются, т.к. у палочек должна сохраняется скорость по координате Х от фейки, но в такой игре в этом мало смысла
        move = 1
        for wand in self.wands:
            wandX, wandY = wand.getXY()
            wand.setY(wandY+move)

    def __checkCollisions(self):
        """Проверка на соударения игрока-ловца и палочки, а также выхода палочки за игровой экран"""

        # Переменные
        lost = False
        lostIndex = None
        collisionIndex = None
        catcherHeight = self.catcher.getHeight()

        # Проверка вышла ли палочка за границы экрана
        if self.wands:
            for i in range(len(self.wands)):
                wandX, wandY = self.wands[i].getXY()
                wandHeight = self.wands[i].getHeight()

                if wandX > self.WIDTH or wandY > self.HEIGHT:
                    lost = True
                    lostIndex = i
                    # Если вышла, то поражение
                    self.__youWonOrLost("Поражение")

            if lostIndex != None:
                # Удаляет вышедшие палочки за граници экрана (использовалось при отладке, в самой игре не нужно)
                del self.wands[:lostIndex]

            # Проверяет на соударения палочек и игрока-ловца на основе расчета дистанции между центрами палочек и игрока-ловца, если это значение меньши суммы полувысот спрайтов, то соударение произошло
            for i in range(len(self.wands)):
                
                wandX, wandY = self.wands[i].getXY()
                wandHeight = self.wands[i].getHeight()
                
                distance = self.__calcDistanceToCatcher(wandX, wandY)

                if int(distance) < int(catcherHeight/2+wandHeight/2):
                    collisionIndex = i

            # Если было соударение, то удаляет палочку и увеличивает счет игрока
            if collisionIndex != None:
                del self.wands[collisionIndex]
                self.score.addScore()

    def __calcDistanceToCatcher(self, objectX, objectY):
        """Расчет расстояния между палочкой и игроком-ловцом"""
        catcherX, catcherY = self.catcher.getXY()
        distance = math.sqrt((catcherX-objectX)**2+(catcherY-objectY)**2)
        return distance       
 
    def __blitAll(self):
        """Помещения всех спрайтов на экран"""
        self.background.blit(self.screen)
        self.fairy.blit(self.screen)
        self.catcher.blit(self.screen)
        self.score.blit(self.screen)
        for wand in self.wands:
            wand.blit(self.screen)

    def __checkScore(self):
        """Проверка счета на привышение победного значения"""
        if self.score.getScore() >= 200:
            self.__youWonOrLost("Победа")

    def __youWonOrLost(self,condition):
        """Вывод надписи поражения или победы на экран"""
        result = ""
        if condition == "Победа":
            result = "Вы победили!"
        elif condition == "Поражение":
            result = "Вы проиграли"
        title = pygame.font.SysFont("Times New Roman", 50)
        youWon = title.render(result, True, self.BLACK)
        textWidth = youWon.get_width()
        textHeight = youWon.get_height()
        self.screen.blit(youWon,(self.WIDTH/2-textWidth/2,self.HEIGHT/2-textHeight/2))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
        sys.exit()

    def __instuctions(self):
        """Вывод инструкций на экран"""
        self.background.blit(self.screen)
        insY = 120
        insX = 20
        instructions = []
        instructionsFont = pygame.font.SysFont("Times New Roman", 20)
        instructions.append(instructionsFont.render("Игра 'Паника в лесу'", True, self.BLACK))
        instructions.append(instructionsFont.render("Вы играете за персонажа, находящимся внизу игрового окна", True, self.BLACK))
        instructions.append(instructionsFont.render("Вам необходимо ловить палочки, которые бросает лесная фея", True, self.BLACK))
        instructions.append(instructionsFont.render("Если палочка упадет, вы проиграли. Для победы наберите 200 очков", True, self.BLACK))
        instructions.append(instructionsFont.render("Для продолжения нажмите любую кнопку", True, self.BLACK))
        for instruction in instructions:
            self.screen.blit(instruction,(insX,insY))
            insY += 30
        pygame.display.update()
                            

if __name__ == "__main__":
    print("Вы запустили модуль напрямую")
    # Игра запускается данной строчкой
    game = ForestPanic()
        
