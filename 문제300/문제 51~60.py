# 리스트

# 051.
movie_rank = ["닥터 스트레인지","스플릿","럭키"]

# 052.
movie_rank.append("배트맨")

# 053.
movie_rank.insert(1,"슈퍼맨")

# 054.
movie_rank.remove("럭키")

# 055.
del movie_rank[2:4]

# 056.
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","Go","C#"]
langs = []
langs = lang1 + lang2

# 057.
nums = [1,2,3,4,5,6,7]
print(max(nums));print(min(nums))

# 058.
총합 = 0
nums = [1,2,3,4,5]
for 반복 in nums :
    총합 += 반복
print(총합)

# 059.
개수 = 0
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
for 반복 in cook :
    개수 += 1
print(개수)

# 060.
합계 = 0
nums = [1,2,3,4,5]
for 반복 in nums :
    합계 += 반복
print(합계/5)
