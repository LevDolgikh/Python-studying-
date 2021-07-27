# Date: 20.07.2021
# Author: Lev Dolgikh

# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Hero(object):

    def blast(self,enemy):
        print("Игрок стреляет во врага")
        enemy.die()

class Alien(object):

    def die(self):
        print("Пришелец погиб :)")

hero = Hero()
alien = Alien()
hero.blast(alien)
        
input("\n\nНажмите 'Enter', что бы выйти")



