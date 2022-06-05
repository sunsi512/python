import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
html = url.read()
문자열 = html.decode()

리스트 = []
soup = BeautifulSoup(문자열, 'html.parser')
tag = soup.find_all("div", class_="tit3")
for i in tag:
    #<a>를 기준으로 자르고 <a>를 없앤다
    result = i.find('a').text.strip()
    리스트.append(result)

print(리스트)

for j in 리스트:
    print(j)
