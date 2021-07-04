def func_a(bundle, start):
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle):
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer
        
def solution(n, bundle):
    a_cards = func_a(bundle,n)[:n]
    b_cards = func_a(bundle,n)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score,b_score)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")