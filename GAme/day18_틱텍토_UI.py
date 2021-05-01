
#  틱텍토 게임 만들기

from tkinter import *   # tkinter : 파이썬 UI
import random as r    # 난수 생성
from tkinter import  messagebox # 메시지 창

# 2. 버튼 함수 만들기
def 버튼(화면): # 함수 선언
    게임판 = Button(화면 ,padx = 1 , bg="alice blue",text="   ",font=("arial",60,'bold'),relief='sunken',bd = 10 )    # ?
    return 게임판    # b 반환

# 리셋----------
def 리셋():
    for i in range(3):
        for j in range(3):
            게임판[i][j]["text"]=" "
            게임판[i][j]["state"]= NORMAL

# 이기는수 함수 만들기
def 이기는수():
    for i in range(3):  # i 는 0부터 2까지 1씩 증가
        # 가로-----------
        if 게임판[i][0]["text"]==게임판[i][1]["text"] == 게임판[i][2]["text"] == 알  :
            messagebox.showinfo( "게임종료", 알+"승리")
            리셋()
        # 세로-------------
        if 게임판[0][i]["text"]==게임판[1][i]["text"] == 게임판[2][i]["text"] == 알  :
            messagebox.showinfo("게임종료", 알 + "승리")
            리셋()
        # 대각선----------
    if 게임판[0][0]["text"]==게임판[1][1]["text"]==게임판[2][2]["text"] == 알 :
        messagebox.showinfo("게임종료", 알 + "승리")
        리셋()
    if 게임판[0][2]["text"]==게임판[1][1]["text"]==게임판[2][0]["text"] == 알 :
        messagebox.showinfo("게임종료", 알 + "승리")
        리셋()
#  0.0 / 0.1 / 0.2
#  1.0 / 1.1 / 1.2
#  2.0 / 2.1 / 2.2

# 알 교체 함수
def 알교체():
    global 알
    for i in ["O","X"]: # O 혹은 X 를 i 에 대입
        if not(i == 알 ) :   #현재 알이 i 와 같지 않으면
            알 = i   # 교체
            break   # 반복문 종료

# 클릭 함수만들기
def 클릭(가로,세로):
    게임판[가로][세로].config( text = 알, state=DISABLED, disabledforeground = colour[알])
    이기는수()  # 함수 호출
    알교체()   # 알  교체 함수 불려오기
    레이블.config(text = 알  + "님 플레이어 순서입니다")



# 화면 설정
화면 = Tk()   # WINDOW에 화면 만들기
화면.title(" 틱택토 게임 ")    # 타이틀 정하기

# 알 만들기
알 = r.choice(["O","X"])
colour = { "O":"deep sky blue","X":"cyan"}

# 텍스트 만들기
레이블 = Label( text=알+"님 플래이어 순서입니다" , font=("arial",15,"bold"))     # 게임 설정
                # text= " 내용입력 "        font 글꼴명   크기  굵기
# 텍스트[레이블] 배치하기 [ 4번쨰 행[가로]에 1번째열[세로] , 세로 3칸을 병합[합치기]
레이블.grid( row = 3 , column = 0 , columnspan = 3 )    # 버튼 사이즈

게임판 = [ [  ] , [  ] , [  ] ]    # 이차원 배열

# 2. 2차원 배열에 버튼 넣기
for i in range(3):   # 3번 반복하기 [가로]
    for j in range(3):  # 3번 반복하기 [세로]
        게임판[i].append(버튼(화면))
        게임판[i][j].config( command=lambda  row=i , col=j:클릭(row,col))
        게임판[i][j].grid(row = i , column = j )

화면.mainloop()   # 화면 반복 실행하기