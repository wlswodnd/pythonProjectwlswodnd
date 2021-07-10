def solution(temperature, A, B):
    answer = 0
    for i in range(A,B):
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution(temperature, A, B)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")