# 반복문

# 111.
문자열 = input("문자열을 입력하세요 : ")
print(문자열*2)

# 112.
숫자 = int(input("숫자을 입력하세요 : "))
print(숫자+10)

# 113.
숫자 = int(input("숫자을 입력하세요 : "))
if 숫자%2 == 0 :
    print("짝수입니다")
else:
    print("홀수입니다")

# 114.
숫자 = int(input("숫자을 입력하세요 : "))
if 숫자+20 >= 255 :
    print(255)
else:
    print(숫자+20)

# 115.
숫자 = int(input("숫자을 입력하세요 : "))
if 숫자-20 >= 255 :
    print(255)
elif 숫자-20 <= 0 :
    print(1)
else:
    print(숫자-20)

# 116.
시간 = input("시간을 입력하세요 : ")
시,분 = 시간.split(":")
if 분 == "00" :
    print("정각입니다")
else:
    print("정각이 아닙니다")

# 117.
fruit = ["사과","포도","홍시"]
과일 = input("좋아하는 과일은? : ")
if 과일 in fruit :
    print("정답입니다")
else:
    print("오답입니다")

# 118.
warn_investment_ilst = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
종목명 = input("투자 종목을 입력하세요 : ")
if 종목명 in warn_investment_ilst :
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# 119.
fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
계절 = input("좋아하는 계절을 입력하세요 : ")
if 계절 in fruit :
    print("정답입니다")
else:
    print("오답입니다")

# 120.
fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
계절 = input("좋아하는 과일을 입력하세요 : ")
과일 = fruit.values()
if 계절 in 과일 :
    print("정답입니다")
else:
    print("오답입니다")