# 연산자

print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2 ** 3) # 거듭제곱 
print(5 % 3) # 나머지 구하기 
print(10 // 3) # 몫 구하기

print(10 > 3) # True 
print(4 >= 7) # False
print(10 < 3) # False

print(3 == 3) # True
print(4 == 3) # False
print(1 != 3) # True 느낌표(!)를 사용하게 되면 같지 않다를 뜻함

print(not(1 != 3)) # False
print((3 > 0 ) and (3 < 5)) # True / and 연산자는 두 개 모두 참이면 True
print((3 > 0) & (3 < 5)) # &는 and와 동일

print((3 > 0) or (3 > 5)) # True / or 연산자는 둘 중 하나만 참이면 True
print((3 > 0) | (3 > 5)) # True / |는 or와 동일

number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18 / number = number + 2 와 동일
print(number)
number *= 2 # 36 number = number * 2 와 동일 
print(number)
# 다른 연산자도 위와 같이 이용가능