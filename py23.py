# for 변수명 in range(10):

# while
# import time

# 기준점 = 0
# while 기준점<10:
#    time.sleep(1)         #1초동안 멈춤
#    print('10은 5보다 큽니다')
#    기준점 += 1
# print('프로그램 종료')


# '''
#  while 조건:
#     조건이 맞을때마다 실행할 코드
# '''

#예제) 10번 출력하기
# num = 1
# while num < 11:
#     print(num, '번 했습니다.')
#     num += 1

# n = 10
# while n >= 1:
#     print(n)
#     n -= 1


# 정수 = int(input('정수를 입력하세요>>>'))
# ㅁ = 1
# while ㅁ < 정수+1:
#      print(ㅁ, '번째 Hello')
#      ㅁ += 1


# #2
배수 = 0 
while 배수 <= 100:
    if 배수 % 7 == 0:
        print(배수)
        배수 += 1
    else:배수 += 1

dan = 2
while dan <= 9:
    n = 1
    while n <=9:
        print('{}*{}={}'.format(dan, n, dan*n))
        n += 1
    dan += 1