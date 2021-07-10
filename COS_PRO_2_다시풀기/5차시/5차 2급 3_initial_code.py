def solution(speed, cars):
    answer = 0
    for x in cars:
        if x >= speed * 11 / 10 and x < speed * 12 / 10:
            answer += 3
        elif x >= speed + speed * 0.2and x < speed + speed*0.3 :
            answer += 5
        elif x >= speed + speed*0.31:
            answer += 7
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")