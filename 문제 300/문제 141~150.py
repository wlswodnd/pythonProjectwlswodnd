# 반복문

# 141.
리스트 = [100,200,300]
for 반복 in 리스트 :
    print(반복+10)

# 142.
리스트 = ["김밥","라면","튀김"]
for 메뉴 in 리스트 :
    print("오늘의 메뉴 :",메뉴)

# 143.
리스트 = ["SK하이닉스","삼성전자","LG전자"]
for 반복 in 리스트 :
    print(len(반복))

# 144.
리스트 = ["dog","cat","parrot"]
for 반복 in 리스트 :
    print(반복,len(반복))

# 145.
리스트 = ["dog","cat","parrot"]
for 반복 in 리스트 :
    print(반복[0])

# 146.
리스트 = [1,2,3]
for 반복 in 리스트 :
    print("3","x",반복)

# 147.
리스트 = [1,2,3]
for 반복 in 리스트 :
    print("3","x",반복,"=",3*반복)

# 148.
리스트 = ["가","나","다","라"]
for 반복 in 리스트[1:4] :
    print(반복)

# 149.
리스트 = ["가","나","다","라"]
for 반복 in 리스트[0:3:2] :
    print(반복)

# 150
리스트 = ["가","나","다","라"]
for 반복 in 리스트[::-1] :
    print(반복)