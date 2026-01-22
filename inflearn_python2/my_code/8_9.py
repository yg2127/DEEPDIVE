# 객체 지향 프로그래밍 -> 코드의 재사용, 코드 중복 방지, 유지 보수, 대형 프로젝트
# 규모가 큰 프로젝트 -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 차량1
car_company_1 = "Ferrari"
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 680},
    {'price' : 700000000}
]

# 차량2
car_company_2 = "BMW"
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 450},
    {'price' : 120000000}
]

# 차량3
car_company_3 = "Audi"
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 60000000}
]

# 리스트 구조
# 관리하기가 불편 관리하기 위해선 인덱스 번호를 알아야 함
# 인덱스 접근 시 실수 가능성, 삭제 불편
# 데이터가 많아지고 데이터를 묶으면 관리하기가 어려움
# 잘 만든 코드에선 이걸 다루는 메소드, 함수가 있음

car_company_list=['Ferrari', 'BMW','Audi']
car_detail_list=[
    {'color' : 'White', 'horsepower' : 680, 'price' : 700000000},
    {'color' : 'Black', 'horsepower' : 450, 'price' : 120000000},
    {'color' : 'Silver', 'horsepower' : 300, 'price' : 60000000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print('-'*15)

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제 (키는 유일해야 하므로), 키 조회 예외 처리 신경써야함
# 잘 만든 패키지 소스를 보면 딕셔너리 형태를 매우 많이 씀 알고리즘에서도 많이 쓴다!

# 딕셔너리 안에 딕셔너리가 있는 형태
car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : {'color' : 'White', 'horsepower' : 680, 'price' : 700000000}},
    {'car_company' : 'BMW', 'car_detail' : {'color' : 'Black', 'horsepower' : 450, 'price' : 120000000}},
    {'car_company' : 'Audi', 'car_detail' : {'color' : 'Silver', 'horsepower' : 300, 'price' : 60000000}},
]

del car_dicts[1]
print(car_dicts)
print('-'*15)

# 클래스 구조 (megic method, special method는 다음에 배운다.)
# 구조 설계 후 재사용성 증가, 코드 반복 최소화! 메소드를 활용한 데이터 다루기

class car(object):
    def __init__(self, company, details):
        self.company = company
        self.details = details
    def __str__(self): # 프린트문으로 문자열을 출력하는 사용자 입장에선 __str__을 하고
        return f'str : {self.company} - {self.details}'
    def __repr__(self): # 예는 개발자 레벨에서 객체값을 엄격하게 규정하여 반환할 때에 사용한다.
        return f'repr : {self.company} - {self.details}'
        
car1 = car('Ferrari', {'color' : 'White', 'horsepower' : 680, 'price' : 700000000})

# print(car1) 
# 메직메소드 할당을 안하면 그냥 car object 이런식의 메모리 할당만 알려준다. 
# 그래서 파이썬에서 이미 만든 매직매소드를 활용해서 자세한 정보를 출력할 수 있다.
# str 메소드와 repr 둘 다 있으면 str 먼저 사용하고 str이 없으면 repr값을 반환받아서 출력한다.

car2 = car('BMW', {'color' : 'Black', 'horsepower' : 450, 'price' : 120000000})
car3 = car('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 60000000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__) # 클래스 안에 뭐가 있는지 확인하기 위해
print(dir(car1)) # 사용할 수 있는 메타정보에 대해 알려준다. dict, dir, repr 등등이 있으니까 나중에 사용할 수 있다.

print('-'*15)

cl = []
cl.append(car1)
cl.append(car2)
cl.append(car3)

print(cl)
# 이런식으로 리스트 안의 객체값으로 인스턴스가 들어가게 될 때는 str 메서드가 있어도 repr 메서드를 통해 반환된다.

for x in cl:
    print(x) # 이건 str 메서드를 통해 출력되는 값
    print(repr(x)) # 이건 repr 메서드를 통해 반환되는 값을 출력해주고