# 두 수의 합
import service_identity


a = 3
b = 2
result = a+b
print(result)
a = 3
b = 2
result = a+b
print(result)
# 코드가 길어지면 지저분해짐.

# 그렇다면 함수를 이용하자
def Sum(a,b):
    result = a+b
    print(result)
def Sub(a,b):
    result = a+b
    print(result)
def Mul(a,b):
    result = a+b
    print(result)
def Div(a,b):
    result = a+b
    print(result)

# 함수 사용
Sum(2,3)
Sum(6,3)
# 함수의 이름과 사용법을 알고 있어야함
# 초보자가 사용하기에는 어려움
# Sub(5,'3')           # 오류
# Div(7,0)             # 0 안됨

# 초보자가 사용하기 편하게 변수와 함수를 뭉쳐놓고 쉽게 제공하자
class 사칙연산 : 
    a, b = 0, 0     # self
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def 더하기(self):
        result = a + b
        print(result)
    def 빼기(self):
        result = a - b
        print(result)
    def 곱하기(self):
        result = a * b
        print(result)
    def 나누기(self):
        result = a / b
        print(result)

객체1 = 사칙연산(3,5)
객체1.빼기


class 더하기:

    def 두개더하기(self, a, b):
        print(a+b)
        return a+b
    def 세개더하기(self, a, b, c):
        print(a+b+c)
        return a+b+c
    def 네개더하기(self, a, b, c, d):
        print(a+b+c+d)
        return a+b+c+d
    def __init__(self):
        print("처음에 무조건 사용됨")
    def __del__(self):
        print("끝날때 무조건 사용됨")

객체2 = 더하기()
객체2.세개더하기(3,4,5)

# 277p
class Service:

    def __init__(self,service):
        self.service = service
        print('{}Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{}Service가 종료되었습니다.'.format(self.service))

s = Service('길 안내')
del s