# 객체지향2

class car(object):
    """
    Car class
    Author : Yu
    Date : 2026.01.22
    """
    # 클래스 변수 : 모든 인스턴스가 공통적으로 갖고있는 속성
    car_count = 0 
    
    def __init__(self, company, details): # init 블록 내부가 바로 네임스페이스
        self.company = company
        self.details = details
        car.car_count += 1
    def __str__(self): # 프린트문으로 문자열을 출력하는 사용자 입장에선 __str__을 하고
        return f'str : {self.company} - {self.details}'
    def __repr__(self): # 얘는 개발자 레벨에서 객체값을 엄격하게 규정하여 반환할 때에 사용한다.
        return f'repr : {self.company} - {self.details}'
    
    def detail_info(self):
        print(f'Current id : {id(self)}')
        print(f'Car Detail Info : {self.company} {self.details.get('price')}')
    def __del__(self):
        car.car_count -=1
        

#Self 의미
car1 = car('Ferrari', {'color' : 'White', 'horsepower' : 680, 'price' : 700000000})
car2 = car('BMW', {'color' : 'Black', 'horsepower' : 450, 'price' : 120000000})
car3 = car('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 60000000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car1)==id(car3))

print(car1.company == car2.company)
print(car1 is car2)

# dir & __dict__
print(dir(car1))
print(dir(car2)) 
# 인스턴스가 가지고 있는 속성과 메소드를 보기 위해 dir로 반환된 리스트 값을 출력해서 확인한다.

print(car1.__dict__)
print(car2.__dict__)
#dict는 키와 벨류로 모든 개별 속성 값들을 전부 반환함

# 클래스 정보를 파악할 때 dir, dict가 유용하게 쓰인다

# 선언한 메소드 호출
car1.detail_info()
car2.detail_info()
#셀프를 통해 해당 인스턴스 객체를 그대로 삽입한다!

print(car1.__class__, id(car1.__class__))
print(car2.__class__, id(car2.__class__))
# car1이나 car2, car3의 클래스는 car로 동일하니까!
print(id(car1.__class__) is id(car2.__class__))

# 아래의 클래스 자체의 인스턴스 메소드는 호출 불가, 
# 반환값으로 self(인스턴스)가 input으로 들어와야 하는데 괄호가 비어 있으니까!
# car.detail_info()
# 대신 self의 input값을 직접 넣어주면 사용 가능!
car.detail_info(car1)

# 클래스 변수 확인
print(car1.__dict__,'\n') # 인스턴스 개별 속성에선 클래스변수가 안나옴

print(dir(car1)) # 인스턴스의 모든 속성 & 메소드 확인에서는 car_count가 나온다!

# 접근
print(car1.car_count)
print(car.car_count)

del car2
print(car.car_count)

# 만약에 car_count가 네임스페이스 안에도 있고 클래스 변수로도 선언되어 있다면
# 
# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 클래스 변수와 동일한 변수의 인스턴스 변수 생성 가능(네임스페이스에서 검색 후 상위(클래스 변수, 부모 클래스 변수) 단위 검색)
