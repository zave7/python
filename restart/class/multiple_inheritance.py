class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) 
        self.damage = damage

# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리
valkyrie = FlyableAttackUnit("발키리", 90, 6, 9)
valkyrie.fly(valkyrie.name, "3시")