# Cox Pro 2급_2차시

# 문제 6
def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(length):
        if i == floors[i+1] :
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

floors = [1,2,5,4,2]
ret = solution(floors)
print("Solution 함수 결과  :",ret,".")