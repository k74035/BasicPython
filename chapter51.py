# 모듈 사용
# import chapter50
# chapter50.price(3) # 3명에서 영화 보러 갔을 때 가격
# chapter50.price_morning(4) # 4명에서 조조 할인 영화 보러 갔을 때
# chapter50.price_sordier(5) # 5명의 군인이 영화 보러 갔을 떄

# import chapter50 as ch # 모듈 명이 길때 줄여서 애칭으로 사용 가능
# ch.price(3)
# ch.price_morning(4)
# ch.price_sordier(5)

# from chapter50 import * # chapter50 모듈의 모든 걸 사용하겠다 
# # . 없이 바로 함수 호출하여 사용가능 
# # from random import *
# price(3)
# price_morning(4)
# price_sordier(5)

from chapter50 import price, price_morning
price(5)
price_morning(6)
# price_sordier(7) # 오류 price_sordier함수는 받지 않았음

# 이 부분은 price_sordier함수를 price로 부르겠다라는 의미 
from chapter50 import price_sordier as price
price(5) # 군인 5명의 요금을 내는 함수 price_sordier를 price로 쓰겠다.