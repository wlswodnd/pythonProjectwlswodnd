# Cox Pro 2급_2차시

# 문제 2
def fun_a(arr): # 5의 배수
    count = 0
    for n in arr :
        if n % 5 == 0:
            count += 1
    return count

def fun_b(three,five):  # 비교
    if three > five :
        return "three"
    elif three < five :
        return  "five"
    else:
        return "same"

def fun_c(arr): # 3의 배수
    count = 0
    for n in arr :
        if n % 3 == 0 :
            count += 1
    return count

def solution (arr):
    count_three = fun_c(arr)
    count_five = fun_a(arr)
    answer = fun_b(count_three,count_five)
    return answer

arr = [2,3,6,9,12,15,10,20,22,25]
ret = solution(arr)
print("Solution 함수 결과  :",ret,".")