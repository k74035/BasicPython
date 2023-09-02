# dictonary(사전) 자료형
# key와 value값으로 구성됨 / key값은 중복되지 않아야 함.

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) # -> keyerror / 실행오류

print(cabinet.get(3))
print(cabinet.get(5)) # -> none / 계속 실행됨
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet1 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet1["A-3"])
print(cabinet1["B-100"])

# 새 손님  -> 값 변환과 값 추가
print(cabinet1)
cabinet1["A-3"] = "김종국"
cabinet1["C-20"] = "조세호"
print(cabinet1)

# 간 손님 -> 값 삭제
del cabinet1["A-3"]
print(cabinet1)

# key 들만 출력
print(cabinet1.keys())

# value 들만 출력
print(cabinet1.values())

# key,value 쌍으로 출력
print(cabinet1.items())

# 목욕탕 폐점
cabinet1.clear()
print(cabinet1)