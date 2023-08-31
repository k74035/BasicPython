# 문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)

# 여러 문장을 가진 문자열 출력
sentence3 = '''
나는 소년이고.
파이썬은 쉬워요
'''
print(sentence3)
# '''는 그냥 사용하면 주석처리가 되지만 이렇게 변수에 할당하거나 함수 내에서 사용시 여러문장을 쓰겠다로 받아들인다


# 슬라이싱 (필요한 만큼만 가져오는 것)
jumin = "990129-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:14])
# print("뒤 7자리 : " + jumin[7:]) 위와 동일

print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번쨰부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # python의 0번째 문자가 대문자이냐?
print(len(python)) # python의 길이 반환
print(python.replace("python", "java")) # python 변수에 저장된 문자열에서 python을 java로 교체

index = python.index("n") # n이 있는 위치를 반환
print(index)
# index는 0에서 부터 시작한다는 것을 잊지 말자!
index = python.index("n", index + 1) # 두번째 n이 있는 위치를 반환

print(python.find("java"))
print(python.count("n")) # n이 사용된 횟수 반환


# 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20)) # 순서는 상관 없다

# 방법 4 (v3.6이상 사용가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 변수에 저장된 값을 사용가능

