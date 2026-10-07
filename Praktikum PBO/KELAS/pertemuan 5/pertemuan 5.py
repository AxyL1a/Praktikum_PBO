# Denny Mulia
# 2509106011

from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack 
        self.armor = armor

    @abstractmethod
    def ulti(self,target):
        return (self.attack * 88) - target.health

    def hitung_damage(self,target):
        return max(self.attack - target.armor, 0)

    def serang(self, target):
        damage = self.hitung_damage(target)
        target.health -= damage
        print(f'{self.name} menyerang {target.name}, damage {damage}')

    def __add__(self, healing):
        return self.health + healing

    def __sub__(self,burn):
        darah =self.health
        for i in range(60):
            darah = darah - burn
            print('darah: ', darah)
        self.health = darah
        print(self.health)

class Mage(Hero):
    def hitung_damage(self, target):
        return self.attack

    def ulti(self,target):
        return (self.attack * 88) - target.health

class Warrior(Hero):
    def hitung_damage(self,target):
        return super().hitung_damage(target) + 10

    def ulti(self,target):
        return (self.attack * 67) - target.health

class Minion():
    def __init__(self,name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage




# minion = Minion("minion", 40, 5,0)
sora = Warrior("Sora", 100, 50, 32)
eudora = Mage("Eudora", 100,60, 5)

# sora.serang(minion)
# eudora.serang(sora)
# sora.serang(eudora)


# print(sora.ulti(eudora))
print(isinstance(eudora,Mage))
# print(eudora + 100)
# print(eudora - 3)