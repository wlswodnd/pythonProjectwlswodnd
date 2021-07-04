def solution(calorie):
    min_cal = calorie[0]
    answer = 0
    for cal in calorie:
        if cal > min_cal:
            answer += cal - min_cal
        min_cal = min(min_cal, cal)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")