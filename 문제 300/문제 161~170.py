# 반복문

# 161.
for 반복 in range(100) :
    print(반복)

# 162.
for 반복 in range(2002,2051,4) :
    print(반복)

# 163.
for 반복 in range(1,31) :
    if 반복%3 == 0 :
        print(반복)

# 164.
for 반복 in range(99,-1,-1) :
    print(반복)

# 165.
for 반복 in range(10) :
    print("0."+str(반복))

# 166.

for 곱 in range(1,10) :
    print("3 x",곱,"=",3*곱)

# 167.
for 곱 in range(1,10) :
    if 곱%2 != 0 :
        print("3 x",곱,"=",3*곱)

# 168.
누적 = 0
for 반복 in range(1,11) :
    누적 += 반복
print("합 :",누적)

# 169.
누적 = 0
for 반복 in range(1,11) :
    if 반복%2 != 0 :
        누적 += 반복
print("합 :",누적)

# 170.
누적 = 1
for 반복 in range(1,11) :
    누적 *= 반복
print("합 :",누적)