# 특정 url의 HTML을 읽어서 내용을 출력!!

from urllib.request import urlopen

# 특정 URL에 접속해서 접속객체를 생성
urlObj = urlopen("http://localhost/index.html")
# urlObj = urlopen("http://naver.com/index.html")

print(urlObj.read().decode("utf-8"))
