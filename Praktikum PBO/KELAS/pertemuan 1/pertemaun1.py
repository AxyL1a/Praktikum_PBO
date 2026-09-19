class Hero: 
    Jumlahhero = 0 #atribut kelas
    def __init__(self,name,health,armor,attack):
        self.name = name #atribut intance/ object
        self.health = health
        self.armor = armor
        self.attack = attack
        Hero.jumlahHero += 1

    # def healthUp (self, up):
    #     self.health += up

    # @classmethod
    # def totalhero(cls):
        


    # def levelUp(self):
    #     self.health += 50
    #     self.armor += 2
    #     self.attack += 5

    def healing (self):

        print(self.health)
        self.health += 10
        print(self.health)

roger = Hero('roger',100,5,8)
print(roger.name)



sniper = Hero ('sniper',50,5,30)
print (sniper.name)