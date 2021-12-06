class Unit:
    def __init__(self, name, hp = 40, damage = 5):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성됨".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린")

# 레이스 : 공중 유닛, 비행기, 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛 뺏기
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 객체에 멤버 추가 가능  wraith2에만 추가됨

# if wraith2.clocking == True:
#     print("{} 는 현재 클로킹 상태 입니다".format(wraith2.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("1시")

firebat1.damaged(25)
firebat1.damaged(25)