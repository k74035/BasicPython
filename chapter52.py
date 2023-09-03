# 패캐지 
# 하나의 디렉토리에 여러 파일 모듈을 갖다 놓은 것
# import시 맨뒤에 있는 부분은 모듈이나 패캐지만 가능 / 클래스나 함수는 import 바로 할 수 없다.

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # 다만 from import 부분에서는 클래스나 함수를 사용가능하다
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # __all__
# from random import *
from travel import *    
''' *은 travel이라는 패캐지에 있는 모든 것을 가져오겠다는 것이지만 실제로는 문법상으로
공개 범위를 설정을 해주어야만 한다
패캐지 안에 포함된 것들 중 원하는 것만 공개 원하지 않는 것은 비공개로 가능하다
__init.py__에서 설정 가능하다.

''' 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()