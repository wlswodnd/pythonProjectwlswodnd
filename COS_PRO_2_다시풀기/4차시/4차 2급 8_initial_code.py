def solution(n, votes):
    arr = [0] * (n + 1)
    for vote in votes:
        arr[vote] += 1

    for i in range(1, n+1):
        if arr[i] > sum(arr)/2:
            return i
    return -1

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")