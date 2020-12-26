class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine1 = Unit("마린", 40, 5)

# 레이스 : 공중 유닛, 비행기. 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True; # 동적으로 외부에서 멤버변수를 만들 수 있음
if wraith2.clocking==True:
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))
