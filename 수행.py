from turtle import *

print("10527진재웅")

def 직렬저항(c):
    for i in range(c):
        fd(30)
        lt(70)
        fd(30)
        rt(145)
        for a in range(2):
            fd(55)
            lt(145)
            fd(55)
            rt(145)

        fd(55)
        lt(145)
        fd(30)
        rt(70)
        fd(30)

def 배터리(c):
    for i in range(c):
        fd(30)
        rt(90)
        fd(14)
        bk(28)
        fd(14)
        lt(90)
        up()
        fd(10)
        down()
        rt(90)
        fd(25)
        bk(50)
        fd(25)
        lt(90)
        fd(30)

def 병렬저항():
    fd(30)
    lt(90)
    x,y = pos()
    fd(50)
    rt(90)
    직렬저항(1)
    rt(90)
    fd(50)
    up()
    goto(x,y)
    down()
    fd(50)
    lt(90)
    직렬저항(1)
    lt(90)
    fd(50)
    rt(90)
    fd(30)


def 입력():
    DR = []
    PR = []
    bc = int(input("입력(bc) : "))
    brc = int(input("입력(brc) : "))
    prc = int(input("입력(prc) : "))
    for i in range(brc):
        DR.append(int(input("입력(직렬저항) : ")))
    for i in range(prc):
        b = []
        b.append(int(input("입력(병렬저항1) : ")))
        b.append(int(input("입력(병렬저항2) : ")))
        PR.append(b)
    return bc,brc,prc,DR,PR

def 계산(t):
    R = 0
    for i in range(0,t[2]):
        R += sum(t[3])
        R += 1/(sum(t[4][i])/int((t[4][i][0])*int(t[4][i][1])))
    return R

while True:
    lt(180)
    speed(0)
    d = 입력()
    배터리(d[0])
    fd(60*(d[1]+d[2]))
    rt(90)
    fd(150)
    rt(90)
    직렬저항(d[1])
    for i in range(d[2]) :
        병렬저항()
    rt(90)
    fd(151)
    home()
    ht()
    l = 계산(d)
    print("전체 저항은 : %dΩ입니다" %(l))
    f = input("다시 할까요?(y/n) : ")
    if f == "n":
        break
    else:
        st()
        reset()

mainloop()
