class Unit:
    def __init__(self):
        print("unit constructor")

class Flyable:
    def __init__(self):
        print("flyable constructor")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 다중상속에서 부모 생성자 호출시에는 앞의 클래스 생성자만 호출됨.
        Unit.__init__(self)
        Flyable.__init__(self)

class Wraith(FlyableUnit):

    cloaking_developed = False  # 이놈은 뭐야? static ?  파이썬에서는 클래스 변수라고 하네.

    def __init__(self):
        super().__init__()
        self.cloaking_mode # 멤버변수고..

    def set_cloaking():
        if Wraith.cloaking_developed == False:
            return

        

dropship = FlyableUnit() #print("unit constructor")

if isinstance(dropship, FlyableUnit):
    print("is instance")