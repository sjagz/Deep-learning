# BeautifulSoup4 : HTML Parsing library

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# print(bs.html.body.div.ul.li.text)
# print(bs.ul.li.text) # 생략해서 표현할 수 있어요!
print(bs.ul.li.next_sibling.next_sibling)

# <li id="tiger">호랑이</li>  => Element
# tag, attribute, text
# 일단 BeautifulSoup 객체를 생성했어요!

