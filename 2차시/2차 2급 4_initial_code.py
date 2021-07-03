#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words):
    #여기에 코드를 작성해주세요.
    answer = ''
    for i in words:
        if 5 <= len(i) :
            answer += i
    if answer == '':
        answer = "empty"
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")