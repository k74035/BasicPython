# class -> chapter 40에서 한 코딩을 간단하게 클래스라는 개념을 도입해본다

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린") -> 실행안됨

# __init__함수 -> 생성자 / 객체 생성시 자동호출 / 객체란 클래스로 부터 만들어지는 녀석

# 멤버변수 / class 내에서 정의 된 변수 

# 레이스 : 공중 유닛, 비행기, 클로킹( 상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 외부에서 객체에 멤버변수를 추가로 만들어서 사용

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))
    
# if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name)) 
# 확장한 멤버변수는 그 확장한 객체에만 해당되는 것임 wraith1.clocking은 안되는 것을 확인

# 메소드
# 클래스 내에서 메소드 괄호 내에는 무조건 self를 적어둔다고 기억하자

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
    
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
        