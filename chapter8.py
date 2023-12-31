# tuple(튜플) -> 변경되지 않는 목록
# 괄호 없이도 값을 할당 가능하다 -> menu = "돈까스", "치즈까스"
# 주로 함수에서 return 값을 반환할 때 많이 사용한다.

menu = ("돈가스", "치즈까스")
print(menu(0))
print(menu(1))

# menu.add("생선까스") # ->값 추가 불가능

# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java, python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.addd("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)