# while(반복문)
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".foramt(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")


# customer1 = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 화".format(customer1, index))
#     index += 1

customer = "토르"
person = "unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")