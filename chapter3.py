# 간단한 수식

print(abs(-5)) # 5 절대값
print(pow(4, 2)) # 4^2 제곱
print(max(5, 12)) # 12 최대값
print(min(5, 12)) # 5 최솟값
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)+ 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성