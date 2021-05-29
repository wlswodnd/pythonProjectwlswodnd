import urllib.parse

from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수 제공
import urllib.request as ur # 파이썬에서 html 가져오기 => urlopen
    # URL : 인터넷 주소 : www.naver.com
while True :
    모델명 = input("모델명 : ")
    검색어 = urllib.parse.quote(모델명)
    찾는문자 = "판매"

    # 1. 인터넷 주소 열기
    url = "https://search.naver.com/search.naver?ie=utf8&query="+검색어

    # 2. 주소 열어서 웹문서 변수에 저장
    html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

    # 3. read() : 인터넷에서 읽어오기
    soup = bs(html.read(),"html.parser")

    # 4. 해당 태그를 찾아서 가져오기
    태그 = soup.find_all("span",{"class":""})
    for i in 태그 :
        b = 찾는문자 in i.text
        if b :
            print("현재 모델의 출시가 :",i.text)