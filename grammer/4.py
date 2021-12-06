# if
weather = "rain1"
#weather = input("날씨 어때요?")

if weather == 'rain' or weather == 'snow':
    print('우산챙기삼')
elif weather == 'mise':
    print('마스크 챙기삼')
else:
    print('그냥 나가요')


#temp = int(input('기온 어때요?'))
temp = 10
if 30 >= temp:
    print('')
elif 10 <= temp and temp < 30:
    print('')
#elif 0 <= temp and temp > 10:
elif 0 <= temp < 10:
    print('')
else:
    print('')


# for

for waiting_no in range(5):
    print("대기번호 : {}".format(waiting_no))

# while
customer = "tor"
index = 5
while index >= 1:
    print("{0} 손님 커피가 준비되었어요. {1}번 남았어요".format(customer, index))
    index = index - 1

    if index == 0:
        print('커피는 폐기처리함')


# customer = "토르"
# person = "Unknown"

# while customer != person:
#     print("{} 커피가 준비되었어요".format(person))

#     person = input('이름이 뭐예요?')


# continue break
absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("수업 끝")
        break
    else:
        print("{} 야 책 읽어".format(student))


# 한줄 for
# 출석번호 1,2,3,4 를 101, 102, 103, 104로 변경

students = range(1, 5)
students = [i+100 for i in students]
print(students)

# 학생이름을 길이로 변환
students = ['uno', 'park', 'sunsun']
students = [len(i) for i in students]
print(students)

from random import *
time = range(5, 51)
get = 0
i = 1
chance = 50
while chance > 0:
    #rand = sample(time, 1)
    rand = randrange(1, 51)

    #if rand[0] >= 5 and rand[0] <= 15:
    if 5<= rand <= 15:
        print("[o] {}번째 손님 (소요시간 : {}분)".format(i, rand))
        get += 1
    else:
        print("[] {}번째 손님 (소요시간 : {}분)".format(i, rand))

    chance -= 1

print("총 탑승객 : {}분".format(get))


a = range(1,10)
print(type(a))
b = randrange(1,10)
print(type(b))