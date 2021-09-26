#다운로드 할때 인터렉티브 셸에서 3.5버전하고 3.9버전으로 나눠서 쓰고 있음
#3.9버전에 패키지를 추가 다운로드 하기 위해서는 pip3.9(혹은 그에 상응하는 버전) install 패키지명
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')

#target = request.urlopen(url)

soup = BeautifulSoup(target, 'html.parser')

for location in soup.select('location'):
    #내부의  city, wf, tmn, tmx 태그를 찾아 출력
    print("도시:", location.select_one('city').string)
    print("날씨:", location.select_one('wf').string)
    print("최저기온:", location.select_one('tmn').string)
    print("최고기온:", location.select_one('tmx').string)
    print()
