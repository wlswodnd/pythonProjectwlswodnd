def func_a(passed, non_passed):
    return ( passed > 1 and non_passed ==0 )

def func_b(scores):
    answer = 0
    if scores[0] < 40:
        answer += 1
    if scores[1] < 44:
        answer += 1
    if scores[2] < 35:
        answer += 1
    return answer

def func_c(scores):
    answer = 0
    if scores[0] >= 80:
        answer += 1
    if scores[1] >= 88:
        answer += 1
    if scores[2] >= 70:
        answer += 1
    return answer

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_c(my_score)
        non_passed = func_b(my_score)
        answer += func_a(passed,non_passed)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")