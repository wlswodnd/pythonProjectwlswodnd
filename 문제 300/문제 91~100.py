# 딕셔너리

# 091.
inventory = { "메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}

# 092.
inventory = { "메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory["메로나"][0],"원")

# 093.
inventory = { "메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory["메로나"][1],"개")

# 094.
inventory["월드콘"] = [500,7]

# 095.
아이스크림종류 = inventory.keys()

# 096.
icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}
가격 = icecream.values()
print(가격)

# 097.
icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}
가격 = icecream.values()
총합 = 0
for 합 in 가격 :
    총합 += 합
print(총합)

# 098.
icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}
new_product = {"팥빙수":2700,"아맛나":1000}
icecream.update(new_product)
print(icecream)

# 099.
keys = ("apple","pear","peach")
vals = (300,250,400)
result = dict(zip(keys,vals))
print(result)

# 100.
data = ["09/05","09/06","09/07","09/08","09/09"]
close_price = [10500,10300,10100,10800,11000]
close_table = dict(zip(data,close_price))
print(close_table)
