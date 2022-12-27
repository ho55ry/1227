# ------------------------------------------------------------------------------------------------
# 사람 데이터 타입                  => 동사무소 주민 관리 프로그램
# 속성/성질/외모 ...                    Jumin
# - 이름      비공개
# - 생년월일  비공개
# - 성별
# - 상세주소  비공개
# - 동
# - 나이
# - 전화번호  비공개
# - 주민번호  비공개
# - 생애주기
#
# 기능/역할/행동 ...
# - 전체 정보 확인
# - 기본 정보 확인
# 
# ------------------------------------------------------------------------------------------------

class Jumin:
    # 클래스 변수 : 모든 인스턴스 함께 사용
    Dong='신암동' # 비공개 원하면 __Dong='신암동'   # 클래스 내에서는 사용 가능

    # 생성자 메서드
    def __init__(self,name,birth,gender,addr,age,phone,id,lifecycle):
        self.__name = name
        self.__birth = birth
        self.gender = gender
        self.__addr = addr
        self.age = age
        self.__phone = phone
        self.__id = id
        self.lifecycle = lifecycle

    # get/set 메서드 => 비공개 속성 접근 여부 메서드
    # 전화번호, 주소는 변경 될 수 있음 => set 메서드 필요
    def set__phone(self,phone):
        self.__phone = phone
    def set__addr(self,addr):
        self.__addr = addr

    # 비공개 메서드

    # 일반 메서드 => 인스턴스 메서드
    def allinfo(self):
        print(f' ------ [ 개인정보 상세 ] ------ ')
        print(f' - 이름 : {self.__name}- ')
        print(f' - 생년월일 : {self.__birth}- ')
        print(f' - 성별 : {self.gender}- ')
        print(f' - 상세주소 : {self.__addr}- ')
        print(f' - 나이 : {self.age}- ')
        print(f' - 전화번호 : {self.__phone}- ')
        print(f' - 주민번호 : {self.__id}- ')
        print(f' - 생애주기 : {self.lifecycle}- ')

    def info(self):
        print(f' ------ [ 개인정보 ] ------ ')
        print(f' - 성별 : {self.gender}- ')
        print(f' - 나이 : {self.age}- ')
        print(f' - 생애주기 : {self.lifecycle}- ')

