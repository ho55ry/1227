# --------------------------------------------------------------------------------------------
# 클래스가 메모리에 들어가야지 사용가능.
# 클래스가 메모리에 들어가면 = 객체
# 객체 중에 하나하나가 인스턴스 ex) int instance, str ins, dict ins ...  // 객체가 더 큰 개념
# 문법 : class 클래스명:
# --------------------------------------------------------------------------------------------
# 강아지                                         class Dog:
# 이름                                              name='메리'
# 성별                                              gender='여자'     속성, 필드, 멤버변수
# 몸무게                                            weight=3.4       (Attribute,field)
# 색상         => 속성, 특징, 외형 ==> 변수          color='흰색'
# 앉아                                              def sit(): 코드                    
# 기다려                                            def wait(): 코드   메서드, 멤버함수  
# 짖는다                                            def bark(): 코드   (Method)
# 꼬리친다     => 동사             ==> 함수          def wag(): 코드
# :
# --------------------------------------------------------------------------------------------
#
#  사용자 정의 클래스 
class Dog:
    legs=4 #클래스 변수 (<-> 인스턴스 변수)  : 클래스 전체가 가지는 속성
    # 생성자 메서드 : 힙(메모리)에 생성되는 객체 초기화, 데이터 저장
    # 인스턴스 마다 고유의 속성 => 인스턴스 변수
    # 콜백 함수 = 시스템에서 호출하는 함수
    def __init__(self, name, weight, color) : # self: 각 인스턴스의 메모리 내 Heap에서의 주소
        print('Dog__init__()')
        self.name=name #'Merry'
        self.weight=weight #3.4      #인스턴스 변수. 객체마다 다른거
        self.color=color #'white'
        #self.legs=4 # <===공통적인 특성은 변수에 넣으면 안됨. 인스턴스 변수가 아님  (메모리 낭비 : 인스턴스마다 legs=4가 생기기때문)
    def bark(self):
        print(f'{self.name}가 짖는다')
    def wag(self):
        print(f'{self.name}가 꼬리를 흔든다')
    def wait(self):
        print(f'{self.name}가 기다린다')
    def eat(self,*food):
        print(f'{self.name}가 {food}를 먹는다.')


# 객체 생성  # 변수명 = 클래스명() <= 생성자 함수
MyDog=Dog('Merry',3.4,'white')
YourDog=Dog('Happy',2.8,'brown')
HisDog=Dog('장군이',7,'black')

# 객체(인스턴스) 속성 사용
# 읽기 => 변수명.속성명
print(MyDog.name,MyDog.weight)
print('클래스 변수 사용 : ',MyDog.legs, Dog.legs)

# 쓰기 => 변수명.속성명=새로운 값
MyDog.weight=4.5
print(MyDog.weight)

# 객체(인스턴스)의 메서드 사용
# 변수명.메서드명()
MyDog.bark()
YourDog.wait()
HisDog.wag()
MyDog.eat('간식','고기')