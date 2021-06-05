# Cox Pro 2급_2차시

# 문제 5
def solution (attack,recovery,hp):
    count = 0
    while(True):
        count += 1
        hp -= 30
        if hp <= 0 :
            break
        hp += 10
    return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack,recovery,hp)
print("Solution 함수 결과  :",ret,".")