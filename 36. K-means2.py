# Date: 20.07.2021
# Author: Lev Dolgikh

import random
import math
from PIL import Image, ImageDraw

# К-среднее (вариант исполнения номер 2)
# Демонстрирует разбиение изображения на кластеры (по цвету)
def kMeans(image,clusters,fileOutputName):
    colorCenters = []
    clustersPixels = []
    newCenters = ["1"]
    iterationCount = 0
    while iterationCount < 10 and newCenters != colorCenters:
        # Определить центры кластеров случайным образом
        if not colorCenters:
            colorCenters = getRandomColorCenters(clusters)
        else:
            colorCenters = newCenters
        # Распределить пиксели по кластерам
        clustersPixels = pixelToClusters(image,colorCenters)
        # Определение нового центра кластера
        newCenters = newClusterCenters(clustersPixels, colorCenters, clusters)
        iterationCount += 1
    printClustersInFile(image,clustersPixels,colorCenters,fileOutputName)
            
            
def getRandomColorCenters(clusters):
    """Задает случайные цвета центров кластеров"""
    colorCenters = []
    for i in range(1,clusters+1):
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        randomRGB = [randR, randG, randB]
        colorCenters.append(randomRGB)
    return colorCenters

def pixelToClusters(image,colorCenters):
    """Распределяет пиксели по кластерам"""
    pixels = image.load()
    HEIGHT, WIDTH = image.size
    clustersPixels = []
    for y in range(0, WIDTH):
        for x in range(0, HEIGHT):
            distance = 0
            distances = []
            for colorCenter in colorCenters:
                red, green, blue = pixels[x,y]
                centerR, centerG, centerB = colorCenter
                distance = math.sqrt((red-centerR)**2+(green-centerG)**2+(blue-centerB)**2)
                distances.append(distance)
            minDistanceIndex = distances.index(min(distances))
            minClusterIndex = minDistanceIndex + 1
            clustersPixels.append([x, y, minClusterIndex, red, green, blue])
    return clustersPixels

def newClusterCenters(clustersPixels, colorCenters, clusters):
    """Возвращает новые центры кластеров"""
    newCenters = []
    for i in range(1,clusters+1):
        rOldCenter, gOldCenter, bOldCenter = colorCenters[i-1]
        weiszfeldDenominator = 0
        weiszfeldNumeratorR = 0
        weiszfeldNumeratorG = 0
        weiszfeldNumeratorB = 0
        for pixel in clustersPixels:
            pixelX, pixelY, clusterIndex, pixelR, pixelG, pixelB = pixel
            if i == clusterIndex:
                colorDistance = math.sqrt((pixelR-rOldCenter)**2+(pixelG-gOldCenter)**2+(pixelB-bOldCenter)**2)
                try:
                    weiszfeldDenominator += 1/colorDistance
                    weiszfeldNumeratorR += pixelR/colorDistance
                    weiszfeldNumeratorG += pixelG/colorDistance
                    weiszfeldNumeratorB += pixelB/colorDistance
                except ZeroDivisionError:
                    weiszfeldDenominator = 0
                    weiszfeldNumeratorR = 0
                    weiszfeldNumeratorG = 0
                    weiszfeldNumeratorB = 0
        try:
            rNewCenter = float(weiszfeldNumeratorR/weiszfeldDenominator)
            gNewCenter = float(weiszfeldNumeratorG/weiszfeldDenominator)
            bNewCenter = float(weiszfeldNumeratorB/weiszfeldDenominator)
            newCenter = [rNewCenter, gNewCenter, bNewCenter]
            newCenters.append(newCenter)
        except ZeroDivisionError:
            newCenters.append([rOldCenter, gOldCenter, bOldCenter])
    return newCenters

def printClustersInFile(image,clustersPixels,colorCenters, fileOutputName):
    """Пиксели кластеров раскрашивает цветом центра каждого кластера и печатает в файл"""
    newimdata = []
    for pixel in clustersPixels:
        pixelX, pixelY, clusterIndex, pixelR, pixelG, pixelB = pixel
        colorCenterR, colorCenterG, colorCenterB = colorCenters[clusterIndex-1]
        newimdata.append((int(colorCenterR), int(colorCenterG), int(colorCenterB)))
    newim = Image.new(image.mode,image.size)
    newim.putdata(newimdata)
    newim.save(fileOutputName)
    
class Main(object):
    # Считывание параметров
    print("Программа разбивает изображение на кластеры методом k-средних")
    fileInputName = input("Введите путь до исходного изображения: ")
    clusters = int(input("Введите количество кластеров: "))
    if clusters not in range(1,100):
        print("Количество кластеров указано неверно, по умолчанию устанавливается значение - 10")
        clusters = 10
    fileOutputName = input("Введите как нужно сохранить изображения: ")

    # Обработка и запись
    image = Image.open(fileInputName)
    imageRGB = image.convert("RGB")
    kMeans(imageRGB, clusters, fileOutputName)

main = Main()

input("\n\nНажмите 'Enter', что бы выйти")



