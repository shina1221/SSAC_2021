from warnings import catch_warnings


class Unit():
    def __init__(self, char_class, hp, mp):
        self.char_class = char_class
        self.hp = hp
        self.mp= mp
    def attack(self):
        print('{}이(가) 공격을 시전합니다.'.format(self.char_class))
    def move(self, x, y):
        self.x =x 
        self.y =y
        print('{}이(가) ({}, {})로 이동했음.'.format(self.char_class, self.x, self.y))

class Melee(Unit):
    def __init__(self, char_class, hp, mp, weapon):
        super().__init__(char_class,hp,mp)
        self.weapon = weapon
    def attack(self):
        print('{}(이)가 공격합니다.'.format(self.char_class))

class Fighter(Melee):
    def __init__(self, hp, mp, weapon='검', shield='원형방패'):
        super().__init__('전사', hp, mp, weapon) # 상위클래스 호출 : super
        self.shield = shield
    def use_shiled(self):
        print('전사가 {}로 적의 공격을 막습니다.'.format(self.shield))

class Paladin(Melee):
    def __init__(self, hp, mp, weapon):
        super().__init__('성기사', hp, mp, weapon)
    #Method overiding : (상위 클래스) 메소드 정의
    def attack(self):
        print('성기사가 공격합니다.')
        print('또 공격합니다.')

    def heal(self):
        print('성기사가 치유를 시전합니다.')
class Wizard(Unit):
    def __inint__(self, hp, mp, skill):
        super().__init__('마법사',hp,mp)
        self.hp = hp
        self.mp = mp
        self.skill = skill
    def use_sepll(self):
        print('마법사가 마법을 시전합니다.')


#다중상속#############################
class Fightmage(Fighter, Wizard):
    def __init__(self, char_class, hp, mp, weapon):
        super().__init__(self, '파이트메이지', hp, mp, weapon)

#        super(Fighter).__init__('파이트메이지', hp,mp,weapon)
    

f = Fighter(100, 20, '검')
w = Wizard(50, 100, ['Fireball', 'Drainlife'])
p = Paladin(80, 50,'장검')
 
units = [f,w,p]

for c in [f,w,p]:
    c.attack()

for unit in units:
    unit.attack()
    
f.move(10,10)
p.move(2,5)
w.move(3,5)

f.use_shiled()
w.use_sepll()
p.heal()

#전사만 공격하는 페이즈
for unit in units:
    if isinstance(unit, Fighter):
        unit.attack()

print()

#근거리 유닛만 공격하는 페이즈
#다형성
for unit in units:
    if isinstance(unit, Melee):
        unit.attack()

#    if type(unit) in [Fighter, Paladin, Monk, Spearmen]:
#        unit.attack()

print()
fm=Fightmage(90, 70, '완드')#왜 안되지?
fm.attack()
fm.hide()
fm.use_shield()
