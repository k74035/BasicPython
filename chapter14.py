# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다".format(balance))
        return balance
    
def withdraw_night(balance, money): # 저녁에 출금
    commision = 100 # 수수료 100원
    return commision, balance - money - commision

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commision , balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은{1}원입니다".format(commision, balance))


# 기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}"\
#         .format(name,age,main_lang))

# profile("유재석", 20, "python")
# profile("김태호", 25, "javav")

# 같은 학교 같은 학년 같은 반 같은 수업 -> 기본값 사용
def profile(name, age= 17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용언어: {2}"\
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")


# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)
    
profile(name = "유재석", main_lang = "파이썬", age = 20 )
profile(main_lang = "자바", age = 25, name = "김태호")

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
    
def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#", "javaScript")
profile("김태호", 25, "Kotlin", "Swift")