import random

d = 0
score = 0
f = []
c = []
word = {}

count = int(input("틀린 단어의 개수를 입력하세요 : "))

for i in range(0,count+1):
    a = input("틀린 영어 단어 입력(스펠링) : ")
    b = input("틀린 영어 단어 입력(뜻) : ")
    word[a] = b

f = word.keys()
d = random.sample(f,count)
for s in range(0,count+1):
    print(d[s],": ")
    e = input()
    if e == word[e] :
        print("맞았습니다")
        score += 1
    else:
        print("틀렸습니다")
print(score)

