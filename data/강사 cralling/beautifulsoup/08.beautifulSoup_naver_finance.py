# BeautifulSoup4 : HTML Parsing library

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
urlObj = urlopen(url)

bs = BeautifulSoup(urlObj.read(), "html.parser")

em = bs.select_one("#content > div.spot > div.today > p.no_today > em > em")
result = []

for item in em.select("span"):
    result.append(item.text)

print("오늘의 원달러 환율은 : {}".format("".join(result)))

