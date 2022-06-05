import urllib.request
import BeautifulSoup

url = urllib.request.rulopen('https://www.naver.com/')
html = url.read()
문자열 = html.decode()

soup = BeautifulSoup(문자열, 'html.parser')
tag = soup.find('title')
result = tag.text.strip()
print(result)