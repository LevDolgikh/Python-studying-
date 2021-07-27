# Date: 20.07.2021
# Author: Lev Dolgikh
import random
import math
# К-среднее
# Демонстрирует разбиение изображения на кластеры

class Image(object):
    """Класс - картинка"""
    def __init__(self):
        """инициализирует картинку"""
        self.imageMap = []
    def __str__(self):
        """вывод на экран картинки"""
        if self.imageMap:
            rep = ""
            for imageString in self.imageMap:
                for imageCell in imageString:
                    rep += str(imageCell) + " "
                rep += "\n"
        else:
            rep = "Картинки нет, не могу вывести"        
        return rep
    def setImage1(self):
        """устанавливает 1 картинку по умолчанию"""
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" "," "," ","0","0","0"," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" "," "," "," "," "," "," "," "," "," "])
        self.imageMap.append([" "," "," "," "," "," "," "," "," "," "])
        self.imageMap.append([" "," "," "," "," "," "," "," "," "," "])
        self.imageMap.append([" "," "," "," "," "," "," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" "," "," ","0","0","0"," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
    def setImage2(self):
        """устанавливает 2 картинку по умолчанию"""
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" "," "," ","0","0","0"," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" ","0"," "," "," "," "," ","0"," "," "])
        self.imageMap.append(["0","0","0"," "," "," ","0","0","0"," "])
        self.imageMap.append([" ","0"," "," "," "," "," ","0"," "," "])
        self.imageMap.append([" "," "," "," "," "," "," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
        self.imageMap.append([" "," "," ","0","0","0"," "," "," "," "])
        self.imageMap.append([" "," "," "," ","0"," "," "," "," "," "])
    def kMeans(self, clustersNumber):
        """разбивает картинку на кластеры"""
        centers = [["1","1"]]
        newCenters = []
        iterationCount = 0
        while newCenters != centers and iterationCount <= 10:
            # Установить начальное значение кластеров(случайным образом или на основании формул)
            if not newCenters:
                centers = []
                for k in range(1,clustersNumber+1):
                    newCenter = []
                    maxDistance = 0
                    distance = 0
                    if centers:
                        for i in range(1,20):
                            randX = random.randint(0,len(self.imageMap))
                            randY = random.randint(0,len(self.imageMap))
                            randCenter = [randX, randY]
                            while randCenter in centers:
                                randX = random.randint(0,len(self.imageMap))
                                randY = random.randint(0,len(self.imageMap))
                                randCenter = [randX, randY]
                            for center in centers:
                                xCenter, yCenter = center
                                distance += math.sqrt((randX-xCenter)**2+(randY-yCenter)**2)
                                if distance > maxDistance:
                                    maxDistance = distance
                                    newCenter = randCenter
                        centers.append(newCenter)
                    else:
                            randX = random.randint(0,len(self.imageMap))
                            randY = random.randint(0,len(self.imageMap))
                            randCenter = [randX, randY]
                            centers.append(randCenter)
            else:
                centers = newCenters
            # Находит расстояния минимальные расстояния между точками и центрами кластеров, указывает каким кластерам относятся точки
            for y in range(0, len(self.imageMap)):
                for x in range(0, len(self.imageMap[0])):
                    distanceToCenters = []
                    if self.imageMap[y][x] != " ":
                        for center in centers:
                            xCenter, yCenter = center
                            distance = math.sqrt((x-xCenter)**2+(y-yCenter)**2)
                            distanceToCenters.append(distance)
                        centerIndex = distanceToCenters.index(min(distanceToCenters))
                        self.imageMap[y][x] = str(centerIndex + 1)
            # Находит геометрический центр
            for i in range(0,len(centers)):
                weiszfeldNumeratorX = 0
                weiszfeldDenominatorX = 0
                weiszfeldNumeratorY = 0
                weiszfeldDenominatorY = 0
                xOldCenter, yOldCenter = centers[i]
                for y in range(0, len(self.imageMap)):
                    for x in range(0, len(self.imageMap[0])):
                        if self.imageMap[y][x] == str(i+1):
                            distance = math.sqrt((x-xOldCenter)**2+(y-yOldCenter)**2)
                            try:
                                weiszfeldNumeratorX += x/distance
                                weiszfeldDenominatorX += 1/distance
                                weiszfeldNumeratorY += y/distance
                                weiszfeldDenominatorY += 1/distance
                            except ZeroDivisionError:
                                weiszfeldNumeratorX = 0
                                weiszfeldDenominatorX = 0
                                weiszfeldNumeratorY = 0
                                weiszfeldDenominatorY = 0
                try:
                    xNewCenter = float(weiszfeldNumeratorX/weiszfeldDenominatorX)
                    yNewCenter = float(weiszfeldNumeratorY/weiszfeldDenominatorY)
                    newCenter = [xNewCenter, xNewCenter]
                except ZeroDivisionError:
                    newCenter = xOldCenter, yOldCenter
                newCenters.append(newCenter)
            iterationCount += 1
            
class Main(object):
    image1 = Image()
    image1.setImage2()
    print("Добрый вечер! Данная программа является тестовой реализацией алгоритма k-средних на простейшем ресунке")
    print("Изображение:")
    print(image1)
    clusters = int(input("Введите количество кластеров от 1 для 10 для разбиения рисунка: "))
    if clusters in range(1,10):
        image1.kMeans(clusters)
    print("Ваш результат(цифрами отображается номер кластера):")
    print(image1)


main = Main()

input("\n\nНажмите 'Enter', что бы выйти")



