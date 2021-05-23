# Cox Pro 2급_1차시

# 문제2

def solution(price,grade) :
    answer = 0

    if grade == "S" :
        answer = price * 0.95   # 1 : 100%   0.5 : 50%   0.25 : 25%   0.1 : 1%
    if grade == "G" :
        answer = price * 0.90
    if grade == "V" :
        answer = price * 0.85

    return int(answer) # 계산된 가격을 리턴

price1 = 2500
grade1 = "V"
ret1 = solution(price1,grade1)
print("Solution : return value of the function is",ret1," .")

price2 = 96900
grade2 = "S"
ret2 = solution(price2,grade2)
print("Solution : return value of the function is",ret2," .")