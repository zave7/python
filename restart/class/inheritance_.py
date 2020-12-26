class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.test = "123"

class AttackUnit(Unit): # 상속할때는 () 에 명시한다!!!!!!!!
    # self는 자기 자신을 의미한다
    # 메소드에는 무조건 self를 적어줘야한다
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 슈퍼클래스의 생성자를 호출해준다!!
                                # self 도 넣어줘야한다니;;; 머임
        self.damage = damage

test = AttackUnit("test", 1, 2)
# print(test.hp)
print(test.test)