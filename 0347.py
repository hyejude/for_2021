from bs4 import BeautifulSoup
import requests
import re

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content,"html.parser")



# print(soup.find_all(serch_function("h2")))
# print(soup.find_all(attrs={'class':'card-title'}))

# <p> 에서 tag 제외한 string만 
print(soup.p.string)
# <ul>안 하위 목록
for child in soup.ul.children:
    print(child)
# <ul> 상위 항목들 -> <body>부터 전체 <html>까지 출력
for parent in soup.ul.parents:
    print(parent)
# find_all : 원하는 부분 가져오기
print(soup.find_all(re.compile("h[1-9]")))
print(soup.find_all(['h1','p']))
# html 속성 활용하기
print(soup.find_all(attrs={'class':'card-title','id':'footer-address-list'}))