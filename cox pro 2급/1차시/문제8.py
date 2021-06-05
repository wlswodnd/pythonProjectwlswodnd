# Cox Pro 2급_1차시

# 문제 8
def solution (sentence):
    str = ""
    for c in sentence : # 해당 문장을 문자 하나씩 c에 대입
        if c != "." and c != " " :   # . 도 아니도 공백도 아니면
            str += c    # 대입
    size = len(str)
    for i in range (size//2) :  # 문자열의 절반의 수 만ㅋㅁ 반복
        if str[i] != str[size -1 - i] : # 양끝이 같는지
            return False
    return True

sentenec1 = "never odd or even."
ret1 = solution(sentenec1)
print("Solution1 함수 결과  :",ret1,".")

sentenec2 = "palindrome"
ret2 = solution(sentenec2)
print("Solution2 함수 결과  :",ret2,".")
