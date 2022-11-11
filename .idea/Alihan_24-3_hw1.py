class Hero :
    Head = 1
    abulity = True
    def __init__(self, name, nickname, hp:int, damage):
        self.name=name
        self.nickname=nickname
        self.hp=hp
        self.damage=damage
    def heal(self):
        print(self.hp + 100)
    def two_damage(self):
        print(self.damage * 2)
    def dreetings(self):
        print(f'my name is {self.name}')
    def brand_phras(self):
        print('good will win')

hero1=Hero('Alihan', 'Alihan123', 20, 1000000)
hero2=Hero('Bakai', 'Bakai123', 250, 545)
hero3=Hero('Ivan', 'Ivan123', 34, 543)
hero4=Hero('Kudret', 'Kudret123', 56, 656)

hero1.heal()
hero2.two_damage()
hero3.dreetings()
hero4.brand_phras()