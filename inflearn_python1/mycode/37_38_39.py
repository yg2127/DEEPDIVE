# 클래스 = 붕어빵 기계 객체 인스턴스 등

# oop(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해

# 예제 1
# 인스턴스 = 붕어빵 틀을 가지고 찍어내는 붕어빵, 코드에서 사용할 객체
class Dog(object): #object 를 상속받음
    
    species = 'firstdog' # 클래스 속성임. 해당 클래스의 모든 객체는 이런 속성을 가지고 있음
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Dog)

# 인스턴스화

a = Dog('micky',2) # 객체
b = Dog('choco',5) # 객체
c = Dog('micky',2) # 객체


#인스턴스는 코드로 구현해서 메모리에 올라가서 
# 우리가 사용하고 활용할 수 있는 대상
# c언어의 구조체와 같은건가??

print(a==b, id(a), id(b)) # 전혀 다르다!
print(a==c, id(a), id(c)) # 안의 내용이 같아도 전혀 다르다!

# 네임스페이스 __dict__ : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도로 접근 가능
print(f'dog1 {a.__dict__}') # 딕셔너리 형태로 반환할 수 있음
print(f'dog2 {b.__dict__}')

# 인스턴스 속성 확인

print(f'{a.name} is {a.age} and {b.name} is {b.age}')

# 뭐 여기까진 c언어의 구조체와 거의 비슷해보임

if a.species == 'firstdog':
    print(f'{a.name} is a {a.species}')
    
print(f'{Dog.species} {a.species} {b.species} {c.species}')

# self에 대해서... self의 이해

class selftest:
    def func1(): # 클래스메소드
        print(f'Func1 called')
    def func2(self): # 인스턴스메소드
        print(id(self))
        print('func2 called')
    # init이 없으면 파이썬이 알아서 커버를 쳐주고 우리는 이 클래스에 어떤 정보가 필요 없다는거임
f = selftest()

print(dir(f))
print(id(f))

#
# f.func1() 
#

# 엥? 이렇게 하면 에러나는데? 
# 에러내용이 TypeError: selftest.func1() takes 0 positional arguments but 1 was given
# 매개변수가 없어야 하는데 하나가 넘어왔다는데?

f.func2()

# 머야. 클래스를 인스턴스화한 객체 f랑 self의 아이디값이 같네?

# 암묵적으로 이 클래스 내부의 매개변수를 선언하는데 self가 없다? -> 클래스 메쏘드임
# 즉 클래스에서 func1()에 self(f의 아이디값)를 넘겼는데 func1()에서 받지를 않으니까 에러가 난거임

# 그럴때는 이렇게 출력하면 된다.
selftest.func1()

#반대로 func2를 위와같이 호출하면 에러가 발생함
# selftest.func2()

# 아래에는 인스턴스화 시킨 변수를 밑에 넣어주면 에러가 안나게 된다!
selftest.func2(f)

# 클래스메소드(def에 self가 없는 경우)는 클래스를 포함한 직접 호출
# 인스턴스메소드(def에 self가 있는경우)는 직접 호출에 객체를 넣어주거나 인스턴스 호출 해야함

# 예제 3
# 클래스변수 (클래스 속성), 인스턴스 변수 (개별 객체의 속성)

class warehouse:
    # 클래스 변수
    stock_num = 0
    
    def __init__(self, name): #인스턴스메소드
        self.name = name # 인스턴스 변수
        warehouse.stock_num+=1
        
    def __del__(self):
        warehouse.stock_num-=1
        

u1 = warehouse('yugeon')
u2 = warehouse('park')

print()
print(warehouse.stock_num)

print(u1.name)
print(u2.name)

print(u1.__dict__) # 해당 객체만의 dict, init에서 선언한 내용만 출력된다
print(u2.__dict__)

print(warehouse.__dict__)

# 이제 del이 나온다

del u1
print(f'after {warehouse.__dict__}')

class dog(object): #object 를 상속받음
    
    species = 'firstdog' # 클래스 속성임. 해당 클래스의 모든 객체는 이런 속성을 가지고 있음
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return f'{self.name} is {self.age} year old'
    
    def bark(self, sound):
        return f'{self.name} says {sound}!'
    
# 예를들어서 자동차라는 클래스가 있으면 자동차의 공통 속성이 있을 수 있고
# 차종마다 개별 속성이 있을 수 있고(엔진, 미션, 가속도, 브랜드, 연식, 키로수, 이름 등등) init으로 객체의 속성 지정할 수 있고
# 자동차의 액선 (전진, 후진, 좌회전, 우회전) 등을 method로 선언할 수 있다!

# 인스턴스 생성
d1 = dog('kkk', 4)
print(d1.info())
print(d1.bark(input()))

# 네임스페이스는 각각 갖고있는 공간, 정보
# 클래스 변수는 해당 클래스, 모든 인스턴스가 공통적으로(공유) 갖고 있는 속성
# 인스턴스 변수 각각의 객체마다 갖고있는 것
# self는 인스턴스화 된 대상, 파이썬 코드에서 메모리로 올라가는 것
# 인스턴스 메소드는 self를 인자로 받는 함수들
# 인스턴스 변수는 self를 붙이고 선언하는 변수들