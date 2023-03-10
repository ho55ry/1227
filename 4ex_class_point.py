# ------------------------------------------------------------------------------------------------
# 바둑알이 놓여지는 위치 저장 클래스
# 클래스 명 : Point
# 변수 
#       -클래스변수
#       -인스턴스변수 : x(공개용 속성), __y(비공개용 속성)
# 메서드
#       -시스템 메서드 : __init__()
#       -커스텀 메서드 : put(), show()
#       -getter/setter 메서드 : 비공개 속성의 값 읽기/쓰기
#        get속성명() / set속성명()
# ------------------------------------------------------------------------------------------------
class Point:
    # 클래스 변수 속성

    # 인스턴스 속성 초기화 및 생성 메서드 => 생성자 메서드
    def __init__(self,x,y):
        self.x=x
        self.__y=y # __붙이면 비공개 
     
    # 메서드
    def put(self):
        print(f'({self.x},{self.__y}) -- o')

    # getter/setter 메서드
    # 비공개 속성을 외부에서 접근 기능 제공 메서드
    def get__y(self): return self.__y
    def set__y(self,y): self.__y=y

# 인스턴스 (객체) 생성
p1=Point(10,5); p1.put()
#print('p1 :',p1.__dict__)

# 비공개 변수는 못바꿈. 같은 이름써서 값 바꿔도 같은 이름의 다른 변수가 추가됨
# p1.y=-5; p1.put()
# p1.__y=-5; p1.put()
# print('p1 :',p1.__dict__)

p1.set__y(-5); p1.put()
print('p1.__y : ',p1.get__y())
p1.put()