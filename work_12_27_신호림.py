# ------------------------------------------------------------------------------------------------
# 주소록 클래스
# ------------------------------------------------------------------------------------------------
class Contact:

    def __init__(self,name,phone,home,email):
        self.name = name
        self.phone = phone
        self.home = home
        self.email = email

me=Contact('신호림','010-3113-0782','053)***-****','****@knu.ac.kr')


# ------------------------------------------------------------------------------------------------
# 은행 관리 업무에 필요한 클래스
# ------------------------------------------------------------------------------------------------
class Client:

    Bank='신한'

    def __init__(self,name,account,balance,id,phone,addr):
        self.name = name
        self.account = account
        self.balance = balance
        self.__id = id
        self.__phone = phone
        self.__addr = addr

    def get__id(self): return self.__id
    def get__phone(self): return self.__phone
    def get__addr(self): return self.__addr

    def set__phone(self,phone): self.__phone=phone
    def set__y(self,addr): self.__addr=addr

me=Client('신호림','110-441-135872','5000','960507-1******','010-3113-0782','신암동')