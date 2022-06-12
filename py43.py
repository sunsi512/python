string = 'Hello python'

# 글자 시작위치 찾기
idx = string.find('pyth')         # 위치
print(idx)

# replace : 글자 바꾸기
result = string.replace('python', 'World')
print(result)

# 171p
s = 'Life is too short'
print(s.replace('short', 'long'))

a = '010-2345-6789'
result = a.replace('-','')
print(result)

# 173p
while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-') !=6:
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0]
    print('생년월일은 {}입니다.'.format(birthday))
    break