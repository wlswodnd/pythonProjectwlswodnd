def solution(stuffs):
    answer = 0
    small_counter, general_counter = 0, 0
    for s in stuffs:
        if s > 3:
            general_counter += s
        else:
            small_counter += s
    if small_counter > general_counter:
        answer = small_counter
    else:
        answer = general_counter
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
stuffs = [5, 3, 4, 2, 3, 2]
ret = solution(stuffs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")