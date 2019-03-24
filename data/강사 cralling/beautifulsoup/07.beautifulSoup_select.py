# BeautifulSoup4 : HTML Parsing library

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# 아이디가 tiger인걸 찾을꺼예요
#  <li id="tiger">호랑이</li>
# print(bs.select_one("#tiger").text)
# bs.select("ol > li:nth-child(2)")
print(bs.select_one("ol > li:nth-of-type(2)").text)

for li in bs.select("li"):
    print(li.text)