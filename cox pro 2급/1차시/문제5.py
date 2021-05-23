# Cox Pro 2급_1차시

# 문제 5

def solution(arr) :
    left, right = 0, len(arr)-1
    while left < right :
        arr[left], arr[right] = arr[right],arr[left]
        left += 1
        print( left )
        right -= 1
        print( right )
    return arr

arr = [1,4,2,3]
ret = solution(arr)

print("Solution : return value of the function is",ret,".")
# 왼쪽     오른쪽
#  0        3
#  1        2
#  2        1  반복문 탈출 조건x
#   왼쪽       오른쪽
#   0          0      1 1 1 1
#   1         -1      4 3 3 4
#   2         -2      2 2 2 2