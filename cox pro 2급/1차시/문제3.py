# Cox Pro 2급_1차시

# 문제3

def func_a (month,day) :
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(month-1) :   # 월-1 만큼 반복하기
        total += month_list[i]  # 입력한 월의 전 월 까지 일수를 다 더하기
    total += day # 내가 입력한 월의 일수 더하기
    return total # 제외



def solution (start_month,start_day,end_month,end_day) :
    start_total = func_a(start_month,start_day) # 시작 날짜
    end_total = func_a(end_month,end_day)   # 끝 날짜
    return end_total - start_total  # 끝 날짜 - 시작 날짜



start_month = 1
start_day = 1
end_month = 2
end_day = 2
ret = solution(start_month,start_day,end_month,end_day)
print("Solution : return value of the function is",ret," .")
