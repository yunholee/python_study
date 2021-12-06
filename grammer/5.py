def open_account():
    print("create new account")

def deposit(balance, money):
    print("입금 완료 잔액은 {0}원".format(balance + money))

    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료. 잔액은 {} 원 입니다".format(balance - money))
        return balance -money
    else:
        print("출금 안됨. 잔액은 {} 원 입니다".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - commission - money
    #return (commission, balance - commission - money)  이것과 동일




balance = 0
balance = deposit(balance, 1000)
#print(balance)
balance = withdraw(balance, 500)
(commission, balance) = withdraw_night(balance, 300)
print("수수료 {}이며, 잔액은 {} 입니다".format(commission, balance))

def profile(name, age=17, main_lang='python'):
     print("이름: {0}\t나이: {1}\t언어:{2}" \
     .format(name, age, main_lang))


profile('uno', 20, 'java')
profile('park', 30, 'php')
profile('sun')
profile(main_lang='go', age=25, name='lee')


def profile1(name, age, lang1, lang2, lang3):
    print("name : {}\tage: {}".format(name, age), end= " ")
    print(lang1, lang2, lang3)

profile1('uno', 20, 'jajva', 'go', 'python')


def profile2(name, age, *language):
    print("name : {}\tage: {}".format(name, age), end= " ")
    for lang in language:
        print(lang, end= " ")
    print()

profile2('uno', 20, 'jajva', 'go', 'python', 'php', 'c++')



gunin = 10

def checkpoint(soldiers):
    #gunin = 20
    global gunin
    gunin = gunin - soldiers
    print("함수내 남은총 : {}".format(gunin))

print("전체 총: {}".format(gunin))
checkpoint(2)
print("남은 총: {}".format(gunin))



def checkpoint2(gunin, soldiers):
    gunin = gunin - soldiers
    print("함수내 남은총 : {}".format(gunin))
    return gunin

gunin = checkpoint2(gunin, 2)
print("남은 총: {}".format(gunin))



def std_weight(height, gender):
    add = 0
    if gender == 'man':
        add = 22
    else :
        add = 21

    height2 = height / 100

    return height2 * height2 * add

result = round(std_weight(175, 'man'), 2)
print(result)





