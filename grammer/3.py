menu = {"커피", "우유", "차"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import *
users = range(1, 21) # 1 ~ 20까지
#print(type(users))
users = list(users)
#print(type(users))
shuffle(users)
winners = sample(users, 4)

print(winners[0])
print(winners[1:])

print("치킨 당첨자 %s" % (winners[0]))
print("치킨 당첨자 {}".format(winners[0]))

print("커피 당첨자 {}".format(winners[1:]))