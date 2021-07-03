def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1,length):
        if floors[i] > floors[i-1]:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
floors = [1, 2, 5, 4, 2]
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")