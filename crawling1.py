#크롤링 : 웹페이지에서 월하는 문자를 가져오는 기술
import urllib.request

#가져올 페이지의 주소(URL)을 써줍니다
url = urllib.request.rulopen('https://www.naver.com/')

# 해당 웹페이지의 웹코드를 읽는다
html = url.read()
문자열 = html.decode()

print(문자열)