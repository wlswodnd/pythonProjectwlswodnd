#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(time_table, n):
    #여기에 코드를 작성해주세요.
    answer = 0
    r = 0
    f = 0
    t = [0]*len(time_table)
    for a in time_table :
        for i in range(len(time_table)):
            if i+r == n :
                f = n
            t[i+r-f] += a
            r += 1
            break
    answer = max(t)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")