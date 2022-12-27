# ------------------------------------------------------------------------------------------------
#
#
# ------------------------------------------------------------------------------------------------
num1=[1,2,3,4]
num2=[1,1,1,1]
msg='Good'
greeting='2023'

# 연산 => 덧셈, 곱셈
num3=num1+num2
data=msg+greeting

print(num3,data,sep='\n')

num4=num1*3
data1=msg*3
print(num4,data1,sep='\n')

# ------------------------------------------------------------------------------------------------
# Point 클래스
# 변수
#   클래스 변수 => color
#   인스턴스 변수 => x,y
# 메서드
#   시스템 메서드 => 생성자 메서드 __init__() : 인스턴스 변수 생성 및 초기화
#   getter/setter 메서드 => 비공개 속성 값 읽기/쓰기 메서드
#   비공개 메서드 => 없음( 형식 def __메서드명() )
#   커스텀 메서드 => def printPoint()
# ------------------------------------------------------------------------------------------------
class Point:
    # 클래스 변수
    color='blue'

    # 생성자 메서드 => 인스턴스 변수 생성 및 초기화
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    # 시스템 메서드 콜백(callback)으로 상황이 맞으면 자동 호출
    # 객체 + 객체 시 자동 호출
    def __add__(self,other):
        print('__add__ () ')
        return (self.x + other.x , self.y + other.y)
    
    # 객체 - 객체 시 자동 호출
    def __sub__(self,other):
        print('__sub__ () ')
        return (self.x - other.x , self.y - other.y)

    # 객체 * 객체 시 자동 호출
    def __mul__(self,other):
        print('__mul__ () ')
        return (self.x * other.x , self.y * other.y)

    # 메서드
    def printPoint(self):
        print(f'Point({self.x},{self.y})')

# 객체 생성
p1=Point(10,10)
p2=Point(5,5)

p1.printPoint()
p2.printPoint()

# 객체 연산
print(f'p1+p2=> {p1+p2}')
print(f'p1-p2=> {p1-p2}')
