class Unit:
    def __init__(self, name, hp = 40):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격 합니다. 공격력 : {}"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었다".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다".format(self.name, self.hp))

        if self.hp <= 0:
            print("{} 은 파괴 되었습니다".format(self.name))


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("1시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기. 마린등 유닛을 수송 . 공격 못함

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아간다. 속도 : {}"\
            .format(name, location, self.flying_speed))

class FlyableAttack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리
valkyrie = FlyableAttack("발키리", 200, 6, 5)
valkyrie.fly("발키리", "3시")