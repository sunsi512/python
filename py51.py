# 클래스 : 변수 + 함수 묶어놓을 것(반)

from cv2 import watershed


전역변수 = " "

# 클래스 만드는 법(정의)
class 자동차:
    # 멤버 변수
    차종 = " "
    차주인 = " "
    차색상 = " "
    엔진 = 0

    # 클래스를 사용할 때 무조건 먼저 사용되는 함수(생성자)
    def __init__(self):
        pass
    # 클래서 멤버 함수(==매서드)
    def 차정보입력(self, name, owner, color,):
        self.차종 = name
        self.차주인 = owner
        self.차색상 = color
        print('정보입력완료')
    def 차정보(self):
        print('차는', self.차종, '차주인은', self.차주인, '차색깔은', self.차색상)


# 클래스 사용법(객체화)
내차 = 자동차()     # 1. 클래스를 변수에 담는다 (객체화 한다)
내차.차정보입력('모닝', '홍길동', '빨간색')


# 상속 : 복사붙여넣기(사람이 하지않고 컴퓨터가)
# A클래스의 코드를 B클래스에 복사붙여넣기 (A클래스 : 부모, B클래스 : 자식)

class 슈퍼카(자동차):
    # 자동차클래스가 복사붙여넣기되어있음
    부스터 = '부스터 사용 가능'      # 추가
    # 수정 (오버라이딩)
    def 차정보(self):
        print('차는', self.차종, '차주인은', self.차주인, '차색깔은', self.차색상, self.부스터)


# 클래스 사용법(객체화)
누구차 = 슈퍼카()
누구차.차정보입력('슈퍼카', '아무개', '빨간색',)
누구차.차정보()


# 286p
class Coffee:

    def __init__(self, bean):           # __init__ == 생성자(객체화할때 자동사용되는 함수)
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))


class Espresso(Coffee):
# Coffee 클래스가 복사붙여넣기 됨
    def __init__(self,bean, water):
        super().__init__(bean)         # super() : 부모
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))

coffee = Espresso('콜롬비아',30)
coffee.espresso_info()
