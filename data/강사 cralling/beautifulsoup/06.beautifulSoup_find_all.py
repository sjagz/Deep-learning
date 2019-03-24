# BeautifulSoup4 : HTML Parsing library

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")
# find_all() 조건에 맞는 element를 다 찾아요!!

# li_list = bs.find_all("li")
# for li in li_list:
#     print(li.text)

# li_list = bs.find("ul").find_all("li")
# for li in li_list:
#     print(li.text)

a_list = bs.find_all("a")
for a in a_list:
    print(a.attrs["href"])







