# Cox Pro 2급_1차시

# 문제 6

def solution(number):
    count = 0   # 박수 횟수
    for i in range(1,number + 1) : # 1 부터 40 까지 반복
        current = i    # 현재 숫자
        temp = count    # 임시변수에 박수횟수 저장
        while current != 0 : # 0이 아닐때까지 반복
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9 :
                # 만약에 현재 숫자가 나누기 10 했을때 나머지가 3 혹은 9 이면
                count += 1  # 박수 횟수 올리 기
                print("pair",end= "")   # 박수 출력
            current = current // 10 # 현재 숫자 // 10 자릿수 내리기
        if temp == count :
            print(i,end="")
        print(" ",end="")
    print("")
    return count

number = 40 # 1~40
ret = solution(number)

print("Solution : return value of the function is",ret,".")