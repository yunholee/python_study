class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:    
    print("나누기 전용 계산기")
    num1 = int(input("첫번째 숫자를 입력"))
    num2 = int(input("두번째 숫자를 입력"))

    if num1 >= 10 or num2 >= 10:
        raise ValueError # throw
    elif num1 <= 0 or num2 <= 0:
        raise MyError('나의 에러')
    

    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError: # 숫자가 아닐때
   print("에러다.")
except ZeroDivisionError as err: # 0으로 나눌때
    print(err)
except MyError as err:
    print(err)
#except:
except Exception as err:
    print("알수 없는 오류")
    print(err)
finally:
    print("here finally")