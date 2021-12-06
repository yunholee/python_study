# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# print("코딩 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("\n과학 : 80")
# score_file.write("\n국어 : 50")
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline()) #한줄 읽고 커서만 다음 줄로 이동된 상태
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines()
# for line in lines:
#     print(line, end='')

# import pickle
# profile_file = open('profile.p', 'wb')
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "농구"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# import pickle
# profile_file = open('profile.p', 'rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()


import pickle
with open('profile.p', 'rb') as profile_file:
    print(pickle.load(profile_file))
# close 따로 안해줘도 됨

with open('score.txt', 'w', encoding='utf8') as score_file:
    score_file.write('\n몰라:50')


for idx in range(1,3):
    with open("{}주차.txt".format(idx), 'w', encoding='utf8') as file:
        file.write("- {}주차 주간보고-".format(idx))
        file.write("\n부서:")
        file.write("\n이름:")
        file.write("\n업무 요약:")