from bs4 import BeautifulSoup


html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">123</a>' \
       '  </div>' \
       '</td>'

# 1. 조회
def ex1():
    bs = BeautifulSoup(html,'html.parser')
    print(bs,type(bs))

    tag = bs.a
    print(tag,type(tag))

# 2. Attribute 값 받아오기
def ex2():
    bs = BeautifulSoup(html,'html.parser')

    tag = bs.td
    print(tag['class'],type(tag['class']))
    print(tag['id'],type(tag['id']))
    print(tag.attrs,type(tag.attr))

    tag = bs.div
    # print(tag['id']) # error

def ex3():
    bs = BeautifulSoup(html,'html.parser')

    tag = bs.find('div', attrs={'class':'tit3'})
    # print(tag)

    tag = bs.find('div')
    # print(tag)

    tag = bs.find('td', attrs={'class':'not_exist'})
    # print(tag)

    tag = bs.find(attrs={'title':'범죄도시'})
    print(tag)

def ex4():
    bs = BeautifulSoup(html,'html.parser')

    tag = bs.select("td div a")
    print(tag)

    # text = tag.contents[0]
    # print(text)
# 태그로 뽑는 걸 했으면 "태그 안 value 불러오기"
 


ex4()