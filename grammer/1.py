# STEP 2
print("hello world")
print('hello world')
print("hello world"*9)
print(10 > 5)
print(False) # True False 처럼 첫자가 대문자
print(not False)
print(not (5>6))

# 한줄 주석

'''
두줄 주석
두줄 주석
'''

name = '오아'
count = 3
print(name + " 브랜드는" + str(count) +  "개 입니다") # + 사용시에는 문자열 연결시 str()을 이용해 String 유형으로 변형해야한다.
print(name , " 브랜드는" , count ,  "개 입니다") # , 뒤에 공백이 하나더 추가된다.  , 사용시 str() 하지 않아도 된다.

# STEP3
print(2*3)
print(2**3) # 2^3
print(10%3) # 1
print(10/3) # 3.3333
print(10//3) # 3

print(3 == 3)
print(3 != 3)
print(not(1 != 3))

print((3>0) and (3<5))
print((3>0) & (3<5)) # && 가 아니고 &
print((3>0) or (3>5))
print((3>0) | (3>5)) # || 가 아니고 |

print(5>4>3)
print(5<6>3)

print(abs(-5))
print(pow(4,2)) # 4**2 동일
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) # 3

from math import * # math 안의 모든 함수를 사용한다.
print(floor(4.99)) # 내림 4
print(ceil(3.2)) # 올림 3
print(sqrt(16)) # 4

from random import *
print(random()) # 0.0 ~ 1.0 미만
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만
print(int(random() * 10) + 1) # 1 ~ 10이하
print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1 ~ 46미만의 수
print(randint(1,45)) # 1 ~ 45이하의 수

day = randint(4,28)
print("스터디 날짜는 " + str(day) +  " 일 입니다")

# STEP 4
sentence = """
안녕하세요
하하하
"""
print(sentence)

jumin = "901212-1234567"
print("성별" + jumin[7])
print("년도" + jumin[0:2]) # 0~2 이전까지
print("월" + jumin[2:4])
print("앞자리" + jumin[0:6])
print("앞자리" + jumin[:6])
print("뒷자리" + jumin[7:14])
print("뒷자리" + jumin[7:])
print("뒷자리(뒤에서부터)" + jumin[-7]) # 1
print("뒷자리(뒤에서부터)" + jumin[-7:]) # 1234567
print("뒷자리(뒤에서부터)" + jumin[-7:-1]) # 123456

python = "Python is Good pp"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java")) # 대소문자 구분함

index = python.index("G")
print(index)
index = python.index("o", index+1)
print(index)
print(python.find("Java")) # -1 찾는값 없음
#print(python.index("Java")) # Error 발생
print(python.count("p")) # p문자 갯수

## 1시간 강의

print("나는 %d살 입니다" % 20) # print("%d" % 20)
print("나의 이름은 %s입니다" % "이윤호") # print("%s" % "")
print("성적은 %c 입니다" % "A")
print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강")) # print("%s %s" % ("", ""))

print("나는 {}살 입니다".format(20)) # print("{}".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강")) #print("{} {}".format("", ""))
print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "빨강")) #print("{1} {0}".format("", ""))

print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨강")) # print("{age} {color}".format(age="", color=""))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨강", age=20))

age = 40
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요".format(color="빨강", age=20))

print('안녕\n하세요')

site = "http://naver.com"

val0 = site.replace("http://", "")
#val1 = val0[0:5]
val1 = val0[:val0.index('.')]
val2 = val1[:3]
val3 = len(val1)
val4 = val1.count('e')
print("{}{}{}!".format(val2, val3, val4))
print("{0}{1}{2}!".format(val2, val3, val4))
print("{val2}{val3}{val4}!".format(val2=val2, val3=val3, val4=val4))