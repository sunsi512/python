class 자동차:
    def __init__(self, 차주인, 차종):
        self.name = 차주인
        self.car = 차종
    def 차정보(self):
        print('{} 차의 주인은 {} 입니다.'.format(self.car, self.name))
    def 차변경(self, 차종):
        self.car = 차종
    def __del__(self):
        print('{}차 안내 종료'.format(self.name))

# 클래스 사용
# 객체화(클래스 사용을 위해 변수로 만들어줌)
아빠차 = 자동차('아빠', '벤츠')     #클래스 사용 1
엄마차 = 자동차('엄마', '아반떼')   #클래스 사용 2
내차 = 자동차('나', 'k5')          #클래스 사용 3

아빠차.차정보()
내차.차정보()
엄마차.차정보()
del 아빠차         # 아빠차 변수를 강제로 없앰
엄마차. 차변경('제네시스')
엄마차. 차정보()


population = 0
class Person:
    def __init__(self, name):
        global population      # 클래스보다 위에 있는 전역변수를 수정할 때
        population += 1
        print('{} is born'.format(name))
        self.name = name

    @staticmethod
    def get_population():
        print('전체 인구수: {}명'.format(population))

    def __del__(self):
        global population      # 클래스보다 위에 있는 전역변수를 수정할 때
        population += 1

man = Person('james')
woman = Person('emliy')
Person.get_population()
del man
Person.get_population()