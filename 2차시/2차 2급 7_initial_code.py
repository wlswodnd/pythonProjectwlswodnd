def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = value - 32 / 1.8
    converted = int(value)
    return converted

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
value = 527
unit = "C"
ret = solution(value, unit)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")