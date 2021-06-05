# Cox Pro 2급_2차시

# 문제 3
import math

def solution (N,M) :
    total = 0
    for x in range(N,M+1):
        if x % 2 == 0 :
            total += x*x
    return total

N = 4
M = 7

ret = solution(N,M)
print("Solution 함수 결과  :",ret,".")