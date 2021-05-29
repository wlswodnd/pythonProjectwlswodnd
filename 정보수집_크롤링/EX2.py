from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수 제공
import urllib.request as ur
    # URL : 인터넷 주소 : www.naver.com

# 1. 인터넷 주소 열기
url = "https://movie.naver.com/movie/running/current.nhn"

# 2. 주소 열어서 웹문서 변수에 저장
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all("ul",{"class":"lst_detail_t1"})

print(태그)

# 영화 순위 크롤링 하기
# 1. 인터넷 주소 열기
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

# 2. 주소 열어서 웹문서 변수에 저장
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all("div",{"class":"tit3"})

print(태그)