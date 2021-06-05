# Cox Pro 2급_1차시

# 문제 9
def solution (characters):
    result = ""
    result = characters[0]
    for i in range (1,len(characters)) :
        if characters [i-1] != characters[i] :
            result += characters[i]
    return result

characters = "senteeeencccccceeee" # sentence 구하기
ret = solution(characters)
print("Solution : return value of the function is",ret,".")