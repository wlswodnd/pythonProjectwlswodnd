# 반복문

# 191.
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for 반복 in data :
    for i in range(4) :
        print((반복[i] * 0.00014) + 반복[i])


# 192.
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for 반복 in data :
    for i in range(4) :
        print((반복[i] * 0.00014) + 반복[i])
    print("----")

# 193.
resuit = []
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for 반복 in data :
    for i in range(4) :
        resuit.append((반복[i] * 0.00014) + 반복[i])
print(resuit)

# 194.
resuit = [[],[],[]]
순서 = 0
data = [[2000,3050,2050,1980],[7500,2050,2050,1980],[15450,15050,15550,14900]]
for 반복 in data :
    for i in range(4) :
        resuit[순서].append((반복[i] * 0.00014) + 반복[i])
    순서 += 1
print(resuit)


# 195.
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    print(반복[3])

# 196.
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    if 반복[3] >= 150 :
        print(반복[3])

# 197.
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    if 반복[3] >= 반복[0] :
        print(반복[3])

# 198.
결과 = []
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    결과.append(반복[1]-반복[2])

# 199.
결과 = []
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    if 반복[3] > 반복[0] :
        결과.append(반복[1] - 반복[2])

# 200.
리스트 = [["open","high","low","close"],[100,110,70,100],[200,210,180,190],[300,310,300,310]]
for 반복 in 리스트[1:4] :
    print(반복[3]-반복[0])
