# print('java', 'python')
# print('java', 'python', sep=' vs ', end='?')


# import sys
# print('python', 'java', file=sys.stdout);
# print('python', 'java', file=sys.stderr);

scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')


for number in range(1,21):
    print("대기번호 : {}".format(str(number).zfill(3)))


# answer = input('아무값 입력해요 :')
# print(type(answer))  무조건 str 타입
# print("입력한 값은 : {} 입니다".format(answer))


# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일땐 + 로, 음수일땐 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(123456789))
# 3자리 마다 콤마를 찍어주기 + - 부호
print("{0:+,}".format(123456789))
print("{0:+,}".format(-123456789))
# 3자리마다 콤마, 부호 붙이고, 30자리 확보, 빈공간은 ^^표시
print("{0:^<+30,}".format(123456))
# 소수점 출력
print("{0:.2f}".format(5/3))