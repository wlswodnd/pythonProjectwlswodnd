# Cox Pro 2급_2차시

# 문제 1
max_product_number = 10

def fun_a(gloves):
    counter = [0 for _ in range(max_product_number +1)]
    for x in gloves :   # 해당 장갑의 제품번호에 저장
        counter[x] += 1 # +1 저장
    return counter
        # 순서도 : [2,1,2,2,4]
            # 왼손 counter [1,3,0,1,0,0,0,0,0,0,]
        # 순서도 : [1,2,2,4,4,7]
            # 오른손 counter [1,2,0,2,0,0,1,0,0,0,]
def solution(left_gloves,right_gloves):
    left_counter = fun_a(left_gloves)   # 왼손 장갑 제품별 개수 세기
    right_counter = fun_a(right_gloves) # 오른손 장갑 제품별 개수 세기

    total = 0    # 각 제품 번호별 최대한 많은 장갑 쌍 개수 세기
    for i in range(1,max_product_number +1 ):
        total += min(left_counter[i],right_counter[i])
    return total

left_gloves = [2,1,2,2,4]
right_gloves = [1,2,2,4,4,7]
ret = solution(left_gloves,right_gloves)
print("Solution 함수 결과  :",ret,".")