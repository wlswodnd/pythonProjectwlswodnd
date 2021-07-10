def solution(money, chairs, desks):
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = @@@
            if answer < price and @@@:
                answer = price
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
money1 = 7
chairs1 = [2, 5]
desks1 = [4, 3, 5]
ret1 = solution(money1, chairs1, desks1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 7
chairs2 = [3]
desks2 = [5]
ret2 = solution(money2, chairs2, desks2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")