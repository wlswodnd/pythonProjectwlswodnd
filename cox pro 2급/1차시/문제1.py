# Cox Pro 2급_1차시

# 문제1 : 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기

def solution (shirt_size) : # 함수 만들기
    # 지문 보고 풀기
    size_counter = [ 0 , 0 , 0 , 0 , 0 , 0 ]
    #               XS   S   M   L   XL XXL
    for ss in shirt_size : # 리스트에 반복 => 리스내 항목에 하나씩 대입
        if ss == "XS" :
            size_counter[0] += 1
        if ss == "S" :
            size_counter[1] += 1
        if ss == "M" :
            size_counter[2] += 1
        if ss == "L" :
            size_counter[3] += 1
        if ss == "XL" :
            size_counter[4] += 1
        if ss == "XXL" :
            size_counter[5] += 1
    return size_counter


shirt_size = ["XS","S","L","L","XL","S"]    # 학생들이 원하는 사이즈
ret = solution(shirt_size)
print("Solution : return value of the function is",ret," .")
