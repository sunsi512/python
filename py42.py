# 146p (파이썬 지원함수)
print(2**3)     # 제곱승
print(4**2)     # 제곱승

# 형변환 (자료형 바꾸기)
str(123)       # 점수 123 -> 문자열 123
int('123')     # 문자열 '123' -> 정수 123
float('123.0')    # 문자열 '123.0' -> 실수 123.0

result = eval('100-50')    # 정수 50
print(result)

# # 149p
# expr = input('계산식을 입력하세요 >>> ')
# result = eval(expr)
# print(expr + '=' + str(result))

#abs == 절대값구하기
print(abs(-3))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lst))
print(min(lst))

# divmod == %
# pow == **

# round : 반올림
pi = 3.141592
round(pi, 2)

# sum : 리스트 안에 있는 값을 전부 더하기해서 return
sum(lst)

# len : 리스트 항목의 갯수
len(lst)

# lst의 평균
l = sum(lst) / len(lst)
print(l)

for i, j in enumerate(lst):
    print(i, ':', j)
# enumerate : 방번호와 값을 분리

# 159, 160p
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print('{}월 = {}일'.format(month + 1, day))

무지개 = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for 숫자 , 색 in enumerate(무지개):
    print('무지개의 {}번째 색은 {}입니다.'.format(숫자 + 1, 색))


점수 = []
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
while True:
    a = int(input('점수 입력 >>> '))
    if a >= 0 :
        점수.append(a)
    else:
        break
평균 = sum(점수)/len(점수)
최대 = max(점수)
최소 = min(점수)
print('평균 = {}, 최대 = {}, 최소 = {}'.format(평균, 최대, 최소))