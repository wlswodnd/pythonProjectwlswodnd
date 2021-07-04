    # 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(scores, cutline):
    # 여기에 코드를 작성해주세요.
    answer = 0
    for i in scores:
        if i >= cutline :
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")