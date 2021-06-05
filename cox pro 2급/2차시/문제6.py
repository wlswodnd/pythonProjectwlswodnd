# Cox Pro 2급_2차시

# 문제 6
def solution(floors):
    dist = 0
    length = len(floors)    # 리스트내 층 개수 : 5
    for i in range(1,length): # 1~5 전까지
        if floors[i] > floors[i-1] :    # 현재층이 앞전층보다 크다면
            dist += floors[i] - floors[i-1]
        else:   # 아니면
            dist += floors[i-1] - floors[i]
    return dist

floors = [1,2,5,4,2]
ret = solution(floors)
print("Solution 함수 결과  :",ret,".")