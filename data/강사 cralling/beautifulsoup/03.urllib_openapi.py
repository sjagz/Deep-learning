# 특정 url프로그램을 실행시켜서 결과를 가져오려해요!
from urllib.request import urlopen
from urllib.parse import urlencode

# 호출할 Open API의 url을 명시
open_api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
open_api_param = {
    "key": "430156241533f1d058c603178cc3ca0e",
    "targetDt": "20190314"
}

url = open_api_url + "?" + urlencode(open_api_param)

urlObj = urlopen(url)

data = urlObj.read().decode("utf-8")
print(data)
