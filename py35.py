# # 함수
# # 함수란 : 개발자가 직접 만드는 기능(연산자)

# # + : +를 기준으로 왼쪽의 숫자와 오른쪽의 숫자를 더한다(기능, 더하기 연산자)
# # 무조건 2개만

# # 그러면 연산자에 제공되지 않는 기능은 너가 만들어서 써라 == 함수
# from numpy import _2Tuple


# def 연산자1(숫자1, 숫자2):
#     return 숫자1 + 숫자2

# # 숫자1 + 숫자2 
# print(3+4)
# print(연산자1(3, 4))

# print(5-2)
# def 빼기(숫자1, 숫자2):
#     return 숫자1-숫자2

# print(빼기(5,2))
# # 개발자가 직접 연산자를 만들기 : 등수

# #숫자 세 개를 더하는 기능(연산자) 만들기
# def 연산자2(숫자1, 숫자2, 숫자3):
#     결과 = 숫자1 + 숫자2 + 숫자3
#     return  결과

# print(연산자2(1,2,3))

# def 임시함수():
#     return '임시함수를 사용'       #결과
# print(임시함수())



# 함수(기능. 직접 만드는 연산자) : 나누기, 두번째 숫자가 0이면 결과를 0으로 주는 나누기
def 나누기(숫자1, 숫자2):
    결과 = 0.0
    if 숫자2 == 0:
        return 결과
    else: 
        return 숫자1 // 숫자2

print(나누기(10,2))
print(나누기(10,0))