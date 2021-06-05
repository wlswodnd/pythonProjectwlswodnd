# Cox Pro 2급_1차시

# 문제 10
def solution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data :
        if d <= average :
            cnt += 1
    return cnt

data1 = [1,2,3,4,5,6,7,8,9,10]
ret1 = solution(data1)
print("Solution1 : return value of the function is",ret1,".")

data2 = [1,1,1,1,1,1,1,1,1,10]
ret2 = solution(data2)
print("Solution2 : return value of the function is",ret2,".")