# 지역변수와 전역변수

gun = 10

def checkpoint(sordiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = 20
    gun = gun - sordiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
def checkpoint_ret(gun,sordiers):
    gun = gun -sordiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))