#-------------------------------------------------게임설정----------------------------------------------------------------
import  pygame # 파일 불러오기    [ pygame 함수 사용 가능 ]
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_DOWN , K_RIGHT , K_LEFT
                # 파이게임에 게임 종료 , 직각 , 키 눌렸을때 ,위 키 , 오른쪽 , 왼쪽

import random # 파일 불러오기 [ random 난수에 관련된 함수를 사용 할 수 있다 ]
import  sys # 파일 불러오기 [ sys 컴퓨터에 관련된 함수르 사용 할 수 있다 ]
#--------------------------------------------------기본구성---------------------------------------------------------------
pygame.init()   # 파이게임 초기값 [ 처음 실행 했을 초기값=기본값 ]
화면 = pygame.display.set_mode( (600,600) ) # 화면 구성[ 화면 크기 설정 함수 ]
시간 = pygame.time.Clock()    # 파이게임의 시간체크 [ 게임 시간 체크해주는 함수 ]

음식 = [] # 여러개의 음식를 담아주는 리스트 선언
뱀 = []  # 여러개의 뱀[꼬리]을 담아주는 리스트 선언
(가로 , 세로 ) = ( 20 , 20 )    # 가로 세로 길이
#--------------------------------------------------음식생성---------------------------------------------------------------
def 음식생성() : # 함수 선언[만들기]
    while True : # 계속 받복하기
        위치 = ( random.randint( 0 , 가로-1 ) , random.randint( 0 , 세로-1 ))
        # 가로( 0 부터 19까지 난수생성 )  ,  세로( 0 부터 19까지 난수생성 )
        if 위치 in 음식 or  위치 in 뱀 :
            # 해당 위치에 음식이 있거나  뱀이 있으면
            continue    # 반복문 다시 실행
        음식.append( 위치 )
        break # 반복문 끝내기
#-------------------------------------------------음식배치----------------------------------------------------------------
def 음식배치(위치) : # 함수 선언[민들기]
    삭제대상 = 음식.index(위치)  #해당 위치[인수]에 음식이 존재하면
    # index : 인덱스[색인=검색]
    # 음식.index( 위치 ) : 음식 리스트에 위치의 순서번호를 알려준다
    del 음식[삭제대상]       #del = delete : 삭제
    음식생성()      # 삭제후 다시 음식생성 하기 => 함수호출
#--------------------------------------------------그리기----------------------------------------------------------------
def 그리기 ( 종료메시지 ) : # 종료메시지를 받는 함수 선언
    화면.fill( ( 0 , 0 , 0 ) ) # fill 그리기함수
        # ( 0 , 0 , 0 ) : 펜 색상함수
    for food in 음식 :
        pygame.draw.ellipse( 화면 , ( 204 , 255 , 0 ) , Rect( food[0]*30 , food[1]*30 , 30 ,30 ) )
            # ellipse : 타원 그려주는 함수             모형함수( x축 위치       y축 위치  가로크기 세로 크기
    for body in 뱀 : # 뱀 리스트에 존재에는 변수 만큼 그리기
        pygame.draw.rect( 화면 , ( 51 , 204 , 255 ) ,  Rect( body[0]*30 , body[1]*30 , 30 ,30 ) )

    if 종료메시지 != None : # 해당 메시지가 존재하면 [ 인수가 존재하면 ]
        화면.blit( 종료메시지 , (150 , 300)) # x축:150 y축:300 위치에 종료메시지 띄우기

    pygame.display.update() # 최근 실행 코드로 변경해주는 함수
#--------------------------------------------------실행코드---------------------------------------------------------------
키 = K_UP # 게임실행 했을떄 체음에 위로 올라가기
종료메시지 = None # 종료메시지 변수에는 None[없음] 저장
게임종료 = False # 게임종료 변수에 False 저장
점수 = 0 # 0으로 저장

뱀.append( (int(가로/2) , int(세로/2 ) ) ) # 화면에 가운데부터 뱀꼬리 추가

myfont = pygame.font.SysFont( "malgungothic" , 30 )

for i in  range(10) : # 반복문 갯수만큼 음식 생성 => 음식 총 갯수
    음식생성( ) # 음식생성 함수 불러오기

while True :  # 계속 반복하기

    for 동작 in pygame.event.get() : # 파이게임에서 이벤트[작동]가 발생 했을때
        if 동작.type == QUIT : # 이벤트가 종료이면
            pygame.quit()   # 파이게임 종료 함수
            sys.exit()  # 시스템 종료 함수
        elif 동작.type == KEYDOWN : # 키을 눌렸을때
            키 = 동작.key  # 동작에서 눌러진 key 를 키 볌수에 저장
#-----------------------------------------------------------------------------------------------------------------------
    if not 게임종료 :   # 게임종료가 아니라면[False]
        if 키 == K_LEFT : # 왼쪽 키를 눌렸을때
            몸체 = ( 뱀[0][0] -1  , 뱀[0][1] )
                # x축[-] 왼쪽으로 이동
        elif 키 == K_RIGHT : # 오른쪽 키를 눌렸을때
            몸체 = ( 뱀[0][0] +1 , 뱀[0][1] )
                # x축[+] 오른쪽으로 이동
        elif 키 == K_UP : # 위쪽 키를 눌렸을때
            몸체  = ( 뱀[0][0] , 뱀[0][1] -1 )
                # y축으로 [-] 위쪽으로 이동
        elif 키 == K_DOWN : # 아래쪽 키를 눌렸을때
            몸체  = ( 뱀[0][0] , 뱀[0][1] +1 )
                # y축으로 [+] 아래쪽으로 이동

        # 뱀이 자기 몸에 닿았을때 / 화면 밖으로 나갔을때
        if 몸체 in 뱀 or 몸체[0] < 0 or 몸체[0] >= 세로  or 몸체 [1] < 0 or 몸체[1] >= 가로 :
            종료메시지 = myfont.render("게임 종료 최종점수 : "+str(점수)+"점",True , (255,255,0) )   # 게임종료 최종점수 : 점수로 하기
            게임종료 = True  # 게임 종료을 참으로 하기


        뱀.insert( 0 , 몸체 ) # 뱀에 삽입
        if 몸체 in 음식 :   # 음식 리스트에 몸체가 포함되어 있으면
            # 뱀의 몸이 음식에 닿았을때
            음식배치( 몸체 )  # 음식배치 함수 불러오기
            점수 += 1 # 점수에 1 더하기
        else:   # 아니면
            뱀.pop() # 뱀 리스트의 마지막 삭제하기

    그리기( 종료메시지 ) # ?
    시간.tick(5) # ?
