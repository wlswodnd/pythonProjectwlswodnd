#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0
    t = [0 for _ in range(3)]  # 0이 3개인 리스트
    # t = 0
    # a = 0
    # for i in cards :
    #     a += int(i)
    #     if i == cards[i][0]:
    #         t += 1
    # if t == 3 :
    #     answer = a * 3
    # elif t == 2 :
    #     answer = a * 2
    # else:
    #     answer = a
    for card in cards :
        if card[0] == "black" :
            t[0] += 1
        elif card[0] == "blue" :
            t[1] += 1
        elif card[0] == "red":
            t[2] += 1
        answer += int(card[1])  # 카드의 숫자룰 answer 누적 더하기
    if t[0] == 3 or t[1] == 3 or t[2] == 3 :
        answer *= 3
    elif t[0] == 2 or t[1] == 2 or t[2] == 2 :
        answer *= 2
        # "2" : 문자 2 : 숫자

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")