import pygame



class itemClass(pygame.sprite.Sprite):
    def __init__(self, weaponDamage, durability, range):
        self.weaponDamage = weaponDamage
        self.durability = durability
        self.range = range



baton = itemClass(15, 1000, 5)
glock20 = itemClass(50, 1000, 100)
tazer = itemClass(5, 100, 5)
