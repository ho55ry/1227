# 객체 지향 언어 기본 개념
# (유지보수 쉽게) 1.정보은닉,캡슐화 2.상속(단일,다중):재사용 3.다형성
# -----------------------------------------------------------
# 클래스 명 : Car
#   클래스 변수
#       wheel, handle, engine, brake
#   인스턴스 변수
#       brand, name, seater, color, 제로백
#   시스템 메서드
#       def __init__():
#   메서드
#       def airc():
#       def go():
#       def back():
#       def window():
# -----------------------------------------------------------
class Car:
    wheel=4; handle=1; engine=1; brake=1
    def __init__(self, brand, name, seater, color, 제로백) :
        self.brand=brand
        self.name=name
        self.seater=seater
        self.color=color
        self.제로백=제로백
    def airc(self):
        print(f'{self.name}의 에어컨이 가동한다')
    def go(self):
        print(f'{self.name}이(가) 출발한다')
    def back(self):
        print(f'{self.name}이(가) 후진한다')
    def window(self):
        print(f'{self.name}의 창문을 내린다')
    def info(self):
        print(f'브랜드 : {self.brand}, 모델명: {self.name}, {self.seater}인승, 색상 : {self.color}, 제로백 : {self.제로백}')

Car1=Car('Porsche','Cayenne',4,'White',3.3)
Car2=Car('Lamborghini','Urus',4,'Yellow',3.3)
Car3=Car('Benz','G-Class',4,'black',6.4)

Car1.airc()
Car2.go()
Car3.back()
Car1.window()
Car1.info()

# -----------------------------------------------------------
# 인스턴스와 클래스
# -----------------------------------------------------------
MyCar=Car('대우','티코',4,'빨강',5)

print(MyCar.brand, Car.handle)
print('MyCar.__dict__ : ',MyCar.__dict__)   #인스턴스의 현재 속성값 => 속성:값
print('MyCar.__class__ : ',MyCar.__class__) #인스턴스를 생성한 클래스 정보
for item in Car.__dict__.items():
    print(item)
#print('Car.__dict__ : ',Car.__dict__)


