# BeautifulSoup4 : HTML Parsing library

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")
# find() 처음 찾은거 1개만 사용할 수 있어요!

# .text , .string, .get_text() : tag사이의 문자열 추출
# print(bs.find("h1").get_text())
# print(bs.find(id="cat").get_text())
# print(bs.find(class_="myStyle").text)
print(bs.find(text="강아지").parent)
