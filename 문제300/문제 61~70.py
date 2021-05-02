# 리스트

# 061.
price = ["20180728",100,130,140,160,170]
print(price[1:])

# 062.
nums =[1,2,3,4,5,6,7,8,9,10]
print(nums[0: :2])

# 063.
nums =[1,2,3,4,5,6,7,8,9,10]
print(nums[1: :2])

# 064.
nums = [1,2,3,4,5]
print(nums[ : :-1])

# 065.
interest = ["삼성전자","LG전자","Naver"]
print(interest[0],interest[2])

# 066.
interest = ["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print(" ".join(interest))

# 067.
interest = ["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print("/".join(interest))

# 068.
interest = ["삼성전자","LG전자","Naver","SK하이닉스","미래에셋대우"]
print("\n".join(interest))

# 069.
interest = []
string = "삼성전자/LG전자/Naver"
interest = string.split("/")

# 070.
data = [2,4,3,1,5,10,9]
data.sort()
print(data)
