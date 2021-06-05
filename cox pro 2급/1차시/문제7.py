# Cox Pro 2급_1차시

# 문제 7

def solution ( scores ) :
    count = 0
    for s in scores :
        if 650 <= s and s < 800 :
            count += 1
    return count

scores = [650,722,914,558,714,804,650,679,669,800]  # 수강 신청한 사람들의 점수
ret = solution( scores )

print("Solution 함수 결과 :",ret,".")