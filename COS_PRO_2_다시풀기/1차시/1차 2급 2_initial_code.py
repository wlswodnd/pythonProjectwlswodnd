#You may use import as below.
#import math

def solution(price, grade):
    #Write code here.
    answer = 0
    for i in grade:
        if i == "S":
            answer = price-price*0.05
        elif i == "G":
            answer = price-price*0.1
        elif i == "V":
            answer = price-price*0.15
    return answer

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")