def solution(password):
    capital_count, small_count, digit_count = 0, 0, 0
    for p in password:
        if p >= 'A' and p <= 'Z':
            capital_count += 1
        elif p >= 'a' and p <= 'z':
            small_count += 1
        elif p >= @@@ and p <= @@@:
            digit_count += 1
    if @@@:
        answer = True
    else:
        answer = False
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
password1 = "helloworld"
ret1 = solution(password1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "Hello123"
ret2 = solution(password2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")