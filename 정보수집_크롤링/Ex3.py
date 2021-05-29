import urllib.parse

from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수 제공
import urllib.request as ur
    # URL : 인터넷 주소 : www.naver.com
지역 = input("원하는 지역을 입력 : ")
검색어 = urllib.parse.quote(지역+"날씨")
# 1. 인터넷 주소 열기
url = "https://search.naver.com/search.naver?ie=utf8&query=" + 검색어
# 2. 주소 열어서 웹문서 변수에 저장
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all("span",{"class":"todaytemp"})

print("현재 신촌의 온도는 :",태그[0].text+"도 입니다.")


# 1. 인터넷 주소 열기
url = "https://search.naver.com/search.naver?ie=utf8&query=" + 검색어   # 2. 주소 열어서 웹문서 변수에 저장
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all("span",{"class":"num"})

print("현재 신촌의 미세먼지는 :",태그[4].text+"입니다.")


# 1. 인터넷 주소 열기
url = "https://search.naver.com/search.naver?ie=utf8&query=" + 검색어
# 2. 주소 열어서 웹문서 변수에 저장
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all("span",{"class":"num"})

print("현재 신촌의 오존지수는 :",태그[6].text+"입니다.")
