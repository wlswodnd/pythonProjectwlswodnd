# 크롤링 : 인터넷에서 데이터 추출하기

from bs4 import BeautifulSoup as bs
import urllib.request as ur

# 1. 인터넷 주소 열기
url = "https://quotes.toscrape.com/"
html = ur.urlopen(url)  # 해당 url 파이썬에서 열기해서 html 변수에 저장

# 3. read() : 인터넷에서 읽어오기
soup = bs(html.read(),"html.parser")

# 4. 읽어온파일중 "span" 찾아서 첫번쨰 글자 가져오기
print(soup.find_all("span")[0].text)
# 마크업언어[html] 에서 <span> 태그를 찾아서 태그 사이에 있는 텍스트 가져오기

# find_all()  : 찾는값 모두 가져오기
print(soup.find_all("span")[2].text)

# find_all()  : 찾는값 모두 가져오기
print(soup.find_all("span")[4].text)

# 모든 span 출력
for i in soup.find_all("span") :
    print(i.text)

# div에 포함된 해당 클래스만 찾기
for i in soup.find_all("div",{"class" : "quote"}) :
    print(i.text)
