# list

subway = [1,2,3]
print(subway)
print(subway.index(2))
subway.append(4)
print(subway)
subway.insert(1, 0)
print(subway)
print(subway.pop())
print(subway)
subway.append(1)
print(subway)
print(subway.count(1))

my_list = [3,2,1,6,7,2]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
# my_list.clear()
print(my_list)
your_list = ["윤호", "경혜"]
my_list.extend(your_list)
print(my_list)

#dictionary

cabinet = {3:"uno", 100:343}
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) # 오류와 함꼐 다음 스크립트 중지
print(cabinet.get(222))
print(cabinet.get(222, '값없음'))

print(3 in cabinet)

cabinet[200] = "good"
print(cabinet)

del cabinet[100]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)

#1 시간 40분

# tuple 수정 불가
menu = ("돈까스", "치즈까스")
print(menu[0])
#menu.add("생선") # 오류

# name = "uno"
# age = 20
# hobby = "coding"
(name, age, hobby) = ("uno", 20, "coding")
print(name, age, hobby)


# set 중복안됨, 순서 없음
my_set = {1,3,3,2}
print(my_set)

java = {"uno", "park"}
python = set(["sun", "uno"])
print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

java.add('hi')

java.remove('uno')