def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer

def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score2 - score1)
    return answer
            
def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    down = func_b(mid_scores, final_scores)
    answer = [up, down]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")