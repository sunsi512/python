# 1)
from re import M


while True:
    city = input('대한민국의 수도는 어디인가요? >>>')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print ('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')

#(2)
hobbies = []
while True:
    hobby = input('취미를 입력하세요(종료는 그냥 엔터) >>>')
    if hobby == '':
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else:
        hobbies.append(hobby)
print(hobbies)

#(3)
fruits = ['사과', '감귤']
count = 3

while count > 0:
    fruit = input('어떤 과일을 저장할까요?')
    if fruit in fruits:
        print('동일한 과일이 있습니다.')
        continue
    fruits.append(fruit)
    count -= 1
    print('입력이 {}번 남았습니다.'.format(count))

print('5개 과일은 {}입니다.'.format(fruits))

#(4)
count = 0
total = 0
while count < 5:
    n = int(input('{}번째 정수를 입력하세요 >>>'.format(count + 1)))
    if n <= 0:
        print('0 이하의 정수를 처리할 수 없습니다.')
        continue
    total += n
    count += 1
print('입력된 3개 암수의 총 합은 {}입니다.'.format(total))
