# 반복문

# 151.
리스트 = [3,-20,-3,44]
for 반복 in 리스트 :
    if 반복 < 0 :
        print(반복)

# 152.
리스트 = [3,100,23,44]
for 반복 in 리스트 :
    if 반복%3 == 0 :
        print(반복)

# 153.
리스트 = [13,21,12,14,30,18]
for 반복 in 리스트 :
    if 반복 < 20 and 반복%3 == 0 :
        print(반복)

# 154.
리스트 = ["I","study","python","language","!"]
for 반복 in 리스트 :
    if len(반복) >= 3 :
        print(반복)

# 155.
리스트 = ["A","b","c","D"]
for 반복 in 리스트 :
    if 반복.isupper() :
        print(반복)

# 156.
리스트 = ["A","b","c","D"]
for 반복 in 리스트 :
    if 반복.islower() == True :
        print(반복)

# 157.
리스트 = ["dog","cat","parrot"]
for 반복 in 리스트 :
    print(반복[0].upper()+반복[1:])

# 158.
리스트 = ["hello.py","ex01.py","intro.hwp"]
for 반복 in 리스트 :
    이름,확장자 = 반복.split(".") ; print(이름)

# 159.
리스트 = ["intro.h","intro.c","define.h","run.py"]
for 반복 in 리스트 :
    이름,확장자 = 반복.split(".")
    if 확장자 == "h" :
        print(이름)

# 160.
리스트 = ["intro.h","intro.c","define.h","run.py"]
for 반복 in 리스트 :
    이름,확장자 = 반복.split(".")
    if 확장자 == "h" or "c" :
        print(이름)