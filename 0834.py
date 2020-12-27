from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
res = urlopen(req)
# 네이버 영화의 인코딩 타입이 euc-kr이라 cp949로 디코딩함
html = res.read().decode('cp949')

bs = BeautifulSoup(html,'html.parser')
tags = bs.findAll('div', attrs={'class':'tit3'})


# for tag in tags:
    # 가져온 tag에서 <a>안 텍스트
    # print(tag.a.text)

for index, tag in enumerate(tags):
    print(str(index)+":"+tag.a.text)