# 문자열

# 031.
a = "3"
b = "4"
print(a+b)
# 예상 결과
# 34

# 032.
print("Hi"*30)
# 예상 결과
# HiHiHi

# 033.
print("-"*80)

# 034.
t1 = "python"
t2 = "java"
t3 = t1 + " " + t2 + " "    # 문자끼리 +로 연결
print(t3*4)

# 035.  %s : 문자 형식  %d : 정수 형식
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % ( name1 , age1 ))
print("이름: %s 나이: %d" % ( name2 , age2 ))

# 036.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = "13"
김민수 = '{0},{1},{2},{3}'.format("이름:",name1,"나이:",age1)
이철희 = '{0},{1},{2},{3}'.format("이름:",name2,"나이:",age2)
print(김민수)
print(이철희)

# 037.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = "13"
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


# 038.
상장주식수 = "5,969,782,550"
제거 = 상장주식수.replace(",","")
print(int(제거))

# 039.
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

# 040.
print("   삼성전자   ".strip() )
