#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    #여기에 코드를 작성해주세요.
    answer = [0 for _ in range(4)]  # 0을 4개 가지고 있는 리스트
    for i in people :
        if i >= 105 :
            answer[3] += 1  # xl에 1 추가
        elif i <= 105 and i >= 100 :    # 사이즈가 100이상 105 미만이면
            answer[2] += 1  # l에 1 추가
        elif i <= 100 and i >= 95 : # 사이즈가 95이상  100미만이면
            answer[1] += 1  # m에 1 추가
        elif i <= 95 :  # 사이즈가 95미만이면
            answer[0] += 1  # s에 1 추가
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")