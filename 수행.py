import turtle as t

print("10527진재웅")

def 직렬저항():
    t.forward(100)
    t.left(70)
    t.forward(30)
    t.right(145)
    t.forward(55)
    t.left(145)
    t.forward(55)
    t.right(145)
    t.forward(55)
    t.left(145)
    t.forward(55)
    t.right(145)
    t.forward(55)
    t.left(145)
    t.forward(30)
    t.right(70)
    t.forward(100)

def 배터리():
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.right(180)
    t.forward(50)
    t.left(180)
    t.forward(25)
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()
    t.left(90)
    t.forward(16)
    t.right(180)
    t.forward(32)
    t.right(180)
    t.forward(16)
    t.right(90)

배터리()
직렬저항()
