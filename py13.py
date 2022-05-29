#a = 7
#b = 2
#print('{} + {} = {}'.format(a, b, a + b))         # 더하기
#print('{} - {} = {}'.format(a, b, a - b))         # 빼기
#print('{} * {} = {}'.format(a, b, a * b))         # 곱하기
#print('{} ** {} = {}'.format(a, b, a ** b))       # 제곱승
#print('{} / {} = {}'.format(a, b, a / b))         # 나누기(소수점까지)
#print('{} // {} = {}'.format(a, b, a // b))       # 나누기(소수점 뗌)
#print('{} % {} = {}'.format(a, b, a % b))         # 나머지 구하기

정수 = int(input('10 ~ 99 사이의 정수를 입력하세요 >>>'))
print('십의 자리 : {}'.format(정수 // 10))
print('일의 자리 : {}'.format(정수 % 10))
