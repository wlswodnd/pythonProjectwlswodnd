def solution(socks):
    answer = 0
    count = [0 for _ in range(10)]
    for s in socks:
        count[s] += 1
    for c in count:
        answer += (c % 2)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
socks = [1, 2, 1, 3, 2, 1]
ret = solution(socks)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다. 
print("solution 함수의 반환 값은", ret, "입니다.")