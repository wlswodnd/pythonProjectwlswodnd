# 반복문

# 121.
문자 = input("문자 한개를 입력하세요 : ")
확인 = 문자.islower()
if 확인 == True:
    print(문자.upper())
else:
    print(문자.lower())

# 122.
sccore = int(input("점수를 입력 : "))
if 100 >= sccore >= 81 :
    print("A")
elif 80 >= sccore >= 61 :
    print("B")
elif 60 >= sccore >= 41 :
    print("C")
elif 40 >= sccore >= 21 :
    print("D")
elif 20 >= sccore >= 0 :
    print("E")

# 123.
환율 = { "달러":1167,"엔":1.096,"유로":1268,"위안":171 }
환전 = input("화폐이름과 금액을 입력하세요 : ")
금액,이름 = 환전.split(" ")
print(환율[이름]*int(금액),"원")

# 124.
일 = int(input("숫자을 입력 : "))
이 = int(input("숫자을 입력 : "))
삼 = int(input("숫자을 입력 : "))
수 = [일,이,삼]
print(max(수))

# 125.
통신사 = {"011":"SKT","016":"KT","019":"LGU","010":"알수없음"}
번호 = input("번호를 입력 : ")
순서 = 번호.split("-")
print(통신사[순서[0]])

# 126.
우편번호 = input("우편번호를 입력하세요 : ")
if 우편번호[2] == 0 or 1 or 2 :
    print("강북구")
else:
    if 우편번호[2] == 3 or 4 or 5 :
        print("도봉구")
    else:
        print("노원구")

# 127.
주민등록번호 = input("주민등록번호를 입력 : ")
if 주민등록번호[7] == 1 or 3 :
    print("남자")
else:
    print("여자")

# 128.
주민등록번호 = input("주민등록번호를 입력 : ")
if 주민등록번호[8] == 0 :
    print("남자")
else:
    print("여자")
# 129.
확인 = 0
주민등록번호 = input("주민등록번호를 입력 : ")
for 반복 in range(8) :
    확인 += int(주민등록번호[0+반복])*(2+반복)
print(확인)
for 계속 in range(4) :
    확인 += int(주민등록번호[8+계속]) * (2+계속)
결과 = 11-(확인%11)
if 결과 == int(주민등록번호[12]) :
    print("유효한 주민등록번호입니다")
else:
    print("유효하지 않은 주민등록번호입니다")

# 130.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
결과 = int(btc['opening_price']) + ( int(btc['max_price']) - int(btc['min_price']) )
if 결과 > int(btc['max_price']) :
    print("상승장")
else:
    print("하락장")
