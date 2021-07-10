def solution(temperature, A, B):
    answer = 0
    for i in range(A+1,B):  # A와 B 사이의 수 를 i에 대입
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
                # i가 A보다 크고 i가 B보다 크면
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
temperature = [3,2,1,5,4,3,3,2] # n일동안 매일매일 평균 기온 리스트
A = 1
B = 6
    # A번째 수 와 B번째 수의 사이에 수들이 A와B보다 큰 수를 찾기
ret = solution(temperature, A, B)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")