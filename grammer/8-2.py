class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} 유닛 {} 로 이동 속도 : {}".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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


# 드랍쉽 : 공중 유닛, 수송기. 마린등 유닛을 수송 . 공격 못함

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아간다. 속도 : {}"\
            .format(name, location, self.flying_speed))

class FlyableAttack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battle = FlyableAttack("배틀크루저", 500, 25, 5)

vulture.move("11시")
battle.fly(battle.name, "9시")
battle.move("9시")


# 건물
class BuildingUnitTest(Unit):
    def __init__(self, name, hp, location):
        pass # 나머지 코드를 정의하지 않고 우선 실행 가능한 상태로 만든다.

# 서플라이 디폿 ㅋ: 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnitTest("서플라이 디폿", 500, "7시")

def game_start():
    print("game start")

def game_end():
    pass

game_start()
game_end()


class BuildUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super 시 self 전달 불필요
        self.location = location